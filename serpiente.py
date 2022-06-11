#importar libreria
#⬛ 🌸
from tkinter import*#para gregar la funcion de texto
import random

#formato de ventana y sobre ventana
direccion = " "
velocidad=30
x,y=15,15
n_limite_posicion=15
#comida
posicion_comida = (15,15)
#cuerpo
posicion_cuerpo = [(75,75)]
nueva_posicion =[(15,15)]

#para mover la figura       
def direccionales():
    global direccion_continua, posicion_cuerpo,nueva_posicion,x,y
    #direccion de serpiente
    if direccion =="Up":#de abajo hacia arriba
        y =  y-velocidad#30
        nueva_posicion[0:]= [(x, y)]
        #para que se "telestraporte" el cuerpo y no se pierda osea tiene como limite la ventana
        if y >=515:# rango de hacia arriba
            y=n_limite_posicion#15              
        elif y <=0:
            y=515#lo que demora en salir por arriba
    elif direccion =="Down":#de arriba hacia abajo 
        y = y+velocidad
        nueva_posicion [0:]= [(x, y)]
        if y >=515:#rango de hacia abajo
            y=n_limite_posicion
        elif y <=0:
            y=n_limite_posicion
    elif direccion == "Left":#de izquierda a derecha
        x = x-velocidad
        nueva_posicion[0:]= [(x, y)]
        if x >=750:
            x = 0
        elif x <=0:
            x=750
    elif direccion == "Right": #de derecha a izquierda c:
        x = x + velocidad
        nueva_posicion[0:]= [(x, y)]
        if x >=750:
            x=n_limite_posicion
        elif x <=0:
            x=n_limite_posicion

    posicion_cuerpo = nueva_posicion + posicion_cuerpo[:-1]#para que se agrege el cuerpo cerca de la cabeza

    for parte, lugar in zip(canvas_pantalla.find_withtag("culebra"), posicion_cuerpo):
        canvas_pantalla.coords(parte, lugar)
#para hacer continuo el movimiento de la serpiente
def direccion_continua(evento):
    global direccion
    if evento == "Left":
        if direccion != "Right":
            direccion = evento
    elif evento == "Right":
        if direccion != "Left":
            direccion = evento
    elif evento == "Up":
        if direccion != "Down":
            direccion = evento
    elif evento == "Down":
        if direccion != "Up":
            direccion = evento

def movimiento():
    global posicion_comida,posicion_cuerpo,nueva_posicion
    posiciones =  [15, 45, 75,105,135,165, 195, 225, 255, 
    285, 315, 345, 375, 405, 435] #+30

    direccionales()
    #velocidad de tiempo (rapidez)
    texto.after(175, movimiento)
    if posicion_comida == posicion_cuerpo[0]:
        numero_de_cuerpo = len(posicion_cuerpo)
        texto2['text'] = 'Cantidad 🌸: {}'.format(numero_de_cuerpo)
        #posicionar el raton en las coordenadas que ya especificados
        posicion_comida = (random.choice(posiciones), random.choice(posiciones))
        posicion_cuerpo.append(posicion_cuerpo[-1])

        #se agregar el cuerpo crece más
        if posicion_comida not in posicion_cuerpo:
            canvas_pantalla.coords(canvas_pantalla.find_withtag("comida"), posicion_comida)
            #-1
        canvas_pantalla.create_text(*posicion_cuerpo[-1], text= "⬛", fill="#1C1C1C", font = ('Arial',25), tag ="culebra")    
       
       
     
    #posicion_cuerpo = nueva_posicion + posicion_cuerpo[:-1] == 15  y  contar(posicion_cuerpo = nueva_posicion + posicion_cuerpo[:-1])
   #-1
    if posicion_cuerpo[-1] == nueva_posicion[0] and len(posicion_cuerpo)>=4: 
        derrota()
        
    for i in posicion_cuerpo:
        if len(posicion_cuerpo)==26:
            victoria()#mensaje de que se llego al limite de nivel 
      
def derrota():
    canvas_pantalla.delete(ALL)
    #fondo de mensaje de que fallaste
    canvas_pantalla.create_image(0,0,image=derrota_imagen,anchor="nw")

def victoria():
    canvas_pantalla.delete(ALL)
    #fondo de mesaje si pierdes o ganas
    canvas_pantalla.create_image(0,0,image=victoria_imagen,anchor="nw")
    
def salir ():
    ventana.destroy()
    ventana.quit()

#formato
ventana = Tk()
ventana.geometry('800x530')#dimension de ventana_ancho y alto
#fondo=PhotoImage(file="fondo.png")
ventana.config(bg="white")#color de fondo ventan Tk
ventana.title("Mini Juego Retro de Serpiente")#titulo
ventana.iconbitmap("serpienteico.ico")#icono
victoria_imagen=PhotoImage(file="victoria.png")
derrota_imagen=PhotoImage(file="derrota.png")
#cordenadas al dar click con el mouse
def motion(event):
    x, y = event.x, event.y
    print('x: {}, y: {}'.format(x, y))
ventana.bind('<Button 1>', motion)

#formato y posicion de boton/texto
cordenada1= Frame(ventana, width=785, height=350, bg='white')
cordenada2 = Frame(ventana, width=785, height=490, bg='white')
cordenada1.grid(column=0, row=0)
cordenada2.grid(column=0, row=1)

#activacion para que funcione cuando precionamos direccionales de teclado
ventana.bind("<KeyPress-Up>", lambda evento:direccion_continua("Up"))
ventana.bind("<KeyPress-Down>", lambda evento:direccion_continua("Down"))
ventana.bind("<KeyPress-Left>", lambda evento:direccion_continua("Left"))
ventana.bind("<KeyPress-Right>",  lambda evento:direccion_continua("Right"))

#fondo de ventana tk y tamaño
canvas_pantalla= Canvas(cordenada2, bg="#C8FE2E", width=800, height=800)
#canvas_pantalla.create_image(0,0,image=fondo,anchor="nw")
canvas_pantalla.pack()

#botones de iniciar tambien texto de conteo de comida/cuerpo
#crea la comida
canvas_pantalla.create_text(85,85, text="🌸", fill='black',font = ("arial",20), tag ="comida")
#crear boton
boton = Button(cordenada1, bg="white",text="¡A comer!",font=("Simplified Arabic Fixed",15,"bold"), command = movimiento)
#posicion del boton
boton.grid(row=0, column=0, padx=20)

#texto
#formato del texto
texto=Label(cordenada1, bg='white', fg = 'black', font=("Simplified Arabic Fixed",15, 'bold'))#negrita,comida
texto2=Label(cordenada1, bg='white', fg = 'black', font=("Simplified Arabic Fixed",18, 'bold'))#conteo infomacion digito
#ubicacion del texto sobre ventana tk
texto2.grid(row=0,column=2, padx=20)

#activacion todo sobre ventana
ventana.mainloop()