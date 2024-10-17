from tkinter import Label, Button, Entry, Tk, Frame, PhotoImage #button=cria o botão, entry=para voce digitar, frame=cria a parte da linha verde, tk = biblioteca
import qrcode
from PIL import Image, ImageTk #PIL=mostra a imagem
from tkinter import messagebox #mostra uma tela que tenha o envolvimento do usuario
import pyshorteners #encurta a url

root = Tk() #root=raiz, o root serve para criar  a tela raiz, a tela principal
root.title('Gerador de Código QR') #gera o qr code
root.config(padx=50, pady=100) #padX= tamanho do espaçamento da input, padY= tamanho do espaçamento do qrcode ate a tela principal

def create_image_window(root: Tk, image_path: str): #a função vai criar a janela da imagem do qrcode
    frame_image = Frame(root, highlightbackground='green', highlightcolor='green', highlightthickness=1, width=400, height=450, bd=2) #width= largura da tela, height= altura da tela
    frame_image.pack(side='right') #o qrcode fica do lado direito da tela principal
    frame_image.propagate(False) #**a propagação da imagem é falsa
    img = Image.open(image_path) #vai abrir a imagem, o valor será os bytes que abrem a imagem
    tk_img = ImageTk.PhotoImage(img)
    label = Label(frame_image, image=tk_img) #o label é um rótulo
    label.grid(row=2, column=1, columnspan=2)#determina o tamanho do label, tipo row= 2(linha=2), column=1(coluna=1)
    label.pack()#junta as linhas, compacta elas, termina o label
    add_button = Button(frame_image, text='gerar novo', width=36, command=lambda: voltar_tela_inicial(frame_image)) #adiciona o botão, width= tamanho da largura, comando=lambda(lambda recebe qualquer número de argumentos, o root na voltar tela inicial da raiz)
    add_button.grid(row=4, column= 1, columnspan = 2) #a posição do botão
    add_button.pack()#termina o botão, posiciona o centro do item colocado
    root.mainloop()#rodar o código
def gera_qr_code(root: Tk, main_entry: Entry):#gera o qr code e emntrada de dados
    url = main_entry.get()
    if len(url) == 0:#mostra se a url é falsa, len=tamanho da url
        messagebox.showinfo(title='Erro!', message='Favor insira uma URL válida: ')
    else:#senão for falsa...:
        main_entry.delete(0, 'end')
        opcao_escolhida = messagebox.askokcancel(title=url, message=(f'o endereço de url é: \n {url}'))
        if opcao_escolhida: qr = qrcode.QRCode(version=1, box_size=10, border=5)
        short_url = pyshorteners.Shortener().tinyurl.short(url)
        qr.add_data(short_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color='Black', back_color='white')#cores do preenchimento e cor de fundo do qr code
        img.save('qrExport.png')#vai salvar a imagem
        create_image_window(root, 'qrExport.png')#cria a janela da imagem
def create_main(root: Tk):#função que ta configurando a tela principal
    frame_main = Frame(root, highlightbackground='green', highlightcolor='green', highlightthickness=1, width=400, height=150, bd=2)#config da tela, width= tamanho da largura da tela principal, height = tamanho da altura da tela principal
    frame_main.pack(side='left')#a posição do input
    frame_main.propagate(False)
    main_label = Label(frame_main, text='URL:')
    main_label.grid(row=2, column=0)
    main_label.pack()
    main_entry = Entry(frame_main, width=35)
    main_entry.grid(row=2, column=1, columnspan=2)
    main_entry.focus()
    main_entry.pack()
    add_button = Button(frame_main, text='gerar qr code', width=36, command=lambda:gera_qr_code(root, main_entry))
    add_button.grid(row=4, column=1, columnspan=2)
    add_button.pack()
    root.mainloop()

def voltar_tela_inicial(frame_image):
    frame_image.destroy()

create_main(root)
    
    

