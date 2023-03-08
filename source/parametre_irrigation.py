
import customtkinter as CTK
from PIL import Image
from Conf import Irrigation
from DateTime import Vcalender
from DateTime import Vclock

class parametre_irrigation:

    def __init__(self,master,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # define all objects used for the irrigation parameters
        self.menu_button = {}
        self.param_irrigation_frame = {}
        self.irrigation_entries = {}
        self.irrigation_buttons = {}
        self.culture_entries = {}
        self.culture_buttons = {}
        

        #initialize components of the irrigation parameters
        self.init_components(master)
        # display components to the screen
        self.disp_components()

    def irrigation_component(self):
        
        entries_list = ["mode_irrigation", "frequence_irrigation", "heure_irrigation"]
        entries_text = ["mode d'irrigation", "frequence d'irrigation (n)","hh:mm"]

        self.irrigation_frame = CTK.CTkFrame(master = self.param_irrigation_frame["tabview_1"].tab("irrigation"),
                                        width = 330,
                                        height = 330,
                                        fg_color= "transparent",
                                        corner_radius = 15)

        self.irrigation_title = CTK.CTkLabel(master = self.param_irrigation_frame["tabview_1"].tab("irrigation"),
                                                    text="Table de configuration des parametres d'irrigation",
                                                    font = CTK.CTkFont(size = 15,weight = "bold"))



        self.irrigation_entries["mode_irrigation"] = CTK.CTkComboBox(master = self.irrigation_frame,
                                                            width=185,
                                                            height=30,
                                                            corner_radius=13,
                                                            values=["goutte à goutte", "aspersion"],   
                                                            font = CTK.CTkFont(size = 14)

                                                           )
        
        self.irrigation_entries["frequence_irrigation"] = CTK.CTkEntry(master = self.irrigation_frame,
                                                                placeholder_text = entries_text[1],
                                                                font = CTK.CTkFont(size = 14),
                                                                width = 190,
                                                                height = 35)
        
        self.irrigation_buttons["clock"] = CTK.CTkButton(master = self.irrigation_frame,
                                                                            text="",
                                                                            width = 10,
                                                                            height = 15,
                                                                            
                                                                            fg_color= "#184873",
                                                                            hover_color="#295a87",
                                                                            image = CTK.CTkImage(Image.open("images/clock.png"),size = (25,25)),
                                                                            corner_radius = 15,
                                                                            anchor = "center",
                                                                            command=self.push_hour)
        
        self.irrigation_entries["heure_irrigation"] = CTK.CTkEntry(master = self.irrigation_frame,
                                                                placeholder_text = entries_text[2],
                                                                font = CTK.CTkFont(size = 14),
                                                                width = 140,
                                                                height = 35)
        for i in range(3):
            self.irrigation_buttons[entries_list[i]] =  CTK.CTkButton(master = self.irrigation_frame,
                                                                            text="",
                                                                            width = 30,
                                                                            height = 30,
                                                                            font = CTK.CTkFont(size = 12,weight = "bold"),
                                                                            fg_color= "#184873",
                                                                            hover_color="#295a87",
                                                                            image = CTK.CTkImage(Image.open("images/appliquer.png"),size = (25,25)),
                                                                            corner_radius = 15,
                                                                            anchor = "center"
                                                                            )
            
        self.irrigation_buttons["appliquer tout"] = CTK.CTkButton(master = self.param_irrigation_frame["tabview_1"].tab("irrigation"),
                                                    text="appliquer tout",
                                                    width = 180,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#184873",
                                                    hover_color="#295a87",
                                                    corner_radius = 15,
                                                    anchor = "center"
                                                    
                                                    )
    
    def culture_components(self): 
        buttons_list = ["surface","culture", "Kc"]
        
        self.culture_frame = CTK.CTkFrame(master = self.param_irrigation_frame["tabview_1"].tab("culture"),
                                        width = 340,
                                        height = 330,
                                        fg_color= "transparent",
                                        corner_radius = 15)

        self.culture_title = CTK.CTkLabel(master = self.param_irrigation_frame["tabview_1"].tab("culture"),
                                                    text="Table de configuration des parametres de culture",
                                                    font = CTK.CTkFont(size = 15,weight = "bold"))

            
        self.culture_entries["surface"] = CTK.CTkEntry(master = self.culture_frame,
                                                        placeholder_text = "surface",
                                                        font = CTK.CTkFont(size = 14),
                                                        width =170,
                                                        height = 35)
        
        self.culture_entries["culture"] =  CTK.CTkComboBox(master = self.culture_frame,
                                                            width=170,
                                                            height=30,
                                                            corner_radius=13,
                                                            values=["empty"],   
                                                            font = CTK.CTkFont(size = 14)
                                                            )
        
        self.culture_entries["element"] =  CTK.CTkComboBox(master = self.culture_frame,
                                                            width=160,
                                                            height=30,
                                                            corner_radius=13,
                                                            values=["empty"],   
                                                            font = CTK.CTkFont(size = 14)
                                                            )
        self.culture_buttons["Kc_saison"] = CTK.CTkButton(master=self.culture_frame,
                                                          text="",
                                                          width=15,
                                                          height=30,
                                                          image = CTK.CTkImage(Image.open("images/calendar.png"),size = (20,20)),
                                                          command = self.push_date
                                                          )
        self.culture_entries["Kc_saison"] = CTK.CTkEntry(master = self.culture_frame,
                                                        placeholder_text = "(jj/mm/aaaa)",
                                                        font = CTK.CTkFont(size = 14),
                                                        width =120,
                                                        height = 35)

        self.culture_entries["Kc_value"] = CTK.CTkEntry(master = self.culture_frame,
                                                placeholder_text = "valeur Kc",
                                                font = CTK.CTkFont(size = 14),
                                                width =160,
                                                height = 35
                                                )
        
        for button in buttons_list:
            self.culture_buttons[button] =  CTK.CTkButton(master = self.culture_frame,
                                                    text="",
                                                    width = 30,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#184873",
                                                    hover_color="#295a87",
                                                    image = CTK.CTkImage(Image.open("images/appliquer.png"),size = (25,25)),
                                                    corner_radius = 15,
                                                    anchor = "center"
                                                    )   
            
        self.culture_buttons["appliquer tout"] = CTK.CTkButton(master = self.param_irrigation_frame["tabview_1"].tab("culture"),
                                                    text="appliquer tout",
                                                    width = 180,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#184873",
                                                    hover_color="#295a87",
                                                    corner_radius = 15,
                                                    anchor = "center"    
                                                 )
                                                 
    def init_components(self,master):

        button_list = ["irrigation","culture"]
        button_text = ["irrigation","culture"]
        button_icons = ["irrigation.png","culture.png"]

        self.param_irrigation_frame["buttons_frame"] = CTK.CTkFrame(master = master,
                                                                width = 270,
                                                                height = 110,
                                                                fg_color= "transparent",
                                                                corner_radius = 15
                                                                )
        
        self.param_irrigation_frame["tabview_1"] = CTK.CTkTabview(master = master,
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
            self.menu_button[button_list[button]] = CTK.CTkButton(master = self.param_irrigation_frame["buttons_frame"],
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
            
        self.menu_button["irrigation"].configure(command =  self.push_irrigation)
        self.menu_button["culture"].configure(command =  self.push_culture)

        for button in button_list:
            self.param_irrigation_frame["tabview_1"].add(button)
        else:
            self.param_irrigation_frame["tabview_1"].add("     ")

        self.irrigation_component()
        self.culture_components()



    def disp_components(self):
        self.param_irrigation_frame["buttons_frame"].place(relx = 0, rely = 0.8)
        self.param_irrigation_frame["tabview_1"].place(relx = 0.005,rely = 0.002)

        button_list = ["irrigation", "culture"]
        i = 0
        for button in button_list:
            self.menu_button[button].grid(row = 0,column = i, padx =5,pady =5)
            i+=1
        
        self.irrigation_title.place(relx = 0.04,rely =0.05)
        self.irrigation_frame.place(relx = 0.17,rely =0.25)
        
        self.irrigation_buttons["appliquer tout"].place(relx = 0.28,rely =0.8)
        self.irrigation_entries["mode_irrigation"].grid(row = 0, column = 0,padx = 4,pady = 4)
        self.irrigation_entries["frequence_irrigation"].grid(row = 1, column = 0,padx = 4,pady = 4)
        self.irrigation_entries["heure_irrigation"].place(relx = 0.2,rely =0.7)
        self.irrigation_buttons["clock"].place(relx = 0.01,rely =0.7)
        self.irrigation_buttons["mode_irrigation"].grid(row = 0, column = 1,padx = 4,pady = 4)
        self.irrigation_buttons["frequence_irrigation"].grid(row = 1, column = 1,padx = 4,pady = 4)
        self.irrigation_buttons["heure_irrigation"].grid(row = 2, column = 1,padx = 4,pady = 4)
 
        
        self.culture_title.place(relx = 0.06,rely =0.05)
        self.culture_frame.place(relx = 0.03,rely =0.2)
        self.culture_entries["surface"].grid(row = 0, column = 0,padx = 4,pady = 4)
        self.culture_entries["culture"].grid(row = 1, column = 0,padx = 4,pady = 4)
        self.culture_entries["element"].grid(row = 1, column = 1,padx = 4,pady = 4)
        self.culture_buttons["Kc_saison"].place(relx = 0.01,rely =0.7)
        self.culture_entries["Kc_saison"].place(relx = 0.115,rely =0.69)
        self.culture_entries["Kc_value"].grid(row = 2, column = 1,padx = 4,pady = 4)
        self.culture_buttons["surface"].grid(row = 0, column = 2,padx = 4,pady = 4)
        self.culture_buttons["culture"].grid(row = 1, column = 2,padx = 4,pady = 4)
        self.culture_buttons["Kc"].grid(row = 2, column = 2,padx = 4,pady = 4)
        self.culture_buttons["appliquer tout"].place(relx = 0.28,rely =0.87)


    def push_irrigation(self):
        self.param_irrigation_frame["tabview_1"].set("irrigation")

    def push_culture(self):
        self.param_irrigation_frame["tabview_1"].set("culture")

    def appliquer_mode_GG1(self):
        for key in Irrigation.Mode_data_GG.keys():
           Irrigation.Mode_data_GG[key] = int(self.irrigation_entries[key].get())
        
        print(Irrigation.Mode_data_GG)
    
    def push_date(self):
        return Vcalender()
    
    def push_hour(self):
        return Vclock()