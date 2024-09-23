
import tkinter as tk
from tkinter import font

tela = tk.Tk()
tela.title("my baby")
tela.geometry("300x250")

nova_font = font.Font(family="arial",size=24)
font01 = font.Font(family="times new roman", size=26)
font02 = font.Font(family="arial black", size=32)

Label = tk.Label(tela, text="my baby", font=nova_font)
Label.pack(pady=20)

Label = tk.Label(tela, text="my baby", font=font01)
Label.pack(pady=20)

Label = tk.Label(tela, text="my baby", font=font02)
Label.pack(pady=20)

botao= tk.Button(tela,text="botao")
botao.pack(pady=5)

caixa_texto = tk.Entry(tela)
caixa_texto.pack(pady=5)

tela.mainloop()
