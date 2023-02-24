
import customtkinter as CTK
from tkinter import messagebox
from constants import constants 

class SignIN_W(CTK.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #setting of the sign IN window
        self.geometry("{}x{}+400+300".format(constants.signIN_wind_dim[0],constants.signIN_wind_dim[1]))
        self.title(constants.signeIN_wind_title)
        self.resizable(False, False)


        #initiate components
        self.init_components()

        #display components
        self.disp_components()
        
    def init_components(self):
        self.main_frame = CTK.CTkLabel( master = self,text="", 
                                        width = constants.signIN_frame1_dim[0],
                                        height = constants.signIN_frame1_dim[1],
                                        fg_color = "#424949",
                                        corner_radius = 10
                                        )

        self.title_in = CTK.CTkLabel(master = self, 
                                     text="Sign In",
                                     font = CTK.CTkFont(family="Times New Roman",size = 25, weight = "bold"))

        self.user_entry =CTK.CTkEntry(master = self.main_frame,
                                      placeholder_text = "entrer un utilisateur",
                                      font = CTK.CTkFont(size = 15),
                                      width = 200,
                                      height = 35)

        self.password_entry = CTK.CTkEntry(master = self.main_frame,
                                           placeholder_text="entrer un mot de passe",
                                           font = CTK.CTkFont(size = 15),
                                           width = 200,
                                           height = 35,
                                           )
        self.password_entry.configure(show='#')

        self.connect_button = CTK.CTkButton(master = self, 
                                            text = "connect",
                                            font= CTK.CTkFont(size=14),
                                            width=100,
                                            height =25,
                                            fg_color = "green",
                                            command = self.check_user)
    
    def disp_components(self):
        self.title_in.place(relx = 0.36, rely = 0.1)
        self.main_frame.place(relx = 0.15, rely = 0.4)
        self.user_entry.place(relx = 0.03, rely = 0.1)
        self.password_entry.place(relx = 0.03, rely = 0.55)
        self.connect_button.place(relx = 0.33, rely = 0.8)

    def check_user(self):
        user_data = [self.user_entry.get(), self.password_entry.get()]
        if user_data == constants.user_data:
            messagebox.showinfo("sign in successful","welcome to the main User Interface")
            self.destroy()
        else:
            messagebox.showwarning("sign in failed","username or parssword is incorrect!\nplease try again")
