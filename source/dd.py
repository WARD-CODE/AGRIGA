import tkinter as tk
import re

class HourEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.pattern = re.compile(r'^([01][0-9]|2[0-3]):[0-5][0-9]$')
        self.configure(validate='key')
        self.configure(validatecommand=self.validate_command)

    def validate_command(self):
        value = self.get()
        if not value:
            return True
        match = self.pattern.match(value)
        return match is not None

# Example usage
root = tk.Tk()
entry = HourEntry(root)
entry.pack()
root.mainloop()