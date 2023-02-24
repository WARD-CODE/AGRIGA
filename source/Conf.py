import paho.mqtt.client as mqtt
from pyowm import OWM

"""owm = OWM('cf43685e65aea50b553f48125f7b25e9')
mgr = owm.weather_manager()

broker = mqtt.Client("P1")
broker_adresse = "localhost"  # adresse du broker
"""
class Irrigation:
    StartTime = None  # l'heure du debut d'irrigation
    EndTime = None  # l'heure de fin d'irrigation
    LastIrrigationCounter = 0  # derniére irrigation
    LastIrrigationDate = None
    ETM = None
    Timer = None
   
    Mode_data_GG = {
            "distance_ligne":0,
            "espace_gouteur":0,
            "debit_eau":0
        }
    Mode_data_ASP = {
            "diam_gouteur":0,
            "ecart_gouteur":0,
            "distance_ligne":0,
            "pression":0
        }
    
    param_data_IRG = {
            "type":'<default>',
            "frequence":0,
            "heure":''}

    param_data_CUL = {
            "surface":0.0,
            "culture":{'type':'','element':''},
            "Kc":0.0}

    electrovanne_stat = ["desactive"]
    pompe_stat = ["desactive"]
    # Drip[0] : Debit gouteur, Drip[1] : distance gouteur, Drip [2] : distance ligne
    Sprinkler = [None, None, None, None]
    # Sprinkler[0] : Diametre de la buse, Sprinkler[1] : distance gouteur,
    # Sprinkler[2] : distance ligne, Sprinkler[3] : Pression a la buse


class Flags:
    EndIrrigation = 0
    Irrigationstat = 0