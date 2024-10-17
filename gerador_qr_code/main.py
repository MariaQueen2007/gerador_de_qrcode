import tkinter as tk

class Main(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

    def configura_titulo(self, titulo:str) -> None:
        self.title(titulo)
        pass
    def configura_tamhorizontal(self, horizontal:float) -> None:
        self.config(padx=horizontal)
        pass
    def configura_tamvertical(self, vertical:float) -> None:
        self.config(pady=vertical)
    