import customtkinter as CTK
from tkintertable import TableCanvas



class TableFrame(CTK.CTkToplevel):
    def __init__(self,CSV_file = "Historique.csv"):
        super().__init__()
        self.wm_title("Historique")
        self.Table = None
        self.init_components(CSV_file)
        self.disp_components()
    
    def init_components(self,CSV_file):
        self.Table = TableCanvas(self)
        self.Table.importCSV("Databases/{}".format(CSV_file))

    def disp_components(self):    
        self.Table.show()



