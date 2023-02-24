import customtkinter as CTK
from PIL import Image
from tkinter import messagebox
from constants import constants 
from signIN import SignIN_W
from vkeyboard import VkeyBoard
from frame_screen import FrameScreen


CTK.set_appearance_mode(constants.wind_mode)


class App(CTK.CTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.principal_frame ={}
        self.menu_button = {}
        self.general_button = {}
        
        self.window_configuration()
        self.init_components()
        self.disp_components()
        #self.sign_in()

    
    def sign_in(self):
        self.toplevel_window = None
    
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = SignIN_W(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
    
    def init_components(self):
        button_list = ["home","supervision","mode_irrigation","parameter_irrigation"]
        button_text = ["Accueil","Supervision","Modes\nIrrigation","Parameters\nIrrigation"]
        button_icons = ["home.png","supervision.png","irrigation.png","culture.png"]

        gbutton_list = ["eteindre","redemarer","aide"]
        gbutton_icons = ["poweron.png","restart.png","help.png"]

        self.principal_frame["safitech"] = CTK.CTkFrame(master = self,
                                            width = 270,
                                            height = 100,
                                            fg_color= "#424949",
                                            corner_radius = 15)
        
        self.principal_frame["menu"] = CTK.CTkFrame(master = self,
                                            width = 250,
                                            height = 220,
                                            fg_color= "#424949",
                                            corner_radius = 15)
        
        self.principal_frame["keyboard"] = VkeyBoard(self)

        self.principal_frame["frame screen"] = FrameScreen(self)

        self.principal_frame["menu_general"] = CTK.CTkFrame(master = self,
                                                            width = 270,
                                                            height = 110,
                                                            fg_color= "transparent",
                                                            corner_radius = 15)


        self.safitech_title = CTK.CTkLabel(master = self.principal_frame["safitech"],
                                           text = "SAFITECH",
                                           font = CTK.CTkFont(family = "Arial Black",size = 20,weight = "bold"),
                                           )

        self.safitech_slogon = CTK.CTkLabel(master = self.principal_frame["safitech"],
                                    text = "Irrigation System",
                                    height = 3,
                                    font = CTK.CTkFont(family = "Arial Black",size = 14,weight = "bold", slant="italic"),
                                    )


        self.safitech_logo = CTK.CTkLabel(master = self.principal_frame["safitech"],
                                    text = "",
                                    image = CTK.CTkImage(Image.open("images/safitech.png"),size = (70,55)),
                                    )
        for button in range(0,4):
            self.menu_button[button_list[button]] = CTK.CTkButton(master = self.principal_frame["menu"],
                                                    text=button_text[button],
                                                    width = 120,
                                                    height = 100,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#209637",
                                                    hover_color="#30CD4F",
                                                    compound="top",
                                                    image = CTK.CTkImage(Image.open("images/{}".format(button_icons[button])),size = (40,40)),
                                                    corner_radius = 15
                                                    )
        
        for button in range(0,3):
            self.general_button[gbutton_list[button]] = CTK.CTkButton(master = self.principal_frame["menu_general"],
                                                    text=gbutton_list[button],
                                                    width = 90,
                                                    height = 70,
                                                    font = CTK.CTkFont(size = 12,weight = "bold"),
                                                    fg_color= "#209637",
                                                    hover_color="#30CD4F",
                                                    compound="top",
                                                    image = CTK.CTkImage(Image.open("images/{}".format(gbutton_icons[button])),size = (30,30)),
                                                    corner_radius = 15
                                                    )

        self.menu_button["home"].configure(command=self.push_accueil)
        self.menu_button["supervision"].configure(command=self.push_supervision)
        self.menu_button["mode_irrigation"].configure(command=self.push_modes)
        self.menu_button["parameter_irrigation"].configure(command=self.push_parametres)

        self.general_button["eteindre"].configure(command=self.push_eteindre)
        self.general_button["redemarer"].configure(command=self.push_redemarer)

    def push_accueil(self):
        self.principal_frame["frame screen"].set("Acueil")
        
    
    def push_supervision(self):
        self.principal_frame["frame screen"].set("Supervision")
    
    def push_modes(self):
        self.principal_frame["frame screen"].set("Mode Irrigation")
    
    def push_parametres(self):
        self.principal_frame["frame screen"].set("Parametres Irrigation")

    def push_eteindre(self):
        self.destroy()

    def push_redemarer(self):
        self.destroy()

    def disp_components(self):
        self.principal_frame["safitech"].place(relx= 0,rely = 0)
        self.safitech_title.place(relx = 0.32, rely = 0.21)
        self.safitech_slogon.place(relx = 0.32, rely = 0.436)
        self.safitech_logo.place(relx = 0.06, rely = 0.12)

        self.principal_frame["menu"].place(relx= 0.014,rely = 0.2)
        self.menu_button["home"].grid(row=0, column=0, padx=5, pady=5)
        self.menu_button["supervision"].grid(row=0, column=1, padx=5, pady=5)
        self.menu_button["mode_irrigation"].grid(row=1, column=0, padx=5, pady=5)
        self.menu_button["parameter_irrigation"].grid(row=1, column=1, padx=5, pady=5)

        self.principal_frame["menu_general"].place(relx= 0.6,rely = 0.85)
        self.general_button["aide"].grid(row =0,column=0, padx=5, pady=5)
        self.general_button["redemarer"].grid(row =0,column=1, padx=5, pady=5)
        self.general_button["eteindre"].grid(row =0,column=2, padx=5, pady=5)

        self.principal_frame["keyboard"].place(relx= 0.014,rely = 0.6)
        
        self.principal_frame["frame screen"].place(relx= 0.36,rely = 0)
        
        
    def window_configuration(self):
        self.title(constants.wind_title)
        self.geometry("{}x{}".format(constants.wind_dim[0],constants.wind_dim[1] ))
        self.resizable(False,False)

if __name__ == "__main__":
    App().mainloop()
    

