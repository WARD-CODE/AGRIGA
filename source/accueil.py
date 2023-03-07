
import customtkinter as CTK
from PIL import Image
from horloge import Horloge

class Accueil:
    def __init__(self,master, *args, **kwargs):
        super().__init__(*args , **kwargs)
        self.accueil_frame={}
        self.datime_objects = {}
        self.init_components(master)

        self.disp_components()

    
    def init_components(self, master):
        self.accueil_frame["mainframe"] = CTK.CTkFrame(master=master,
                                                       height=440,
                                                       width=470,
                                                       fg_color="#101010",
                                                       corner_radius=15)
        
        self.accueil_frame["mainbar"] = CTK.CTkFrame(master=self.accueil_frame["mainframe"],
                                                       height=40,
                                                       width=450,
                                                       fg_color="#171717",
                                                       corner_radius=10)
        
        self.accueil_frame["toolbar"] = CTK.CTkFrame(master=self.accueil_frame["mainframe"],
                                                       height=60,
                                                       width=200,
                                                       fg_color="#171717",
                                                       corner_radius=25)
        
        self.logo = CTK.CTkLabel(master=self.accueil_frame["mainframe"],
                                 text = "SAFITECH Irrigation System",
                                 font = CTK.CTkFont(family="Arial Black", size = 15,weight="bold"),
                                 text_color="#202020",
                                 image = CTK.CTkImage(Image.open("images/safitech_gray_no.png"),size = (140,105)),
                                 compound="top",
                                 bg_color="transparent",
                                 pady= 10

                                 )
        
        self.datime_objects["time"] = Horloge(self.accueil_frame["mainbar"],"time",text_size=25)
        self.datime_objects["date"] = Horloge(self.accueil_frame["mainbar"],"date",text_size=20)
        
        # self.connectivity["mainbutton"] = CTK.CTkButton(master=self.accueil_frame["toolbar"],
        #                                                 text='',
        #                                                 image=CTK.CTkImage(Image.open("images/"))
        #                                                 )

    def disp_components(self):
        self.accueil_frame["mainframe"].pack()
        self.accueil_frame["mainbar"].place(relx=0.02,rely=0.02)
        self.logo.place(relx=0.5/2,rely=0.7/2)
        self.datime_objects["time"].place(relx=0.01,rely=0.12)
        self.datime_objects["date"].place(relx=0.63,rely=0.12)
        self.accueil_frame["toolbar"].place(relx=0.55/2,rely=0.83)