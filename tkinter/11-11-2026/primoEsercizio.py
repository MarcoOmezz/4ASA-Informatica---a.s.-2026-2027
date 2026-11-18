import tkinter as tk

def saluta():
    etichetta.config(text="Ciao, hai cliccato!")

root = tk.Tk()
root.title("Esercizio prova")
root.geometry("300x200")

root.configure(bg="lightblue")

#label
etichetta = tk.Label(root, text="Benvenuto!", font=("Arial", 16))

#posizionare
etichetta.pack(pady=10)

pulsante = tk.Button(root, text="Cliccami!", command=saluta)
pulsante.pack(pady=20)

root.mainloop() #da inserire sempre