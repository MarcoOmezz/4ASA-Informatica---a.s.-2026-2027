'''realizza una semplice interfaccia grafica che permette di calcolare il costo totale di una spesa. Nello specifico il programma 
dovrà chiedere due dati all'utente: il prezzo base e la quantità. Al click di un pulsante il programma dovrà ritornare il costo complessivo 
(dato dal prezzo * quantità)'''

import tkinter as tk 

def calcolo():
    valorecosto = float(costo.get())
    valoreqta = float(qta.get())
    totale = valoreqta * valorecosto
    risultato.config(text=f"valore complessivo {totale}€")

root = tk.Tk()
root.title("calcolo")
root.geometry("400x300")

costo = tk.StringVar()
qta = tk.StringVar()

risultato = tk.Label(root, text="", font=("Arial", 14))
risultato.grid(row=0, column=0, columnspan=2, pady=20)

labelprezzo = tk.Label(root, text="prezzo:")
labelprezzo.grid(row=1, column=0, padx=10, pady=10, sticky="e")

labelquantita = tk.Label(root, text="quatnita:")
labelquantita.grid(row=2, column=0, padx=10, pady=10, sticky="e")

entryprezzo = tk.Entry(root, textvariable=costo)
entryprezzo.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

entryquantita = tk.Entry(root, textvariable=qta)
entryquantita.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

pulsante=tk.Button(root, text="calcolo", command=calcolo)
pulsante.grid(row=3, column=0, columnspan=2,  padx=10, pady=10, sticky="e")

root.mainloop()