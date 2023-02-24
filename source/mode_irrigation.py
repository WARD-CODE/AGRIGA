

import customtkinter as CTK
from tkinter import messagebox
from constants import constants
from PIL import Image
from Conf import Irrigation

class Mode_irrigation:

    def __init__(self,master,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.menu_button = {}
        self.mode_irrigation_frame = {}
        self.drip_entries = {}
        self.drip_buttons = {}
        self.aspersion_entries = {}
        self.aspersion_buttons = {}
        self.Mode_entry_GG = []


        self.init_components(master)
        self.disp_components()

    def drip_component(self):
        #drip fields
        entries_list = ["distance_ligne", "espace_goutteur", "debit_eau"]
        entries_text = ["distance entre les lignes(Cm)", "Espace entre les goutteurs","débit d'eau(L/heure)"]

        self.drip_frame = CTK.CTkFrame(master = self.mode_irrigation_frame["tabview_1"].tab("drip"),
                                        width = 330,
                                        height = 330,
                                        fg_color= "transparent",
                                        corner_radius = 15)

        self.drip_title = CTK.CTkLabel(master = self.mode_irrigation_frame["tabview_1"].tab("drip"),
                                                    text="Table de configuration Mode Goutte à Goutte",
                                                    font = CTK.CTkFont(size = 18,weight = "bold"))

        for indx in range(0,3):
            
            self.drip_entries[entries_list[indx]] = CTK.CTkEntry(master = self.drip_frame,
                                                                placeholder_text = entries_text[indx],
                                                                font = CTK.CTkFont(size = 14),
                                                                width = 190,
                                                                height = 35)
            
            self.drip_buttons[entries_list[indx]] =  CTK.CTkButton(master = self.drip_frame,
                                                    text="appliquer",
                                                    width = 140,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#209617",
                                                    hover_color="#30CD4F",
                                                    corner_radius = 15,
                                                    anchor = "center"
                                                    )
            
        self.drip_buttons["appliquer tout"] = CTK.CTkButton(master = self.mode_irrigation_frame["tabview_1"].tab("drip"),
                                                    text="appliquer tout",
                                                    width = 180,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#209617",
                                                    hover_color="#30CD4F",
                                                    corner_radius = 15,
                                                    anchor = "center"
                                                    
                                                    )
    
    def aspersion_components(self):
        
        entries_list = ["diam_gouteur", "ecart_gouteur", "distance_ligne","pression"]
        entries_text = ["Diamètre du gouteur (mm)", "Ecart entre les asperseurs (cm)","Distance entre les lignes (cm)","Pression (bar)"]

        self.aspersion_frame = CTK.CTkFrame(master = self.mode_irrigation_frame["tabview_1"].tab("aspersion"),
                                        width = 340,
                                        height = 330,
                                        fg_color= "transparent",
                                        corner_radius = 15)

        self.aspersion_title = CTK.CTkLabel(master = self.mode_irrigation_frame["tabview_1"].tab("aspersion"),
                                                    text="Table de configuration Mode Aspersion",
                                                    font = CTK.CTkFont(size = 18,weight = "bold"))

        for indx in range(0,4):
            
            self.aspersion_entries[entries_list[indx]] = CTK.CTkEntry(master = self.aspersion_frame,
                                                                placeholder_text = entries_text[indx],
                                                                font = CTK.CTkFont(size = 14),
                                                                width =210,
                                                                height = 35)
            
            self.aspersion_buttons[entries_list[indx]] =  CTK.CTkButton(master = self.aspersion_frame,
                                                    text="appliquer",
                                                    width = 120,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#209617",
                                                    hover_color="#30CD4F",
                                                    corner_radius = 15,
                                                    anchor = "center"
                                                    )
            
        self.aspersion_buttons["appliquer tout"] = CTK.CTkButton(master = self.mode_irrigation_frame["tabview_1"].tab("aspersion"),
                                                    text="appliquer tout",
                                                    width = 180,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#209617",
                                                    hover_color="#30CD4F",
                                                    corner_radius = 15,
                                                    anchor = "center"
                                                    
                                                    )
    def init_components(self,master):

        button_list = ["drip","aspersion"]
        button_text = ["goutte à goutte",'aspersion']
        button_icons = ["drip.png","aspersion.png"]

        self.mode_irrigation_frame["buttons_frame"] = CTK.CTkFrame(master = master,
                                                                width = 270,
                                                                height = 110,
                                                                fg_color= "transparent",
                                                                corner_radius = 15
                                                                )
        
        self.mode_irrigation_frame["tabview_1"] = CTK.CTkTabview(master = master,
                                                                width = 460,
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

        for button in range(0,2):
            self.menu_button[button_list[button]] = CTK.CTkButton(master = self.mode_irrigation_frame["buttons_frame"],
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
            
        self.menu_button["drip"].configure(command =  self.push_drip)
        self.menu_button["aspersion"].configure(command =  self.push_aspersion)

        for button in button_list:
            self.mode_irrigation_frame["tabview_1"].add(button)
        else:
            self.mode_irrigation_frame["tabview_1"].add("     ")

        self.drip_component()
        self.aspersion_components()



    def disp_components(self):
        self.mode_irrigation_frame["buttons_frame"].place(relx = 0, rely = 0.8)
        self.mode_irrigation_frame["tabview_1"].place(relx = 0.005,rely = 0.002)

        button_list = ["drip", "aspersion"]
        i = 0
        for button in button_list:
            self.menu_button[button].grid(row = 0,column = i, padx =5,pady =5)
            i+=1

        self.drip_title.place(relx = 0.05,rely =0.05)
        self.drip_frame.place(relx = 0.1,rely =0.25)
        self.drip_buttons["appliquer tout"].place(relx = 0.28,rely =0.8)
        self.drip_entries["distance_ligne"].grid(row = 0, column = 0,padx = 4,pady = 4)
        self.drip_entries["espace_goutteur"].grid(row = 1, column = 0,padx = 4,pady = 4)
        self.drip_entries["debit_eau"].grid(row = 2, column = 0,padx = 4,pady = 4)
        self.drip_buttons["distance_ligne"].grid(row = 0, column = 1,padx = 4,pady = 4)
        self.drip_buttons["espace_goutteur"].grid(row = 1, column = 1,padx = 4,pady = 4)
        self.drip_buttons["debit_eau"].grid(row = 2, column = 1,padx = 4,pady = 4)


        self.aspersion_title.place(relx = 0.05,rely =0.05)
        self.aspersion_frame.place(relx = 0.1,rely =0.2)
        self.aspersion_entries["diam_gouteur"].grid(row = 0, column = 0,padx = 4,pady = 4)
        self.aspersion_entries["ecart_gouteur"].grid(row = 1, column = 0,padx = 4,pady = 4)
        self.aspersion_entries["distance_ligne"].grid(row = 2, column = 0,padx = 4,pady = 4)
        self.aspersion_entries["pression"].grid(row = 3, column = 0,padx = 4,pady = 4)
        self.aspersion_buttons["diam_gouteur"].grid(row = 0, column = 1,padx = 4,pady = 4)
        self.aspersion_buttons["ecart_gouteur"].grid(row = 1, column = 1,padx = 4,pady = 4)
        self.aspersion_buttons["distance_ligne"].grid(row = 2, column = 1,padx = 4,pady = 4)
        self.aspersion_buttons["pression"].grid(row = 3, column = 1,padx = 4,pady = 4)
        self.aspersion_buttons["appliquer tout"].place(relx = 0.28,rely =0.87)
        


    def push_drip(self):
        self.mode_irrigation_frame["tabview_1"].set("drip")

    def push_aspersion(self):
        self.mode_irrigation_frame["tabview_1"].set("aspersion")

    def appliquer_mode_GG1(self):
        for key in Irrigation.Mode_data_GG.keys():
           Irrigation.Mode_data_GG[key] = int(self.drip_entries[key].get())
        
        print(Irrigation.Mode_data_GG)