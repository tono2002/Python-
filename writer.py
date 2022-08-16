
print("Writer")
print("-----------")

path = input("Ruta del archivo: ")
print("RECIBIDO!")
def what():
    a1 = input("(w) write / (r) read: ")
    if a1 == "w": #Escribir
        a2 = input("(w) write below / (o) overwrite text: ")
        if a2 == "w":
            txt = input("Text to write: ")
            wr = open(path, "at")
            wr.write(str(txt))
            wr.close()
        elif a2 == "o":
            txt = input("Text to write: ")
            wr = open(path, "wt")
            wr.write(str(txt))
            wr.close()
    elif a1 == "r":
        rd = open(path, "rt")
        a3 = int(input("Characters to read: "))
        print(rd.read(a3))
        rd.close()
    else:
        what()

what()

