import customtkinter as CTK
from PIL import Image
import random

class MesureLabel(CTK.CTkFrame):
    def __init__(self,lab_text, lab_image, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.lab = None
        self.val = None

        self.init_components(lab_text,lab_image)
        self.disp_components()

    def init_components(self,lab_text, lab_image):

        self.lab = CTK.CTkLabel(master = self,
                                text=lab_text,
                                width = 120,
                                height = 90,
                                font = CTK.CTkFont(size = 12,weight = "bold"),
                                fg_color= "gray",
                                compound="top",
                                image = CTK.CTkImage(Image.open("images/{}".format(lab_image)),size = (40,40)),
                                corner_radius = 15,
                                anchor = "center"
                                )
            
        self.val= CTK.CTkLabel(master = self,
                                text="0.00",
                                width = 120,
                                height = 25,
                                font = CTK.CTkFont(size = 17,weight = "bold"),
                                fg_color= "green",
                                corner_radius = 15,
                                anchor = "center"
                                )

    def disp_components(self):
        self.lab.grid(row = 0,column=0,pady = 5)
        self.val.grid(row = 1,column=0)


    def update_value(self,value):
        self.val.configure(text = "{:.2f}".format(value))



