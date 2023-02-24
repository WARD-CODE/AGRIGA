import customtkinter as CTK
from tkinter import ttk
from constants import constants 
import string
from supervision import Supervision
from mode_irrigation import Mode_irrigation
from parametre_irrigation import parametre_irrigation
class FrameScreen(CTK.CTkTabview):
    def __init__(self,wind):
        super().__init__(master = wind,
                        width = 500,
                        height = 500,
                        fg_color= "#424949",
                        corner_radius = 15,
                        state= "disabled")
        
        self.add("Acueil")
        self.add("Supervision")
        self.add("Mode Irrigation")
        self.add("Parametres Irrigation")
        
        self.disp_components()
        
    def disp_components(self):
        self.supervision_object = Supervision(self.tab("Supervision"))
        self.modeIrrigation_object = Mode_irrigation(self.tab("Mode Irrigation"))
        self.parametreIrrigation_object = parametre_irrigation(self.tab("Parametres Irrigation"))
        