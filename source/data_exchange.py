
"""
this file is our main data exchanger
its a commun file between the Backend and IHM 
it contains:
--> the irrigation modes data
    -->Drip mode data
    -->Aspersion mode data

--> the irrigation parameters data
    -->Irrigation data
    -->culture data

--> the actuators & sensors states

--> 
"""
class Irrigation:
   
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
            "culture":{'culture':'','element':''},
            "Kc":0.0}

    electrovanne_stat = ["desactive"]
    pompe_stat = ["desactive"]

    wifi_data = {
        "état":"connecté",
        "ssid":"safitechOrg",
        "mot de passe":"hcetifas",
        "type de securité":"WPA-2",
        "débit":"100kb/s",
        "bande passante":"2.4GHz",
        "signal":"-65dBm"
    }

