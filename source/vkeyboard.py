import customtkinter as CTK
import string

class VkeyBoard(CTK.CTkTabview):
    def __init__(self,wind):
        super().__init__(master = wind,
                        width = 250,
                        height = 200,
                        fg_color= "#424949",
                        corner_radius = 15)
        self.keys = {}
        self.list_caracters = {}
        self.init_components()


        #display components
        self.disp_components()
    
    def init_components(self):
        self.add("maj")
        self.add("min")
        self.add("num")

        tab_k =[self.tab("maj"),self.tab("min"),self.tab("num")]

        self.list_caracters["alphabet uppercase"] = list(string.ascii_uppercase)
        self.list_caracters["alphabet lowercase"] = list(string.ascii_lowercase)
        self.list_caracters["numbers caracters"] = list(string.digits + string.punctuation)

        key = {}
        d = 0
        for k,v in self.list_caracters.items():
            for m in v:
                key[m] = CTK.CTkButton(master=tab_k[d],
                                        text=m,
                                        font=CTK.CTkFont(size=13),
                                        width = 30,
                                        height = 30,
                                        fg_color= "#209631",
                                        hover_color="#30CD4F",
                                        corner_radius = 10,
                                        command=lambda c=m:self.insert_caract(c))
            self.keys[k] = key
            key = {}
            d+=1
            
    def disp_components(self):
        
        caract = ["alphabet uppercase","alphabet lowercase", "numbers caracters"]
        for k in caract:
            i=0
            for x in range(0,4):
                for y in range(0,7):
                    if i < 26:
                        self.keys[k][list(self.keys[k].keys())[i]].grid(row = x, column = y, padx = 1, pady=2)
                        i+=1
                           
    def insert_caract(self,c):
        pass