import customtkinter as CTK
from PIL import Image
from data_exchange import Irrigation

class Wifistat(CTK.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.wm_title("Wifi")

        self.header={}
        self.value = {}
        self.init_components()
        self.disp_components()
    
    def init_components(self):
        param_wifi = ["état","ssid","mot de passe","type de securité","débit","bande passante","signal"]

        self.wifi_title =CTK.CTkLabel(self,
                                      text="paramétres Wi-Fi",
                                      font=CTK.CTkFont(size=17,weight="bold"),
                                      fg_color="green",
                                      corner_radius=15,
                                      image=CTK.CTkImage(Image.open("images/wifi.png"),size = (20,20)),
                                      compound="right",
                                      padx=6
                                      )
        
        self.mainframe=CTK.CTkFrame(self,
                                    width=200,
                                    height=400,
                                    corner_radius=15
                                    )
        for param in param_wifi:
            self.header[param] = CTK.CTkLabel(self.mainframe, 
                                             text=param,
                                             font=CTK.CTkFont(size=12,weight="bold"),
                                             )
        for param in param_wifi:   
            self.value[param] = CTK.CTkLabel(self.mainframe, 
                                             text=Irrigation.wifi_data[param],
                                             font=CTK.CTkFont(size=12,weight="bold"),
                                             fg_color="#595959",
                                             corner_radius=10
                                             )
            
    def disp_components(self):
        param_wifi = ["état","ssid","mot de passe","type de securité","débit","bande passante","signal"]

        self.wifi_title.pack(pady=10)
        self.mainframe.pack(padx=10,pady=10)
        for i in range(7):
            self.header[param_wifi[i]].grid(row = i,column=0,padx=15,pady=5)

        for i in range(7):
            self.value[param_wifi[i]].grid(row = i,column=1,padx=9,pady=5)
    
    def Rasp_wifi_data(self):
        pass


class Mqttstat(CTK.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.Table = None
        self.init_components()
        self.disp_components()
    
    def init_components(self):
        pass
    def disp_components(self):    
        self.Table.show()