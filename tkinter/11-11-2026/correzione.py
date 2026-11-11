import tkinter as tk

def scriviUno():
    label.config(text="1")

def scriviDue():
    label.config(text="2")

root = tk.Tk()
root.title("Esercizio per casa")
root.geometry("300x200")

label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=10)

pulsante1 = tk.Button(root, text="1", command=scriviUno)
pulsante1.pack(pady=20)

pulsante2 = tk.Button(root, text="2", command=scriviDue)
pulsante2.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()