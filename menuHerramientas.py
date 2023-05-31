from HerramientasFunciones import palabraValida, siNumeros,convertirCaracter,convertirPalabra
numero=""
def menu():
    opcion=(input("¡Bienvenido al menú principal!\n¿Que quieres hacer hoy?\nEstas son las opciones, escribe solo el número:\n1) Generar la representación en byte de un carácter\n2) Generar la representación en byte de una palabra\n"))
    while not(cuantosCaracters(opcion)):
        opcion=(input("¡Hey has colocado mas de un caracter!\nColoca solo uno 1 o un 2\nEstas son las opciones:\n1) Generar la representación en byte de un carácter\n2) Generar la representación en byte de una palabra\n"))
    verificacion=ord(opcion)
    while verificacion>58 or verificacion<47:
        opcion=(input("¡Hey has colocado un caracter diferente a un número!\nColoca 1 o 2\nEstas son las opciones:\n1) Generar la representación en byte de un carácter\n2) Generar la representación en byte de una palabra\n"))
        while not(cuantosCaracters(opcion)):
            opcion=(input("¡Hey has colocado mas de un caracter!\nColoca solo un 1 o un 2\nEstas son las opciones:\n1) Generar la representación en byte de un carácter\n2) Generar la representación en byte de una palabra\n"))
        verificacion=ord(opcion)
    opcion=int(opcion)
    while opcion!=1 and opcion!=2:
        opcion=input("Hay has colocado un número diferente de 1 o 2.\nRecuerda, estas son las opciones:\n1) Generar la representación en byte de un carácter\n2) Generar la representación en byte de una palabra\n")
        while not(cuantosCaracters(opcion)):
            opcion=(input("¡Hey has colocado mas de un caracter!\nColoca solo un 1 o un 2\nEstas son las opciones:\n1) Generar la representación en byte de un carácter\n2) Generar la representación en byte de una palabra\n"))
        verificacion=ord(opcion)
        while verificacion>58 or verificacion<47:
            opcion=(input("¡Hey has colocado un caracter diferente a un número!\nColoca 1 o 2\nEstas son las opciones:\n1) Generar la representación en byte de un carácter\n2) Generar la representación en byte de una palabra\n"))
            while not(cuantosCaracters(opcion)):
                opcion=(input("¡Hey has colocado mas de un caracter!\nColoca solo un 1 o un 2\nEstas son las opciones:\n1) Generar la representación en byte de un carácter\n2) Generar la representación en byte de una palabra\n"))
            verificacion=ord(opcion)
        opcion=int(opcion)
    if opcion==1:
        caracter=input("¡Has escogido convertir un caracter!\nIngresa tu caracter, recuerda que debe ser solo uno. Si quieres volver al menu principal presiona 11\n")
        var=(cuantosCaracters(caracter))
        while not(var):
            if numero==11:
                menu()
                var=True
            if var!=True:
                caracter=(input("¡Hey has colocado mas de un caracter!\nColoca solo uno\n"))
            var=(cuantosCaracters(caracter))
        ascci=ord(caracter)
        print(f"Aquí tienes la representación binaria de tu caracter ({caracter}):\n{convertirCaracter(ascci)}")
    if opcion==2:
        palabra=input("¡Has escogido convertir una palabra!\nIngresa tu palabra y ten en cuenta que se te pedirá ingresar la palabra nuevamente si colocas algun espacio ya sea inicial, intermedio o final.\nNo se validará que la palabra exista, solo que los caracteres sean letras\nSi quieres volver al menu principal presiona 11\n")
        var=False
        while not(palabraValida(palabra)):
            cuantosCaracters(palabra)
            if numero==11:
                menu()
                var=True
            if var!=True:
                palabra=input("La palabra ingresada no es válida, verifica que no hayas puesto ningun espacio o caracter especial.\nIngrsa nuevamente tu palabra: ")
        palabraConver=convertirPalabra(palabra)
        print(f"Aquí tienes la representación binaria de tu palabra ({palabra}):\n {palabraConver}")

def cuantosCaracters(caracteres):
    global numero
    numero=""
    contador=0
    for i in caracteres:
        if siNumeros(i)==True:
            contador+=1
    if contador==len(caracteres):
        for i in caracteres:
            numero=f"{numero}{i}"
        numero=int(numero)
    return(len(caracteres)==1)
menu()

