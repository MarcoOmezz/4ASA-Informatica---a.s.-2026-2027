'''
Realizza un programma che fa inserire all'utente il suo nome
e in una label scrive "Ciao [nome]"
'''

import tkinter as tk

def saluta():
    valore = nome.get()
    testo.config(text=f"Ciao {valore}")

root = tk.Tk()
root.geometry("300x300")
root.title("Prova stringVar")

#variabili
nome = tk.StringVar()
#---

testo = tk.Label(root, text="")
testo.pack()

campoTesto = tk.Entry(root, textvariable=nome)
campoTesto.pack()

pulsante = tk.Button(root, text="Saluta", command=saluta)
pulsante.pack()

nome.set("Inserisci il tuo nome")

root.mainloop()