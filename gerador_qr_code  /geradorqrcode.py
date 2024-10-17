from tkinter import *
import tkinter as tk
import qrcode
from PIL import Image, Image, ImageTk
from tkinter import messagebox
from classes.janela import Janela

def create_image_window(image_path):
    window = Janela()
    img = Image.open(image_path)
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=tk_img)
    label.grid(row=2, column=1, columnspan=2)
    window.mainloop()
def gera_qr_code(window, website_entry):
    url = website_entry.get()
    if len(url) == 0:
        messagebox.showinfo(title="Erro!",message="Favor insira uma URL vÃ¡lida")
    else:
        opcao_escolhida = messagebox.askokcancel(
        title=url,
        message=f"O endereÃ§o URL Ã©: \n "
                f"EndereÃ§o: {url} \n "
                f"Pronto para salvar?")
    if opcao_escolhida:
      qr = qrcode.QRCode(version=1, box_size=10, border=5)
      qr.add_data(url)
      qr.make(fit=True)
      img = qr.make_image(fill_color='black', back_color='white')
      img.save('qrExport.png')
      window.destroy()
      create_image_window('qrExport.png')
def create_main():
    window = Janela()
    # window.title("Gerador de CÃ³digo QR")
    # window.config(padx=10, pady=100)
    # Labels
    website_label = Label(text="URL:")
    website_label.grid(row=2, column=0)
    # Entries
    website_entry = Entry(width=35)
    website_entry.grid(row=2, column=1, columnspan=2)
    website_entry.focus()
    add_button = Button(text="Gerar QR Code", width=36, command=lambda: gera_qr_code(window, website_entry))
    add_button.grid(row=4, column=1, columnspan=2)
    window.mainloop()
def voltar_tela_inicial(window):
    window.destroy()
    create_main()
create_main()
