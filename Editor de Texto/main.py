def salvarComo():
    global texto
    t = texto.get("1.0", "end-1c")
    saveLocation = tkinter.filedialog.asksaveasfilename()
    arq1 = open(saveLocation, "w+")
    arq1.write(t)
    arq1.close()

def fontHelvetica():
    global texto
    texto.config(font = "Helvetica")

def fontCourier():
    global texto
    texto.config(font = "Courier")

import sys
version = sys.version
if '3.8.3' in version:
    from tkinter import *
    import tkinter.filedialog
root = Tk("Text Editor")
texto = Text(root)
texto.grid()
botao = Button(root, text="SAVE", command= salvarComo)
botao.grid()
font = Menubutton(root, text="Font")
font.grid()
font.tk_menuBar = Menu(font, tearoff = 0)
font["menu"] = font.tk_menuBar
helvetica = IntVar()
courier = IntVar()
font.tk_menuBar.add_checkbutton(label="Courier", variable = courier, command = fontCourier)
font.tk_menuBar.add_checkbutton(label = "Helvetica", variable = helvetica, command= fontHelvetica)
root.mainloop()

