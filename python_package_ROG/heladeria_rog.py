###Heladería###

def welcome():
    mensaje_bienvenida= "Bienvenidos a la heladeria saludable"
    print(mensaje_bienvenida)
def recopila_datos():
    name=input("¡Buenos días! ¿Dómo te llamas?  : ")
    print("¡saludos "+ name +"! Que la fuerza te acompañe.")
    contenedor=input("¿Qué vas a tomar tarrina o cucurucho?  : ")
    num_bolas=input("¿Cuantas bolas de helado quieres?  : ")
    if int(num_bolas) > 3: 
        print("Que listo calisto...venga te pongo 3 pero porque eres tú")
        num_bolas=3
    elif int(num_bolas) < 0:
        print("no se admiten devoluciones")
        num_bolas=0

    else:
        print("¡Buena ellección!")

    sabores_de_helado=[]

    for i in range(0,int(num_bolas)):
        añadir_sabor=input("Dime el sabor un numero " + str(i+1) +": ")
        print(añadir_sabor + "!! ¡¡Qué buena elección!!")
        sabores_de_helado.append(añadir_sabor)

    
    return (contenedor,num_bolas,sabores_de_helado)
def dibuja_helado(num_bolas,contenedor):
    if int(num_bolas)== 0: dibubolas="   \n"
    elif int(num_bolas) == 1: dibubolas="  0\n"
    elif int(num_bolas) == 2 : dibubolas="  0\n  0\n"
    else : dibubolas=" 000\n"

    if contenedor == "cucurucho" :
        dibuenvase=" \\ /\n  V\n"
        print(dibubolas + dibuenvase )
    elif contenedor == "tarrina" :
        dibuenvase="|___|\n"
        print(dibubolas + dibuenvase )
    else : print(dibubolas + contenedor +"\n")
def bye():
    print(" Espero que te haya gustado y recuerda nuestros helados son digitales y por lo tanto  tienen 0 calorias . Además, nuestros helados son aptos para todo tipos de alergias e intolerancias :) \n ")
