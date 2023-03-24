import customtkinter as CTK
from supervision import Supervision
from mode_irrigation import Mode_irrigation
from parametre_irrigation import parametre_irrigation
from accueil import Accueil
class FrameScreen(CTK.CTkTabview):
    def __init__(self,wind,keypad):
        super().__init__(master = wind,
                        width = 500,
                        height = 500,
                        fg_color= "#424949",
                        corner_radius = 15,
                        state= "disabled")
        
        self.add("Accueil")
        self.add("Supervision")
        self.add("Modes Irrigation")
        self.add("Parametres Irrigation")
        
        self.disp_components()
        self.keypad_activation(keypad)

    def disp_components(self):
        self.supervision_object = Supervision(self.tab("Supervision"))
        self.modeIrrigation_object = Mode_irrigation(self.tab("Modes Irrigation"))
        self.parametreIrrigation_object = parametre_irrigation(self.tab("Parametres Irrigation"))
        self.accueil_object = Accueil(self.tab("Accueil"))

    def keypad_activation(self,keypad):

        keypad.add_stackEntries(self.supervision_object.actionneurs_frame["pompe"])
        keypad.add_stackEntries(self.supervision_object.actionneurs_frame["electrovanne"])

        keypad.add_stackEntries(self.modeIrrigation_object.drip_entries["distance_ligne"])
        keypad.add_stackEntries(self.modeIrrigation_object.drip_entries["espace_gouteur"])
        keypad.add_stackEntries(self.modeIrrigation_object.drip_entries["debit_eau"])

        keypad.add_stackEntries(self.modeIrrigation_object.aspersion_entries["diam_gouteur"])
        keypad.add_stackEntries(self.modeIrrigation_object.aspersion_entries["ecart_gouteur"])
        keypad.add_stackEntries(self.modeIrrigation_object.aspersion_entries["distance_ligne"])
        keypad.add_stackEntries(self.modeIrrigation_object.aspersion_entries["pression"])

        keypad.add_stackEntries(self.parametreIrrigation_object.irrigation_entries["type"])
        keypad.add_stackEntries(self.parametreIrrigation_object.irrigation_entries["frequence"])
        keypad.add_stackEntries(self.parametreIrrigation_object.culture_entries["surface"])
        keypad.add_stackEntries(self.parametreIrrigation_object.culture_entries["culture"])
        keypad.add_stackEntries(self.parametreIrrigation_object.culture_entries["element"])
        keypad.add_stackEntries(self.parametreIrrigation_object.culture_entries["Kc_saison"])
        keypad.add_stackEntries(self.parametreIrrigation_object.culture_entries["Kc"])
        keypad.add_stackEntries(self.parametreIrrigation_object.culture_entries["auto"])


        
