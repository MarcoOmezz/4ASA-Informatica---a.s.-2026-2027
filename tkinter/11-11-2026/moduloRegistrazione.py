import tkinter as tk

root = tk.Tk()
root.title("Modulo registrazione")
root.geometry("400x300")

labelNome = tk.Label(root, text="Nome:")
labelNome.grid(row=0, column=0, padx=10, pady=10, sticky="e")

labelCognome = tk.Label(root, text="Cognome:")
labelCognome.grid(row=1, column=0, pady=10, padx=10, sticky="e")

labelEmail = tk.Label(root, text="Email:")
labelEmail.grid(row=2, column=0, sticky="e", padx=10, pady=10)

entryNome = tk.Entry(root)
entryNome.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

entryCognome = tk.Entry(root)
entryCognome.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

entryEmail = tk.Entry(root)
entryEmail.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

pulsante = tk.Button(root, text="REGISTRATI")
pulsante.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="e")



root.mainloop()