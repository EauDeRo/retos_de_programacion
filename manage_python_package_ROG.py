from python_package_ROG import heladeria_rog

heladeria_rog.welcome()
(contenedor,num_bolas,sabores_de_helado)=heladeria_rog.recopila_datos()
print("\n\n ¡Perfecto!, recapitulemos, querías un/a " + contenedor +" de helado de "+num_bolas +" bolas.\n Los sabores que has elegido son los siguientes:  " + sabores_de_helado.__str__() )

print ("aquí lo tienes: \n")
heladeria_rog.dibuja_helado (num_bolas,contenedor)

heladeria_rog.bye()