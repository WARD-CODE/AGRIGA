
import customtkinter as CTK
from PIL import Image
from tableframe import TableFrame
from Mesure_label import MesureLabel
from Evapotranspiration import ETc
from data_exchange import Irrigation
from tkinter import  messagebox as mbx

class Supervision:
    def __init__(self,master,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.menu_button = {}
        self.supervision_frame = {}

        self.mesures_labels = {}
        self.mesures_values = {}

        self.actionneurs_frame = {}

        self.actionneurs_electrovanne_labels = {}
        self.actionneurs_pompe_labels = {}

        self.evapotranspiration_frame = {}

        self.historique_frame = {}
        self.histo_button = {}


        
        self.init_components(master)
        self.disp_components()
        self.update_mesures()

    def init_components(self,master):

        button_list = ["Mesures", "Actionneurs", "Evapotranspiration", "Historique"]
        button_text = ["Mesures","Actionneurs","Evatranspiration","Historique"]
        button_icons = ["mesures.png","actionneurs.png","evapotranspiration.png","historique.png"]

        # the supervision overview components
        self.supervision_frame["buttons_frame"] = CTK.CTkFrame(master = master,
                                                                width = 270,
                                                                height = 110,
                                                                fg_color= "transparent",
                                                                corner_radius = 15
                                                                )

        self.supervision_frame["tabview_1"] = CTK.CTkTabview(master = master,
                                                        width = 380,
                                                        height = 330,
                                                        fg_color= "#1E1E1E",
                                                        text_color_disabled = "#424949",
                                                        segmented_button_fg_color = "#424949",
                                                        segmented_button_selected_color= "#424949",
                                                        segmented_button_selected_hover_color ="#424949",
                                                        segmented_button_unselected_color = "#424949",
                                                        segmented_button_unselected_hover_color="#424949",
                                                        corner_radius = 15,
                                                        state= "disabled"
                                                        )

        for button in button_list:
            self.supervision_frame["tabview_1"].add(button)
        else:
            self.supervision_frame["tabview_1"].add("     ")
        
        for button in range(0,4):
            self.menu_button[button_list[button]] = CTK.CTkButton(master = self.supervision_frame["buttons_frame"],
                                                    text=button_text[button],
                                                    width = 90,
                                                    height = 80,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#209617",
                                                    hover_color="#30CD4F",
                                                    compound="top",
                                                    image = CTK.CTkImage(Image.open("images/{}".format(button_icons[button])),size = (40,40)),
                                                    corner_radius = 15,
                                                    anchor = "center"
                                                    )

        self.menu_button["Mesures"].configure(command = self.push_mesures)
        self.menu_button["Actionneurs"].configure(command = self.push_actionneurs)
        self.menu_button["Evapotranspiration"].configure(command = self.push_evapotranspiration)
        self.menu_button["Historique"].configure(command = self.push_historique)

        #Mesures fields
        self.mesures_components()
        #actionneurs field
        self.actionneurs_components()
        #evapotranspiration field
        self.evapotranspiration_components()
        #historique field
        self.historique_components()
        
        
    def mesures_components(self):
        
        labels_list = ["Temperature", "Humidité","Pression_air","vitesse_vent","précipitation"] 
        labels_text = ["Temperature\n(C°)", "Humidité\n(%)","Pression d'air\n(P)","Vitesse du vent\n(m/s)","Précipitation\n(v)"]
        labels_icons = ["temperature.png", "Humidity.png","pression.png","wind.png","precipitation.png"]
        
        self.mesures_framescroll = CTK.CTkScrollableFrame(master = self.supervision_frame["tabview_1"].tab("Mesures"),
                                                        width = 410,
                                                        height = 330,
                                                        fg_color= "transparent",
                                                        corner_radius = 15)

        self.misures_title = CTK.CTkLabel(master = self.supervision_frame["tabview_1"].tab("Mesures"),
                                                    text="Supervision et prévision méteologique",
                                                    font = CTK.CTkFont(size = 20,weight = "bold"))

        for label in range(0,5):
            self.mesures_labels[labels_list[label]] = MesureLabel(master=self.mesures_framescroll,
                                                                        lab_text=labels_text[label],
                                                                        lab_image=labels_icons[label],
                                                                        width = 120,
                                                                        height = 120,
                                                                        fg_color= "transparent")
            

            
            
    def actionneurs_components(self):

        self.actionneurs_frame["scroller"] = CTK.CTkScrollableFrame(master = self.supervision_frame["tabview_1"].tab("Actionneurs"),
                                                width = 410,
                                                height = 330,
                                                fg_color= "transparent",
                                                corner_radius = 15)
        
        self.actionneurs_frame["creation"] = CTK.CTkFrame(master = self.actionneurs_frame["scroller"],
                                                width = 250,
                                                height = 50,
                                                fg_color= "transparent",
                                                corner_radius = 15)
        
        self.actionneurs_frame["actionneur"] = CTK.CTkFrame(master = self.actionneurs_frame["scroller"],
                                        width = 250,
                                        height = 100,
                                        fg_color= "transparent",
                                        corner_radius = 15)
        
        self.actionneurs_frame["pompe"] = CTK.CTkEntry(master = self.actionneurs_frame["creation"],
                                                        placeholder_text = "(n) pompes",
                                                        font = CTK.CTkFont(size = 12),
                                                        width = 100,
                                                        height = 35)

        self.actionneurs_frame["electrovanne"] = CTK.CTkEntry(master = self.actionneurs_frame["creation"],
                                                                placeholder_text = "(n) electrovannes",
                                                                font = CTK.CTkFont(size = 12),
                                                                width = 100,
                                                                height = 35)

                                                                
        self.actionneurs_frame["creer"] =  CTK.CTkButton(master = self.actionneurs_frame["creation"],
                                                    text="créer",
                                                    width = 90,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#184873",
                                                    hover_color="#295a87",
                                                    corner_radius = 15,
                                                    anchor = "center",
                                                    command = lambda: self.actionneurs_creator(self.actionneurs_frame["pompe"].get(),self.actionneurs_frame["electrovanne"].get())
                                                    )
        
    def evapotranspiration_components(self):

        self.evapotranspiration_frame["evapotranspiration"]=MesureLabel(master=self.supervision_frame["tabview_1"].tab("Evapotranspiration"),
                                                                        lab_text="Evapotranspiration\n(mm)",
                                                                        lab_image="evapotranspiration.png",
                                                                        width = 120,
                                                                        height = 120,
                                                                        fg_color= "transparent"
                                                                        )
        
        self.evapotranspiration_frame["latitude"] = CTK.CTkEntry(master=self.supervision_frame["tabview_1"].tab("Evapotranspiration"),
                                                        placeholder_text = "latitude(C°)",
                                                        font = CTK.CTkFont(size = 12),
                                                        width = 100,
                                                        height = 35)
        
        self.evapotranspiration_frame["longitude"] = CTK.CTkEntry(master=self.supervision_frame["tabview_1"].tab("Evapotranspiration"),
                                                                placeholder_text = "longitude(C°)",
                                                                font = CTK.CTkFont(size = 12),
                                                                width = 100,
                                                                height = 35)
        
        self.evapotranspiration_frame["obtenir"] = CTK.CTkButton(master=self.supervision_frame["tabview_1"].tab("Evapotranspiration"),
                                                                text="obtenir",
                                                                width = 90,
                                                                height = 30,
                                                                font = CTK.CTkFont(size = 12,weight = "bold"),
                                                                fg_color= "#184873",
                                                                hover_color="#295a87",
                                                                corner_radius = 15,
                                                                anchor = "center",
                                                                command = self.get_evapotranspiration
                                                                )
                    
    def historique_components(self):
        histo_list = ["parametres atmospheriques", "caracteristiques de la culture","Evapotranspiration d'eau"]
        self.historique_frame["frame"] = CTK.CTkFrame(master = self.supervision_frame["tabview_1"].tab("Historique"),
                                                        width = 400,
                                                        height = 200,
                                                        fg_color= "transparent",
                                                        corner_radius = 15)
        
        self.historique_frame["buttons_frame"] = CTK.CTkFrame(master = self.historique_frame["frame"] ,
                                                        width = 200,
                                                        height = 100,
                                                        fg_color= "transparent",
                                                        corner_radius = 15)
        
        self.historique_title=CTK.CTkLabel(master=self.supervision_frame["tabview_1"].tab("Historique"),
                                           text="Historique des données",
                                           font = CTK.CTkFont(size = 15,weight = "bold"))
        
        self.historique_image = CTK.CTkLabel(master = self.supervision_frame["tabview_1"].tab("Historique"),
                                        text="",
                                        width = 150,
                                        height = 150,
                                        fg_color= 'transparent',
                                        image = CTK.CTkImage(Image.open("images/histo.png"),size = (150,150)),
                                        corner_radius = 15,
                                        anchor = "center"
                                        )
        i=1
        for button in histo_list:
            self.histo_button[button] = CTK.CTkButton(master = self.historique_frame["buttons_frame"],
                                            text=button,
                                            width = 120,
                                            height = 40,
                                            font = CTK.CTkFont(size = 12,weight = "bold"),
                                            fg_color= "#184873",
                                            hover_color="#295a87",
                                            # image = CTK.CTkImage(Image.open("images/{}".format(button_icons[button])),size = (40,40)),
                                            corner_radius = 15,
                                            anchor = "center",
                                            command = lambda b=i:self.push_histoList(b)
                                            )
            i+=1
            

    def disp_components(self):

        #general frame
        self.supervision_frame["buttons_frame"].place(relx = 0, rely = 0.8)
        self.supervision_frame["tabview_1"].place(relx = 0.005,rely = 0.002)
       
        button_list = ["Mesures", "Actionneurs", "Evapotranspiration", "Historique"]
        i = 0
        for button in button_list:
            self.menu_button[button].grid(row = 0,column = i, padx =5,pady =5)
            i+=1

        #Mesures
        self.mesures_framescroll.place(relx = 0,rely =-.03)
        self.mesures_labels["Temperature"].grid(row = 1,column = 0, padx =5,pady =3)
        self.mesures_labels["Humidité"].grid(row = 1,column = 1, padx =5,pady =3)
        self.mesures_labels["Pression_air"].grid(row = 1,column = 2, padx =5,pady =2)
        self.mesures_labels["vitesse_vent"].grid(row = 2,column = 0, padx =5,pady =2)
        self.mesures_labels["précipitation"].grid(row = 2,column = 1, padx =5,pady =2)

        #Actionneurs
        self.actionneurs_frame["scroller"].place(relx = 0,rely =-.03)
        self.actionneurs_frame["creation"].pack()
        i=0
        for comp in ("pompe","electrovanne","creer"):
            self.actionneurs_frame[comp].grid(row = 0,column = i, padx = 5, pady = 5)
            i+=1
        self.actionneurs_frame["actionneur"].pack()

        # evapotranspiration
        
        self.evapotranspiration_frame["evapotranspiration"].place(relx = 0.1,rely =0.1)
        self.evapotranspiration_frame["latitude"].place(relx = 0.6,rely =0.1)
        self.evapotranspiration_frame["longitude"].place(relx = 0.6,rely =0.3)
        self.evapotranspiration_frame["obtenir"].place(relx = 0.6,rely =0.5)
        #historique
        self.historique_title.pack()
        self.historique_frame["frame"].pack()
        self.historique_frame["buttons_frame"].place(relx=.01,rely=.14)
        self.historique_image.place(relx=.6, rely=.26)
        self.histo_button["parametres atmospheriques"].grid(row=0,column=0,pady=7,sticky="nsew")
        self.histo_button["caracteristiques de la culture"].grid(row=1,column=0,pady=7,sticky="nsew")
        self.histo_button["Evapotranspiration d'eau"].grid(row=2,column=0, pady=7,sticky="nsew")
        
        
    # additional functions
    def actionneurs_creator(self,pompe,electrovanne):

        for k,v in self.actionneurs_pompe_labels.items():
            v.grid_forget()
        
        for k,v in self.actionneurs_electrovanne_labels.items():
            v.grid_forget()

        i,j = 0,0
        for pmp in range(int(pompe)):
            self.actionneurs_pompe_labels[pmp] = CTK.CTkLabel(master = self.actionneurs_frame["actionneur"],
                                            text="PMP {}".format(i),
                                            width = 90,
                                            height = 90,
                                            font = CTK.CTkFont(size = 12,weight = "bold"),
                                            fg_color= "gray",
                                            pady = 10,
                                            compound="top",
                                            image = CTK.CTkImage(Image.open("images/pompe.png"),size = (40,40)),
                                            corner_radius = 15,
                                            anchor = "center"
                                            )
            self.actionneurs_pompe_labels[pmp].grid(row =j,column = i,padx =3,pady =3)
            i+=1
            if i>3:
                i=0
                j+=1
            
        i, m=0, 1
        self.actionneurs_electrovanne_labels = {}
        for ev in range(int(electrovanne)):
            self.actionneurs_electrovanne_labels[ev] = CTK.CTkLabel(master = self.actionneurs_frame["actionneur"],
                                                                    text="EV {}".format(i),
                                                                    width = 90,
                                                                    height = 90,
                                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                                    fg_color= "gray",
                                                                    pady = 10,
                                                                    compound="top",
                                                                    image = CTK.CTkImage(Image.open("images/electrovanne.png"),size = (40,40)),
                                                                    corner_radius = 15,
                                                                    anchor = "center"
                                                                    )

            self.actionneurs_electrovanne_labels[ev].grid(row =j+m,column = i,padx =3,pady =3)
            i+=1
            if i>3:
                i=0
                m+=1
    
    def push_mesures(self):
        self.supervision_frame["tabview_1"].set("Mesures")
    
    def push_actionneurs(self):
        self.supervision_frame["tabview_1"].set("Actionneurs")

    def push_evapotranspiration(self):
        self.supervision_frame["tabview_1"].set("Evapotranspiration")

    def push_historique(self):
        self.supervision_frame["tabview_1"].set("Historique")
    
    def push_histoList(self,b):
        if b==1:
            return TableFrame("paramtres atmospheriques.csv")
        elif b==2:
            return TableFrame("caracteristiques culture.csv")
        elif b==3:
            return TableFrame("evapotranspiration.csv")

    

    def update_mesures(self):   
        labels_list = ["Temperature", "Humidité","Pression_air","vitesse_vent","précipitation"] 
        for label in labels_list:
            self.mesures_labels[label].update_value(Irrigation.sensors_data[label])
            
        self.mesures_framescroll.after(20000, self.update_mesures)


    def get_evapotranspiration(self):

        
        if Irrigation.param_data_CUL["Kc"] != 0.0:
            location = (float(self.evapotranspiration_frame["latitude"].get()),float(self.evapotranspiration_frame["longitude"].get()))
            etc = ETc(Kc=Irrigation.param_data_CUL["Kc"],
                    location=location,
                    url="http://api.openweathermap.org/data/2.5/forecast",
                    appid="be196491245269d974798fae42fe1c94",
                    units="metric")
            
            self.evapotranspiration_frame["evapotranspiration"].update_value(etc.etc_calculation())
        else:
            mbx.showwarning("valeur Kc","verfier la valeur du coefficient Kc")
