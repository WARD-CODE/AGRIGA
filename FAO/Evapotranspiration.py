import pyeto as pt
import math as m
import datetime
import requests as rq



"""
            ET0 (evapotranspiration): mm day^-1 (millimeters per day)
            Rn (net radiation): MJ m^-2 day^-1 (megajoules per square meter per day)
            G (soil heat flux density): MJ m^-2 day^-1
            Tmean,Tmin,Tmax (mean daily air temperature at 2m height): °C (degrees Celsius)
            RHmax,Rmin maximum and minimum relative humidity [%],
            u2(ws) (wind speed at 2m height): m s^-1 (meters per second)
            es_mean (saturation vapor pressure): kPa (kilopascals)
            ea_mean (actual vapor pressure): kPa (kilopascals)
            Δ(delta) (slope of saturation vapor pressure curve): kPa °C^-1
            γ(gamma) (psychrometric constant): kPa °C^-1

"""
class ETO:

    def __init__(self, **kwargs):
        
        self.wd = {}
        self.wd["Tmin"] = kwargs["tmin"]
        self.wd["Tmax"] = kwargs["tmax"]
        self.wd["Tmean"] = kwargs["tmean"]
        self.wd["Hmin"] = kwargs["hmin"]
        self.wd["Hmax"] = kwargs["hmax"]
        self.wd["lat"] = kwargs["lat"]
        self.wd["lon"] = kwargs["lon"]
        self.wd["alt"] = kwargs["alt"]
        self.wd["cloud"] = kwargs["cloud"]
        self.wd["P"] = kwargs["pressure"]
        self.wd["ws"] = kwargs["wind_speed"]

        self.cd = {}

    def calculation(self):
        # constants
        now = datetime.datetime.now()
        sigma = 4.904e-9 #s Stefan-Boltzmann constant MJ K-4 m-2 day-1
        albedo = 0.23
        Gsc = 0.0820 
        
        J = now.timetuple().tm_yday
        G = 0.0
        self.wd["lat"] = m.radians( self.wd["lat"] )
        self.wd["lon"] = m.radians( self.wd["lon"] )
        # 1-Slope of the saturation vapor pressure curve (kPa/°C)
        self.cd["delta"] = 4098 * (0.6108 * m.exp((17.27 * self.wd['Tmean']) / ( self.wd['Tmean'] + 237.3))) / (( self.wd['Tmean'] + 237.3) ** 2)#verified
        print(self.cd["delta"])
        # 2-Actual vapor pressure from from the minimum relative humidity
        self.cd["E0_tmin"] = 0.611 * m.exp((17.27 * self.wd['Tmin'])/(self.wd['Tmin'] + 237.3))
        self.cd["E0_tmax"] = 0.611 * m.exp((17.27 * self.wd['Tmax'])/(self.wd['Tmax'] + 237.3))

        self.cd["ea_min"] = self.wd['Hmin'] / 100 * self.cd["E0_tmax"]
        
        # 3-Actual vapor pressure from from the maximum relative humidity
        self.cd["ea_max"] = self.wd['Hmax'] / 100 * self.cd["E0_tmin"]
        
        
        # 4-Mean actual vapour pressure (kPa)
        self.cd["ea_mean"] = (self.cd["ea_min"] + self.cd["ea_max"])/2 #verified
        print(self.cd["ea_mean"])
        # 5-Mean saturation vapour pressure (kPa) 
        self.cd["es_mean"] = (self.cd["E0_tmin"] + self.cd["E0_tmax"])/2 #verified
        print(self.cd["es_mean"])
        # solar declination
        self.cd["sd"] = m.degrees(0.409 * m.sin(2*m.pi /365 * J - 1.39)) #verified
        print(self.cd["sd"]) 
        # sunset hour angle
        self.cd["sh"] = m.acos(-m.tan(self.wd["lat"]) * m.tan(self.cd["sd"]))#verified
        
        # Inverse relative distance Earth-Sun
        self.cd["inv_d"] = 1 + 0.033 * m.cos(2 * m.pi * J / 365) #verified
        print(self.cd["inv_d"])
        # Extraterestrial radiation Ra
        self.cd["Ra"] = (24 * 60 / m.pi) * Gsc * self.cd["inv_d"] * ((self.cd["sh"] * m.sin(self.wd["lat"]) \
            * m.sin(self.cd["sd"])) + (m.cos(self.wd["lat"]) * m.cos(self.cd["sd"]) * m.sin(self.cd["sh"])))#verified
        
        # clear –sky radiation Rs0
        self.cd["Rs0"] = (0.75 + 2*m.pow(10,-5)*self.wd["alt"])* self.cd["Ra"]
        
        # solar radiation
        self.cd["Rs"] = self.cd["Ra"] * (0.25 + 0.5 * (1 - self.wd["cloud"] / 100))
        # 6-Net shortwave radiation
        self.cd["Rns"] = (1-albedo)*self.cd["Rs"]

        # 7-Net longwave radiation
        p1 = sigma * ((self.wd["Tmax"] + 273.16) ** 4 + (self.wd["Tmin"] + 273.16) ** 4) / 2
        p2 = 0.34 - 0.14 *m.sqrt(self.cd["ea_mean"])
        p3 = 1.35 * (self.cd["Rs"]/self.cd["Rs0"]) - 0.35
        self.cd["Rnl"] =  p1*p2*p3 

        # 8- net radiation
        self.cd["Rn"] = self.cd["Rns"] + self.cd["Rnl"]  

        # 9- Atmospheric pressure (kPa)
        self.cd["pr_atm"] = (101.3*(293 - 0.0065*self.wd["alt"])/293) ** 5.26

        # 10-Psychrometric constant (gamma)
        self.cd["gamma"] = 0.665e-3 * self.cd["pr_atm"]

        # 11-Evapotranspiration 
        p1 = 0.408 * self.cd["delta"]*(self.cd["Rn"] - G)
        p2 = self.cd["gamma"] * 900 * (self.cd["es_mean"] - self.cd["ea_mean"]) * self.wd["ws"]
        p3 = self.cd["delta"] + self.cd["gamma"]*(1 + 0.34*self.wd["ws"])

        self.cd["ET0"] = (p1+p2)/p3

        return self.cd["ET0"]


if __name__=="__main__":

    link = "http://api.openweathermap.org/data/2.5/weather"

    params = {

        "q":"Oran",
        "appid":"be196491245269d974798fae42fe1c94",
        "units":"metric",

    }

    response = rq.get(link,params)

    if response.status_code == 200:
        data = response.json()
        tmean= data["main"]["temp"]
        tmin=data["main"]["temp_min"]
        tmax=data["main"]["temp_max"]
        hmin=data["main"]["humidity"]
        hmax=data["main"]["humidity"]
        lat=data["coord"]['lat']
        lon=data["coord"]['lon']
        alt=2
        ws=data["wind"]["speed"]
        ap=data["main"]["pressure"]
        cld= data["clouds"]["all"]
        print(tmin,tmax,tmean,hmin,hmax,lat,lon,alt,cld,ap,ws)
        et = ETO(tmin = tmin,tmax = tmax,tmean = tmean,hmin = hmin,hmax = hmax,lat = lat,lon = lon,alt =alt,cloud = cld,pressure= ap,wind_speed =ws)
        print(et.calculation())
    else:
        print(response.status_code)

