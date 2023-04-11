import pyeto as pt
import math as m
import datetime
import requests as rq



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
        
        # Slope of the saturation vapor pressure curve (kPa/°C)
        self.cd["delta"] = 4098 * (0.6108 * m.exp((17.27 * self.wd['Tmean']) / ( self.wd['Tmean'] + 237.3))) / (( self.wd['Tmean'] + 237.3) ** 2)#verified
        
        # Actual vapor pressure from from the minimum relative humidity
        self.cd["E0_tmin"] = 0.611 * m.exp((17.27 * self.wd['Tmin'])/(self.wd['Tmin'] + 237.3))
        self.cd["E0_tmax"] = 0.611 * m.exp((17.27 * self.wd['Tmax'])/(self.wd['Tmax'] + 237.3))

        self.cd["ea_min"] = self.wd['Hmin'] / 100 * self.cd["E0_tmax"]
        
        # Actual vapor pressure from from the maximum relative humidity
        self.cd["ea_max"] = self.wd['Hmax'] / 100 * self.cd["E0_tmin"]
        
        
        # Mean actual vapour pressure (kPa)
        self.cd["ea_mean"] = (self.cd["ea_min"] + self.cd["ea_max"])/2 #verified
        # Mean saturation vapour pressure (kPa) 
        self.cd["es_mean"] = (self.cd["E0_tmin"] + self.cd["E0_tmax"])/2 #verified

        # solar declination
        self.cd["sd"] = m.degrees(0.409 * m.sin(2*m.pi /365 * J - 1.39)) #verified
        

        # sunset hour angle
        self.cd["sh"] = m.acos(-m.tan(self.wd["lat"]) * m.tan(m.radians(self.cd["sd"])))#verified

        # Inverse relative distance Earth-Sun
        self.cd["inv_d"] = 1 + 0.033 * m.cos(2 * m.pi * J / 365) #verified

        # Extraterestrial radiation Ra
        # self.cd["Ra"] = (24 * 60 / m.pi) * Gsc * self.cd["inv_d"] * ((self.cd["sh"] * m.sin(self.wd["lat"]) \
        #     * m.sin(self.cd["sd"])) + (m.cos(self.wd["lat"]) * m.cos(self.cd["sd"]) * m.sin(self.cd["sh"])))#verified
        
        self.cd['Ra'] = pt.et_rad(self.wd['lat'],m.radians(self.cd['sd']),self.cd['sh'],self.cd['inv_d'])

        # clear –sky radiation Rs0
        self.cd["Rs0"] = (0.75 + 2*m.pow(10,-5)*self.wd["alt"])* self.cd["Ra"]

        # solar radiation
        self.cd["Rs"] = pt.sol_rad_from_t(self.cd['Ra'],self.cd["Rs0"],self.wd["Tmin"],self.wd["Tmax"],coastal=True)
        # self.cd["Rs"] = self.cd["Ra"] * (0.25 + 0.5 * (1 - self.wd["cloud"] / 100))

        # Net shortwave radiation
        self.cd["Rns"] = (1-albedo)*self.cd["Rs"]

        # Net longwave radiation
        p1 = sigma * ((self.wd["Tmax"] + 273.16) ** 4 + (self.wd["Tmin"] + 273.16) ** 4) / 2
        p2 = 0.34 - 0.14 *m.sqrt(self.cd["ea_mean"])
        p3 = 1.35 * (self.cd["Rs"]/self.cd["Rs0"]) - 0.35
        self.cd["Rnl"] =  p1*p2*p3 
        
        #  net radiation
        self.cd["Rn"] = self.cd["Rns"] + self.cd["Rnl"]  
        
        # Psychrometric constant (gamma)
        self.cd["gamma"] = 0.665e-3 *  self.wd["P"] / 10

        # 11-Evapotranspiration 
        p1 = 0.408 * self.cd["delta"]*(self.cd["Rn"] - G)
        p2 = self.cd["gamma"] * 900 * (self.cd["es_mean"] - self.cd["ea_mean"]) * self.wd["ws"] /(self.wd["Tmean"]+273)
        p3 = self.cd["delta"] + self.cd["gamma"]*(1 + 0.34*self.wd["ws"])

        # print(self.cd["Rn"],"\n", self.wd["Tmean"],"\n",self.cd["delta"],"\n",
        #       self.cd["ea_mean"],"\n",self.cd["es_mean"],"\n",self.cd["gamma"],"\n",self.wd["ws"])

        self.cd["ET0"] = (p1+p2)/p3

        return self.cd["ET0"]

class ETc:
    Kc = 0.0
    def __init__(self):
        pass

class Kc:
    def __init__():
        pass
        


if __name__=="__main__":

    link = "http://api.openweathermap.org/data/2.5/forecast"

    params = {

        "q":"Oran",
        "appid":"be196491245269d974798fae42fe1c94",
        "units":"metric",

    }

    response = rq.get(link,params)

    if response.status_code == 200:
        data = response.json()
        forcast = {}
        for day in range(5):
            date = (datetime.datetime.now() + datetime.timedelta(days=day)).strftime('%d-%m-%Y')
            forcast[date] = {'tmean':[],'tmin':[],'tmax':[],'hmin':[],'hmax':[],'lat':[],'lon':[],'alt':[],'ws':[],'ap':[],'cld':[]}
            for h in range(8):
                forcast[date]['tmean'].append(data["list"][8*day + h]["main"]["temp"])
                forcast[date]['tmin'].append(data["list"][8*day + h]["main"]["temp_min"])
                forcast[date]['tmax'].append(data["list"][8*day + h]["main"]["temp_max"])
                forcast[date]['hmin'].append(data["list"][8*day + h]["main"]["humidity"])
                forcast[date]['hmax'].append(data["list"][8*day + h]["main"]["humidity"])
                forcast[date]['lat'].append(data["city"]["coord"]['lat'])
                forcast[date]['lon'].append(data["city"]["coord"]['lon'])
                forcast[date]['alt'].append(2)
                forcast[date]['ws'].append(data["list"][8*day + h]["wind"]["speed"])
                forcast[date]['ap'].append(data["list"][8*day + h]["main"]["pressure"])
                forcast[date]['cld'].append(data["list"][8*day + h]["clouds"]["all"])
        
        for date in forcast:
            for param in ('tmean','tmin','tmax','hmin','hmax','lat','lon','alt','ws','ap','cld'):
                forcast[date][param] = sum(forcast[date][param])/8
                
        print(forcast['11-04-2023'])        
        
        et =  ETO(tmin = forcast['11-04-2023']['tmin'],
                  tmax = forcast['11-04-2023']['tmax'],
                  tmean = forcast['11-04-2023']['tmean'],
                  hmin = forcast['11-04-2023']['hmin'],
                  hmax = forcast['11-04-2023']['hmax'],
                  lat = forcast['11-04-2023']['lat'],
                  lon = forcast['11-04-2023']['lon'],
                  alt =forcast['11-04-2023']['alt'],
                  cloud = forcast['11-04-2023']['cld'],
                  pressure= forcast['11-04-2023']['ap'],
                  wind_speed =forcast['11-04-2023']['ws'])
        
        print(et.calculation())
    else:
        print(response.status_code)

