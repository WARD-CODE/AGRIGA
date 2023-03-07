from tkcalendar import Calendar #à installer
from tktimepicker import AnalogPicker #à installer
import customtkinter as CTK
from PIL import Image


class Vcalender(CTK.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Calendrier")
        self.init_component()
        self.disp_component()
        
    def init_component(self):
        self.calend = Calendar(master = self, key ="day", year =2023, month=3,day=1)
        self.button = CTK.CTkButton(master=self,
                                    text="",
                                    image = CTK.CTkImage(Image.open("images/appliquer.png"),size = (25,25))
                                    )
        
    def disp_component(self):
        self.calend.pack(pady=4)
        self.button.pack(pady=3)

class Vclock(CTK.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        self.title("Clock")
        self.init_component()
        self.disp_component()
        
        
    def init_component(self):
        self.clock = AnalogPicker(self, per_orient='vertical')
        
        self.clock.configAnalog(headcolor="#209617", handcolor="#209617", bg="#363636",
                                      clickedcolor="#ffffff", textcolor="#ffffff", canvas_bg="#404040",
                                      alttextwidth=2, bdwidth=0)

        self.clock.configSpin(bg="#404040", height=1, fg="#ffffff", font=("Times", 12), hoverbg="#404040",
                                    hovercolor="#209617", clickedbg="#2e2d2d", clickedcolor="#209617")

        self.clock.configSeparator(font=("Times", 18, "bold"), width=1)
        
       
        
        self.button = CTK.CTkButton(master=self,
                                    text="",
                                    image = CTK.CTkImage(Image.open("images/appliquer.png"),size = (25,25))
                                    )
        
    def disp_component(self):
        self.clock.pack(pady=4)
        self.button.pack(pady=3)