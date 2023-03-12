
import customtkinter as CTK
from PIL import Image
from tkinter import Variable, messagebox
from Conf import Irrigation
from DateTime import Vcalender
from DateTime import Vclock
import re
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
        
        entries_list = ["type", "frequence", "heure"]
        entries_text = ["mode d'irrigation", "frequence d'irrigation (n)","hh:mm-[format]"]

        self.irrigation_frame = CTK.CTkFrame(master = self.param_irrigation_frame["tabview_1"].tab("irrigation"),
                                        width = 330,
                                        height = 330,
                                        fg_color= "transparent",
                                        corner_radius = 15)

        self.irrigation_title = CTK.CTkLabel(master = self.param_irrigation_frame["tabview_1"].tab("irrigation"),
                                                    text="Table de configuration des parametres d'irrigation",
                                                    font = CTK.CTkFont(size = 15,weight = "bold"))



        self.irrigation_entries["type"] = CTK.CTkComboBox(master = self.irrigation_frame,
                                                            width=185,
                                                            height=30,
                                                            corner_radius=13,
                                                            values=["goutte à goutte", "aspersion"],   
                                                            font = CTK.CTkFont(size = 17)

                                                           )
        
        self.irrigation_entries["frequence"] = CTK.CTkEntry(master = self.irrigation_frame,
                                                                placeholder_text = entries_text[1],
                                                                font = CTK.CTkFont(size = 15),
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
        
        self.irrigation_entries["heure"] = CTK.CTkEntry(master = self.irrigation_frame,
                                                                placeholder_text = entries_text[2],
                                                                font = CTK.CTkFont(size = 17),
                                                                width = 140,
                                                                height = 35
                                                                )
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
                                                                            anchor = "center",
                                                                            command=lambda s=entries_list[i]:self.appliquer_param_IRG(s)
                                                                            )
            
        self.irrigation_buttons["appliquer tout"] = CTK.CTkButton(master = self.param_irrigation_frame["tabview_1"].tab("irrigation"),
                                                    text="appliquer tout",
                                                    width = 180,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#184873",
                                                    hover_color="#295a87",
                                                    corner_radius = 15,
                                                    anchor = "center",
                                                    command=lambda :self.appliquer_param_IRG(all=True)
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
                                                        font = CTK.CTkFont(size = 17),
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
                                                        font = CTK.CTkFont(size = 17),
                                                        width =120,
                                                        height = 35)

        self.culture_entries["Kc"] = CTK.CTkEntry(master = self.culture_frame,
                                                placeholder_text = "valeur Kc",
                                                font = CTK.CTkFont(size = 17),
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
                                                    anchor = "center",
                                                    command=lambda s=button:self.appliquer_param_CUL(s)
                                                    )   
        self.culture_buttons["appliquer tout"] = CTK.CTkButton(master = self.param_irrigation_frame["tabview_1"].tab("culture"),
                                                    text="appliquer tout",
                                                    width = 180,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#184873",
                                                    hover_color="#295a87",
                                                    corner_radius = 15,
                                                    anchor = "center",
                                                    command=lambda:self.appliquer_param_CUL(all=True)
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
        self.irrigation_entries["type"].grid(row = 0, column = 0,padx = 4,pady = 4)
        self.irrigation_entries["frequence"].grid(row = 1, column = 0,padx = 4,pady = 4)
        self.irrigation_entries["heure"].place(relx = 0.2,rely =0.7)
        self.irrigation_buttons["clock"].place(relx = 0.01,rely =0.7)
        self.irrigation_buttons["type"].grid(row = 0, column = 1,padx = 4,pady = 4)
        self.irrigation_buttons["frequence"].grid(row = 1, column = 1,padx = 4,pady = 4)
        self.irrigation_buttons["heure"].grid(row = 2, column = 1,padx = 4,pady = 4)
 
        
        self.culture_title.place(relx = 0.06,rely =0.05)
        self.culture_frame.place(relx = 0.03,rely =0.2)
        self.culture_entries["surface"].grid(row = 0, column = 0,padx = 4,pady = 4)
        self.culture_entries["culture"].grid(row = 1, column = 0,padx = 4,pady = 4)
        self.culture_entries["element"].grid(row = 1, column = 1,padx = 4,pady = 4)
        self.culture_buttons["Kc_saison"].place(relx = 0.01,rely =0.7)
        self.culture_entries["Kc_saison"].place(relx = 0.115,rely =0.69)
        self.culture_entries["Kc"].grid(row = 2, column = 1,padx = 4,pady = 4)
        self.culture_buttons["surface"].grid(row = 0, column = 2,padx = 4,pady = 4)
        self.culture_buttons["culture"].grid(row = 1, column = 2,padx = 4,pady = 4)
        self.culture_buttons["Kc"].grid(row = 2, column = 2,padx = 4,pady = 4)
        self.culture_buttons["appliquer tout"].place(relx = 0.28,rely =0.87)


    def push_irrigation(self):
        self.param_irrigation_frame["tabview_1"].set("irrigation")

    def push_culture(self):
        self.param_irrigation_frame["tabview_1"].set("culture")
    
    def push_date(self):
        return Vcalender(self.culture_entries["Kc_saison"])
    
    def push_hour(self):
        return Vclock(self.irrigation_entries["heure"])

    def appliquer_param_IRG(self, field_name='', all=False):
        re_hour= r'^\d{1,2}:\d{2}-([AP]M)$'
        if not all:
            if field_name == "type":
                    Irrigation.param_data_IRG[field_name] = str(self.irrigation_entries[field_name].get())

            elif  field_name == "frequence":   
                if str(self.irrigation_entries[field_name].get()).isdigit():
                    Irrigation.param_data_IRG[field_name] = int(self.irrigation_entries[field_name].get())
                else:
                    messagebox.showwarning("valeur incorrecte","la valeur du champ doit etre entiere")

            elif field_name == "heure":       
                if re.match(re_hour,str(self.irrigation_entries[field_name].get())):
                    Irrigation.param_data_IRG[field_name] = str(self.irrigation_entries[field_name].get())
                else:
                    messagebox.showwarning("valeur incorrecte","la valeur du champ doit etre sous la forme hh:mm")

        elif all:
                checker = 1
                Irrigation.param_data_IRG["type"] = str(self.irrigation_entries["type"].get())

                if str(self.irrigation_entries["frequence"].get()).isdigit():
                    Irrigation.param_data_IRG["frequence"] = int(self.irrigation_entries["frequence"].get())
                    checker+=1
                if re.match(re_hour,str(self.irrigation_entries["heure"].get())):
                    Irrigation.param_data_IRG["heure"] = str(self.irrigation_entries["heure"].get())
                    checker+=1
                if checker == 3:
                    messagebox.showinfo("validation", "données enregistrés et validé!")
                else:
                    messagebox.showwarning("valeurs incorrectes","assurer que les valeurs des entrées sont correctes")
    

    def appliquer_param_CUL(self, field_name="", all=False):
        
        re_date = r'^\d{2}/\d{2}/\d{4}$'
        re_surf = r'^\d{2}.\d{2-5}$'

        if not all:
            if field_name == "culture":
                Irrigation.param_data_CUL[field_name]["culture"] = str(self.culture_entries["culture"].get())
                Irrigation.param_data_CUL[field_name]["element"] = str(self.culture_entries["element"].get())

            elif  field_name == "surface":   
                if re.match(re_surf,str(self.culture_entries["surface"].get())):
                    Irrigation.param_data_CUL[field_name] = float(self.culture_entries[field_name].get())
                else:
                    messagebox.showwarning("valeur incorrecte","la valeur du champ doit etre réelle (nn.ff)")

            elif field_name == "Kc":       
                if re.match(re_date,str(self.irrigation_entries["Kc_saison"].get())):
                    self.auto_Kc(self.irrigation_entries["Kc_saison"].get())
                    Irrigation.param_data_CUL[field_name] = str(self.irrigation_entries[field_name].get())
                else:
                    messagebox.showwarning("valeur incorrecte","la valeur du champ doit etre sous la forme dd/mm/aaaa")

        elif all:
                checker = 1 # to check if all field are valid
                Irrigation.param_data_CUL["culture"]["culture"] = str(self.culture_entries["culture"].get())
                Irrigation.param_data_CUL["culture"]["element"] = str(self.culture_entries["element"].get())

                if re.match(re_surf,str(self.culture_entries["surface"].get())):
                    Irrigation.param_data_CUL["surface"] = float(self.culture_entries["surface"].get())
                    checker+=1
                
                if checker == 3:
                    messagebox.showwarning("validation", "données enregistrés et validé!")
                else:
                    messagebox.showwarning("valeurs incorrectes","assurer que les valeurs des entrées sont correctes")
    