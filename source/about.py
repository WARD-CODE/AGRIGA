import customtkinter as CTK
import string



class About(CTK.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.context = """
        SAFITECH IRRIGATION SYSTEM
        _______________________________________
        Société:  Safitech.
        Module:  Interface Homme-Machine.
        type:  Systéme d'irrigation.
        Distrubution:  Irriginnov.
        version:  1.0.0 .
        _______________________________________
        Copyright (C) 2023 All rights reserved. 
        """
        self.init_component(self.context)
        self.disp_component()
    
    def init_component(self, text):
        self.plan_text = CTK.CTkTextbox(master=self,
                                        width= 300
                                        )
        self.plan_text.insert(CTK.END,text)
        self.plan_text.configure(state=CTK.DISABLED)
    
    def disp_component(self):
        self.plan_text.pack()