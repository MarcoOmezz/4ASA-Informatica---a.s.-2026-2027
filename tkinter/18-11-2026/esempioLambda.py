import tkinter as tk

def saluta(nome):
    testo.config(text=f"Ciao {nome}")

root = tk.Tk()
root.geometry("400x300")
root.title("Prova Lambda")

testo = tk.Label(root, text="")
testo.pack()

pulsante = tk.Button(root, text="Saluta", command=lambda: saluta("Mario"))
pulsante.pack()

root.mainloop()