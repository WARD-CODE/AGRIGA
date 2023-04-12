import pyeto as pt
import math as m
import datetime
import requests as rq

"""
Evapotranspiration process

classes & objects:
-----------------
<singleton>
ET0 : Evapotranspiration of reference
ETc : Crop Evapotranspiration under standard conditions
Kc : Crop coefficient

constants
---------
sigma - Stefan-Boltzmann constant (4.903 x 10-9 MJ K-4 m-2 day-1)
albedo - Albedo 0.23 
Gsc - solar constant (0.082 MJ m-2 min-1)
_________________________________________________________________
data & parameters:
-----------------
wd : weather data
-->hmax - daily maximum air relative humidity (%)
-->hmean - daily minimum air relative humidity (%)
-->tmax - daily maximum air temperature (oC)
-->tmean - daily mean air temperature (oC)
-->tmin - daily minimum air temperature (oC)
-->ws - daily wind speed measured at h m above the ground (m s-1)
-->lat -latitude of the location (rad)
-->lon -longitude of the location (rad)
-->alt -elevation above sea level at the location (m)
-->ap - atmospheric pressure (kPa)
_______________________________________________________________
cd : calculated data
-->delta -daily slope of the vapor pressure curve (kPa oC-1)
-->E0_tmin daily saturation vapor pressure at the mean daily minimum air temperature (kPa)
-->E0_tmax daily saturation vapour pressure at the mean daily maximum air temperature (kPa)
-->ea_min  daily mean actual vapour pressure (kPa) [used as ea when RH max and RH min are available and reliable]
-->ea_max  daily mean actual vapour pressure (kPa) [used as ea when RH max and RH min are available and reliable]
-->ea_mean daily mean actual vapour pressure (kPa)
-->es_mean daily mean vapour pressure of the air at saturation (kPa)
-->sd  daily solar declination (rad)
-->sh daily sunset hour angle (rad)
-->inv_d daily inverse relative distance Earth-Sun
-->Ra daily extraterrestrial radiation (MJ m-2 day-1)
-->Rs0 daily clear sky solar radiation (MJ m-2 day-1)
-->Rs daily incoming measured radiation  (MJ m-2 day-1)
-->Rns daily net solar or shortwave radiation (MJ m-2 day-1)
-->Rnl daily net outgoing longwave radiation (MJ m-2 day-1)
-->Rn net radiation (MJ m-2 day-1)
-->gamma  psychrometric constant (kPa oC-1)

api_param: api parameters

--------------------------------------------------------------------

"""


class ETO:

    __instance = None

    def __new__(cls,*args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self,**kwargs):
        self.wd = {}
        self.cd = {}
        self.api_param = {}
        self.init_api(**kwargs)

        
    def init_api(self,**kwargs):
        # initialization and call of the API
        self.api_param["lat"] = kwargs["location"][0]
        self.api_param["lon"] = kwargs["location"][1]
        self.api_param["appid"] = kwargs["appid"]
        self.api_param["units"] = kwargs["units"]
        self.api_param["url"] = kwargs["url"]

        config_param = {key: self.api_param[key] for key in self.api_param if key != 'url'}
        self.response = rq.get(self.api_param["url"],config_param)

        

    def calculation(self,date):
        # constants
        sigma = 4.904e-9 #s Stefan-Boltzmann constant MJ K-4 m-2 day-1
        albedo = 0.23
        Gsc = 0.0820 
        J = datetime.datetime.strptime(date, '%d-%m-%Y').timetuple().tm_yday
        G = 0.0
        self.wd[date]["lat"] = m.radians( self.wd[date]["lat"] )
        self.wd[date]["lon"] = m.radians( self.wd[date]["lon"] )
        
        # Slope of the saturation vapor pressure curve (kPa/°C)
        self.cd["delta"] = 4098 * (0.6108 * m.exp((17.27 * self.wd[date]['tmean']) / ( self.wd[date]['tmean'] + 237.3))) / (( self.wd[date]['tmean'] + 237.3) ** 2)#verified
        
        # Actual vapor pressure from from the minimum relative humidity
        self.cd["E0_tmin"] = 0.611 * m.exp((17.27 * self.wd[date]['tmin'])/(self.wd[date]['tmin'] + 237.3))
        self.cd["E0_tmax"] = 0.611 * m.exp((17.27 * self.wd[date]['tmax'])/(self.wd[date]['tmax'] + 237.3))

        self.cd["ea_min"] = self.wd[date]['hmin'] / 100 * self.cd["E0_tmax"]
        
        # Actual vapor pressure from from the maximum relative humidity
        self.cd["ea_max"] = self.wd[date]['hmax'] / 100 * self.cd["E0_tmin"]
        
        
        # Mean actual vapour pressure (kPa)
        self.cd["ea_mean"] = (self.cd["ea_min"] + self.cd["ea_max"])/2 #verified
        # Mean saturation vapour pressure (kPa) 
        self.cd["es_mean"] = (self.cd["E0_tmin"] + self.cd["E0_tmax"])/2 #verified

        # solar declination
        self.cd["sd"] = m.degrees(0.409 * m.sin(2*m.pi /365 * J - 1.39)) #verified
        

        # sunset hour angle
        self.cd["sh"] = m.acos(-m.tan(self.wd[date]["lat"]) * m.tan(m.radians(self.cd["sd"])))#verified

        # Inverse relative distance Earth-Sun
        self.cd["inv_d"] = 1 + 0.033 * m.cos(2 * m.pi * J / 365) #verified

        # Extraterestrial radiation Ra
        # self.cd["Ra"] = (24 * 60 / m.pi) * Gsc * self.cd["inv_d"] * ((self.cd["sh"] * m.sin(self.wd[date]["lat"]) \
        #     * m.sin(self.cd["sd"])) + (m.cos(self.wd[date]["lat"]) * m.cos(self.cd["sd"]) * m.sin(self.cd["sh"])))#verified
        
        self.cd['Ra'] = pt.et_rad(self.wd[date]['lat'],m.radians(self.cd['sd']),self.cd['sh'],self.cd['inv_d'])

        # clear –sky radiation Rs0
        self.cd["Rs0"] = (0.75 + 2*m.pow(10,-5)*self.wd[date]["alt"])* self.cd["Ra"]

        # solar radiation
        self.cd["Rs"] = pt.sol_rad_from_t(self.cd['Ra'],self.cd["Rs0"],self.wd[date]["tmin"],self.wd[date]["tmax"],coastal=True)
        # self.cd["Rs"] = self.cd["Ra"] * (0.25 + 0.5 * (1 - self.wd[date]["cloud"] / 100))

        # Net shortwave radiation
        self.cd["Rns"] = (1-albedo)*self.cd["Rs"]

        # Net longwave radiation
        p1 = sigma * ((self.wd[date]["tmax"] + 273.16) ** 4 + (self.wd[date]["tmin"] + 273.16) ** 4) / 2
        p2 = 0.34 - 0.14 *m.sqrt(self.cd["ea_mean"])
        p3 = 1.35 * (self.cd["Rs"]/self.cd["Rs0"]) - 0.35
        self.cd["Rnl"] =  p1*p2*p3 
        
        #  net radiation
        self.cd["Rn"] = self.cd["Rns"] + self.cd["Rnl"]  
        
        # Psychrometric constant (gamma)
        self.cd["gamma"] = 0.665e-3 *  self.wd[date]["ap"] / 10

        # Evapotranspiration 
        p1 = 0.408 * self.cd["delta"]*(self.cd["Rn"] - G)
        p2 = self.cd["gamma"] * 900 * (self.cd["es_mean"] - self.cd["ea_mean"]) * self.wd[date]["ws"] /(self.wd[date]["tmean"]+273)
        p3 = self.cd["delta"] + self.cd["gamma"]*(1 + 0.34*self.wd[date]["ws"])

        # print(self.cd["Rn"],"\n", self.wd[date]["tmean"],"\n",self.cd["delta"],"\n",
        #       self.cd["ea_mean"],"\n",self.cd["es_mean"],"\n",self.cd["gamma"],"\n",self.wd[date]["ws"])

        ET_0 = (p1+p2)/p3
        return float(ET_0)

    def calculate(self):

        if self.response.status_code == 200:
            data = self.response.json()
            # extract data for 5 days
            for day in range(5):
                date = (datetime.datetime.now() + datetime.timedelta(days=day)).strftime('%d-%m-%Y')
                self.wd[date] = {'tmean':[],'tmin':[],'tmax':[],'hmin':[],'hmax':[],
                                'lat':[],'lon':[],'alt':[],'ws':[],'ap':[]}
                
                # 3h retrieving data for one day (3 x 8 = 24h) 
                for h in range(8):
                    self.wd[date]['tmean'].append(data["list"][8*day + h]["main"]["temp"])
                    self.wd[date]['tmin'].append(data["list"][8*day + h]["main"]["temp_min"])
                    self.wd[date]['tmax'].append(data["list"][8*day + h]["main"]["temp_max"])
                    self.wd[date]['hmin'].append(data["list"][8*day + h]["main"]["humidity"])
                    self.wd[date]['hmax'].append(data["list"][8*day + h]["main"]["humidity"])
                    self.wd[date]['lat'].append(data["city"]["coord"]['lat'])
                    self.wd[date]['lon'].append(data["city"]["coord"]['lon'])
                    self.wd[date]['alt'].append(2)
                    self.wd[date]['ws'].append(data["list"][8*day + h]["wind"]["speed"])
                    self.wd[date]['ap'].append(data["list"][8*day + h]["main"]["pressure"])
                    
            
            self.cd["ET0_days"] = []
            dates = []
            for date in self.wd:
                for param in ('tmean','tmin','tmax','hmin','hmax','lat','lon','alt','ws','ap'):
                    self.wd[date][param] = sum(self.wd[date][param])/8
                
                self.cd["ET0_days"].append(self.calculation(date))
                dates.append(date)

            return {"days":5,
                    "dates":dates,
                    "ET0_mean":sum(self.cd["ET0_days"])/5,
                    "ET0_days":self.cd["ET0_days"]
                    }
 
        else:
            print(self.response.status_code)


class ETc:
    Kc = 0.0
    def __init__(self):
        pass

class Kc:
    def __init__():
        pass

if __name__=="__main__":
    

    """
    testing phase
    """
    et = ETO(location=(35.652071,-0.5258542),
             url="http://api.openweathermap.org/data/2.5/forecast",
             appid="be196491245269d974798fae42fe1c94",
             units="metric")
    
    data = et.calculate()

    print("ET0 5 days mean:",data["ET0_mean"])
    print("ET0 for each day:")
    for k in range(5):
        print("{} : {}".format(data["dates"][k],data["ET0_days"][k]))
    

   
