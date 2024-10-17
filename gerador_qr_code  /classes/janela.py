import tkinter as tk

class Janela(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs).__init__()
        self.title('Gerador de Qrcode')
        self.config(padx=10, pady=100)
