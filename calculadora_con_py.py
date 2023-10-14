from tkinter import *

#Ventana
ventana= Tk() 
ventana.title("Calculadora")

#Entrada
entrada= Entry(ventana, font= "Arial 18")
entrada.grid(row=0,column=0,columnspan=4,pady=5,padx=5)

#Creamos botones
botón0 = Button(ventana, height=2, width=15, text= "0", command= lambda: click(0))
botón1 = Button(ventana, height=2, width=5, text= "1", command= lambda: click(1))
botón2 = Button(ventana, height=2, width=5, text= "2", command= lambda: click(2))
botón3 = Button(ventana, height=2, width=5, text= "3", command= lambda: click(3))
botón4 = Button(ventana, height=2, width=5, text= "4", command= lambda: click(4))
botón5 = Button(ventana, height=2, width=5, text= "5", command= lambda: click(5))
botón6 = Button(ventana, height=2, width=5, text= "6", command= lambda: click(6))
botón7 = Button(ventana, height=2, width=5, text= "7", command= lambda: click(7))
botón8 = Button(ventana, height=2, width=5, text= "8", command= lambda: click(8))
botón9 = Button(ventana, height=2, width=5, text= "9", command= lambda: click(9))


botón_div = Button(ventana, height=2, width=5, text= "÷", command= lambda: click("/"))
botón_mul = Button(ventana, height=2, width=5, text= "x", command= lambda: click("*"))
botón_igual = Button(ventana, height=2, width=5, text= "=", command= lambda: resultado())
botón_mas = Button(ventana, height=2, width=5, text= "+", command= lambda: click("+"))
botón_menos = Button(ventana, height=2, width=5, text= "-", command= lambda: click("-"))

botón_punto = Button(ventana, height=2, width=5, text= ".", command= lambda: click("."))
botón_parentesis1 = Button(ventana, height=2, width=5, text= "(", command= lambda: click("("))
botón_parentesis2 = Button(ventana, height=2, width=5, text= ")", command= lambda: click(")"))
botón_borrar = Button(ventana, height=2, width=5, text= "AC", command= lambda: borrar())

#Agrego
botón_borrar.grid( row=1, column=0, padx=5, pady=5)
botón_parentesis1.grid( row=1, column=1, padx=5, pady=5)
botón_parentesis2.grid( row=1, column=2, padx=5, pady=5)
botón_div.grid( row=1, column=3, padx=5, pady=5)
botón1.grid( row=2, column=0, padx=5, pady=5)
botón2.grid( row=2, column=1, padx=5, pady=5)
botón3.grid( row=2, column=2, padx=5, pady=5)
botón_mul.grid( row=2, column=3, padx=5, pady=5)
botón4.grid( row=3, column=0, padx=5, pady=5)
botón5.grid( row=3, column=1, padx=5, pady=5)
botón6.grid( row=3, column=2, padx=5, pady=5)
botón_menos.grid( row=3, column=3, padx=5, pady=5)
botón7.grid( row=4, column=0, padx=5, pady=5)
botón8.grid( row=4, column=1, padx=5, pady=5)
botón9.grid( row=4, column=2, padx=5, pady=5)
botón_mas.grid( row=4, column=3, padx=5, pady=5)
botón0.grid( row=5, column=0, columnspan=2, padx=5, pady=5)
botón_punto.grid( row=5, column=2, padx=5, pady=5)
botón_igual.grid( row=5, column=3, padx=5, pady=5)

#Agregamos funcionalidad

indice=0
def click(valor):
    if entrada.get() == "Math Error":
        entrada.delete(0, "end")
    global indice
    entrada.insert(indice,valor)
    indice= indice+1

def borrar():
    entrada.delete(0,"end")
def resultado():
    try:
        ecuación= entrada.get()
        resultado= eval(ecuación)
        entrada.delete("0","end")
        entrada.insert(0,resultado)
    except:
        entrada.delete(0,"end")
        entrada.insert(0,"Math Error")
        
ventana.mainloop()

