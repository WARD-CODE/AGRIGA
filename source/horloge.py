
import customtkinter as CTK
import datetime
from PIL import Image
import locale

locale.setlocale(locale.LC_TIME, 'fr_FR')
class Horloge(CTK.CTkLabel):
    def __init__(self, master,type,text_size):
        if type == "time":
            image_file = "horloge_home.png"
        else:
            image_file = "calendar_home.png"

        super().__init__(master=master, 
                         font=CTK.CTkFont('OCR A Std', text_size), 
                         fg_color = "transparent",
                         bg_color="transparent",
                         text_color="#30CD4F",
                         image=CTK.CTkImage(Image.open("images/{}".format(image_file)),size=(30,30)),
                         compound="left",
                         padx= 5
                         )
        if type == "time":
            self.update_clock()
        else:
            self.update_calendar()

    def update_clock(self):
        # Get the current time
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        
        # Update the clock label
        self.configure(text=current_time)
        
        # Schedule the update_clock function to be called again in 1000ms (1 second)
        self.after(1000, self.update_clock)
    
    def update_calendar(self):
        current_date = datetime.datetime.now().strftime("%a%d %b %Y")        
        # Update the clock label
        self.configure(text=current_date)
        
        # Schedule the update_clock function to be called again in 1000ms (1 second)
        self.after(60000, self.update_calendar)