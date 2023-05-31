def palabraValida(palabra):
    for i in palabra:
        if siLetras(i)!=True:
            return(False)
    return True


def siNumeros(i):
    if ord(i)>47 and ord(i)<57:
        return(True)
    return(False)

def siLetras(i):
    l=ord(i)
    if (l>=97 and l<=122) or (l>=65 and l<=90)or l== 225 or l== 233 or l== 237 or l== 243 or l== 250 or l== 193 or l== 201 or l== 205 or l== 211 or l== 218:
        return True
    return False

def convertirCaracter(ascci):
    binario = bin(ascci)[2:]
    return binario.zfill(8)

def convertirPalabra(palabra):
    palabraConver=""
    for i in palabra:
        binario=convertirCaracter(ord(i))
        palabraConver=f"{palabraConver} {binario}"
    return (palabraConver)