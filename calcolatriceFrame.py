import tkinter as tk

def cliccato(valore):
    display.config(text=f"{valore}")

root = tk.Tk()
root.geometry("400x600")
root.title("Calcolatrice")

frame_display = tk.Frame(root)
frame_display.pack()

frame_pulsanti = tk.Frame(root)
frame_pulsanti.pack()

#creo il display
display = tk.Label(frame_display, text="0", font=("Arial", 20))
display.pack()


#griglia
numero = 1
for i in range(0, 3):
    for j in range(0, 3):
        pulsante = tk.Button(frame_pulsanti, text=f"{numero}", command=lambda n=numero: cliccato(n))
        pulsante.grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
        numero += 1

virgola = tk.Button(frame_pulsanti, text=",")
virgola.grid(row=3, column=0, padx=10, pady=10, ipadx=10, ipady=10)

zero = tk.Button(frame_pulsanti, text="0")
zero.grid(row=3, column=1, padx=10, pady=10, ipadx=10, ipady=10)

uguale = tk.Button(frame_pulsanti, text="=")
uguale.grid(row=3, column=2, padx=10, pady=10, ipadx=10, ipady=10)

diviso = tk.Button(frame_pulsanti, text="/")
diviso.grid(row=3, column=3, padx=10, pady=10, ipadx=10, ipady=10)

piu = tk.Button(frame_pulsanti, text="+")
piu.grid(row=0, column=3, padx=10, pady=10, ipadx=10, ipady=10)

meno = tk.Button(frame_pulsanti, text="-")
meno.grid(row=1, column=3, padx=10, pady=10, ipadx=10, ipady=10)

per = tk.Button(frame_pulsanti, text="x")
per.grid(row=2, column=3, padx=10, pady=10, ipadx=10, ipady=10)

root.mainloop()