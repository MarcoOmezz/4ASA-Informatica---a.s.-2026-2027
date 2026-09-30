file = open("test.txt", "a") #r, w, a

#lettura
contenuto = file.read()

#scrittura
testo = "Ciao a tutti"
file.write(testo)

#chiusura
file.close() #fondamentale

#metodo smart
with open("test.txt", "w") as file:
    file.write(testo)
#posso non chiudere il file, lo fa automaticamente with