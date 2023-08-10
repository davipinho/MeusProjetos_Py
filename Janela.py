from tkinter import *

def clique(): 
    texto.configure(text= "Ligado")

janela = Tk()
janela.title("Janela")
janela.geometry("400x300")
janela.resizable(True , True)

texto = Label(janela, text="Desligado")
texto.pack()
button = Button(janela, text = "Ligar" , command=clique)
button.pack()

janela.mainloop()
