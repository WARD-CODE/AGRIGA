from http.client import OK
from tkinter import messagebox
import customtkinter as CTK
from PIL import Image
from Conf import Irrigation

class Mode_irrigation:

    def __init__(self,master,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # define all objects used for the Drip mode
        self.menu_button = {} 
        self.mode_irrigation_frame = {}
        self.drip_entries = {}
        self.drip_buttons = {}
        self.aspersion_entries = {}
        self.aspersion_buttons = {}
        self.Mode_entry_GG = []

        #initialize components of the irrigation mode
        self.init_components(master)
        # display components to the screen
        self.disp_components()

    def drip_component(self):
        
        entries_list = ["distance_ligne", "espace_gouteur", "debit_eau"]
        entries_text = ["distance entre les lignes(Cm)", "Espace entre les goutteurs (cm)","débit d'eau(L/heure)"]

        #the drip frame where we add its compoenents
        self.drip_frame = CTK.CTkFrame(master = self.mode_irrigation_frame["tabview_1"].tab("drip"),
                                        width = 330,
                                        height = 330,
                                        fg_color= "transparent",
                                        corner_radius = 15)
        # drip general title
        self.drip_title = CTK.CTkLabel(master = self.mode_irrigation_frame["tabview_1"].tab("drip"),
                                                    text="Table de configuration Mode Goutte à Goutte",
                                                    font = CTK.CTkFont(size = 18,weight = "bold"))
        
        # the drip confguration parametes entries (editfields) and application buttons
        for indx in range(0,3):          
            self.drip_entries[entries_list[indx]] = CTK.CTkEntry(master = self.drip_frame,
                                                                placeholder_text = entries_text[indx],
                                                                font = CTK.CTkFont(size =16),
                                                                width = 250,
                                                                height = 35,
                                                                justify="center"
                                                                )
            
            self.drip_buttons[entries_list[indx]] =  CTK.CTkButton(master = self.drip_frame,
                                                    text="",
                                                    width = 30,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#184873",
                                                    image=CTK.CTkImage(Image.open("images/appliquer.png"),size = (25,25)),
                                                    hover_color="#295a87",
                                                    corner_radius = 15,
                                                    anchor = "center",
                                                    command = lambda s=entries_list[indx]:self.appliquer_mode_GG(s)
                                                    )

        # this button allow a general apply   
        self.drip_buttons["appliquer tout"] = CTK.CTkButton(master = self.mode_irrigation_frame["tabview_1"].tab("drip"),
                                                    text="appliquer tout",
                                                    width = 180,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#184873",
                                                    hover_color="#295a87",
                                                    corner_radius = 15,
                                                    anchor = "center",
                                                    command = lambda:self.appliquer_mode_GG(all=True)
                                                    )
    
    def aspersion_components(self):
        """
        this section will define the components like the previous one 
        and there are no differences.
        
        """
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
                                                                font = CTK.CTkFont(size = 16),
                                                                width =250,
                                                                height = 35,
                                                                justify="center"
                                                                )
            
            self.aspersion_buttons[entries_list[indx]] =  CTK.CTkButton(master = self.aspersion_frame,
                                                    text="",
                                                    width = 30,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    image=CTK.CTkImage(Image.open("images/appliquer.png"),size = (25,25)),
                                                    fg_color= "#184873",
                                                    hover_color="#295a87",
                                                    corner_radius = 15,
                                                    anchor = "center",
                                                    command = lambda s=entries_list[indx]:self.appliquer_mode_ASP(s)
                                                    )
            
        self.aspersion_buttons["appliquer tout"] = CTK.CTkButton(master = self.mode_irrigation_frame["tabview_1"].tab("aspersion"),
                                                    text="appliquer tout",
                                                    width = 180,
                                                    height = 30,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#184873",
                                                    hover_color="#295a87",
                                                    corner_radius = 15,
                                                    anchor = "center",
                                                    command =lambda: self.appliquer_mode_ASP(all=True)
                                                    
                                                    )
    def init_components(self,master):
        """
        in this section we are creating the main frame of the irrigation mode 
        including the drip and aspersion modes sections

        """
        button_list = ["drip","aspersion"]
        button_text = ["goutte à goutte",'aspersion']
        button_icons = ["drip.png","aspersion.png"]

        # the green control buttons frame
        self.mode_irrigation_frame["buttons_frame"] = CTK.CTkFrame(master = master,
                                                                width = 270,
                                                                height = 110,
                                                                fg_color= "transparent",
                                                                corner_radius = 15
                                                                )
        # the main Table to switch between modes
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
        #two buttons represent the drip and aspersion modes
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
        # attachement of the buttons to the callbacks    
        self.menu_button["drip"].configure(command =  self.push_drip)
        self.menu_button["aspersion"].configure(command =  self.push_aspersion)

        # link the main table with buttons
        for button in button_list:
            self.mode_irrigation_frame["tabview_1"].add(button)
        else:
            self.mode_irrigation_frame["tabview_1"].add("     ")

        #adding the sections components to the main frame
        self.drip_component()
        self.aspersion_components()



    def disp_components(self):
        """
        in this section we are displaying all components 
        created before to the irrigation mode view
        
        """
        self.mode_irrigation_frame["buttons_frame"].place(relx = 0, rely = 0.8)
        self.mode_irrigation_frame["tabview_1"].place(relx = 0.005,rely = 0.002)

        button_list = ["drip", "aspersion"]
        i = 0
        for button in button_list:
            self.menu_button[button].grid(row = 0,column = i, padx =5,pady =5)
            i+=1

        self.drip_title.pack(pady = 20)
        self.drip_frame.pack(pady = 5)
        self.drip_buttons["appliquer tout"].pack(pady = 5)
        self.drip_entries["distance_ligne"].grid(row = 0, column = 0,padx = 4,pady = 4)
        self.drip_entries["espace_gouteur"].grid(row = 1, column = 0,padx = 4,pady = 4)
        self.drip_entries["debit_eau"].grid(row = 2, column = 0,padx = 4,pady = 4)
        self.drip_buttons["distance_ligne"].grid(row = 0, column = 1,padx = 4,pady = 4)
        self.drip_buttons["espace_gouteur"].grid(row = 1, column = 1,padx = 4,pady = 4)
        self.drip_buttons["debit_eau"].grid(row = 2, column = 1,padx = 4,pady = 4)


        self.aspersion_title.pack(pady = 10)
        self.aspersion_frame.pack(pady = 5)
        self.aspersion_entries["diam_gouteur"].grid(row = 0, column = 0,padx = 4,pady = 4)
        self.aspersion_entries["ecart_gouteur"].grid(row = 1, column = 0,padx = 4,pady = 4)
        self.aspersion_entries["distance_ligne"].grid(row = 2, column = 0,padx = 4,pady = 4)
        self.aspersion_entries["pression"].grid(row = 3, column = 0,padx = 4,pady = 4)
        self.aspersion_buttons["diam_gouteur"].grid(row = 0, column = 1,padx = 4,pady = 4)
        self.aspersion_buttons["ecart_gouteur"].grid(row = 1, column = 1,padx = 4,pady = 4)
        self.aspersion_buttons["distance_ligne"].grid(row = 2, column = 1,padx = 4,pady = 4)
        self.aspersion_buttons["pression"].grid(row = 3, column = 1,padx = 4,pady = 4)
        self.aspersion_buttons["appliquer tout"].pack(pady =0)
        

    # this callback to switch to the drip mode config
    def push_drip(self):
        self.mode_irrigation_frame["tabview_1"].set("drip")
    # this callback to switch to the aspersion mode config
    def push_aspersion(self):
        self.mode_irrigation_frame["tabview_1"].set("aspersion")

    """ 
    this callback to apply configuration to each field and to save 
    the data in the Irrigation.Mode_data_GG dictionary 

    """
    def appliquer_mode_GG(self, field_name="", all=False):
        if not all:
            if str(self.drip_entries[field_name].get()).isdigit():
                Irrigation.Mode_data_GG[field_name] = int(self.drip_entries[field_name].get())
            else:
                messagebox.showwarning("valeur incorrecte","entrer une valeur entiere")

        elif all:
            list_data = ["distance_ligne","espace_gouteur","debit_eau"]
            
            for data in list_data:
                if str(self.drip_entries[data].get()).isdigit():
                    Irrigation.Mode_data_GG[data] = float(self.drip_entries[data].get())
                else:
                    messagebox.showwarning("valeur incorrecte","assurer que les valeurs entrées sont correctes")
                    break
    """ 
    this callback to apply configuration to each field and to save 
    the data in the Irrigation.Mode_data_ASP dictionary 
    """

    def appliquer_mode_ASP(self, field_name="", all=False):
        if not all:
            if str(self.aspersion_entries[field_name].get()).isdigit():
                Irrigation.Mode_data_ASP[field_name] = float(self.aspersion_entries[field_name].get())
            else:
                messagebox.showwarning("valeur incorrecte","entrer une valeur entiere")

        elif all:
            list_data = ["diam_gouteur","ecart_gouteur","distance_ligne","pression"]
            
            for data in list_data:
                if str(self.aspersion_entries[data].get()).isdigit():
                    Irrigation.Mode_data_ASP[data] = float(self.aspersion_entries[data].get())
                else:
                    messagebox.showwarning("valeur incorrecte","assurer que les valeurs entrées sont correctes")
                    break



        