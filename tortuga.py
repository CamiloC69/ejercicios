import turtle # IMPORATA LA LIBRERIA

# CREA VENTANA DE VISUALZACION GRAFICA
ventana = turtle.Screen()

# CREA EL OBJETO, LA CUAL SERA LA "TORTUGA" QUE DIBUJARA EL GRAFICO
tortuga = turtle.Turtle()

# BUCLE REPITIENDO 4 VECES UNA LINEA DE 100 PX GIRANDO HACIA LA DERECHA EN CADA REPETICION
for i in range(4):
    tortuga.forward(100)
    tortuga.right(90)
    
# ABRE LA VENTANA DONDE MOSTRARA EL GRAFICO AUTOMATICAMENTE
ventana.exitonclick()

'''window = turtle.Screen()
tortuga = turtle.Turtle()

tortuga.forward(100)
tortuga.right(90)

tortuga.forward(100)
tortuga.right(90)

tortuga.forward(100)
tortuga.right(90)

tortuga.forward(100)
tortuga.right(90)

tortuga.forward(100)
tortuga.left(-135)

tortuga.forward(145)

window.mainloop()'''