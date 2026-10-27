def imprime ():
    print("a")

def a(texto,/ , * , num = 2, punto = "."):
    return (str(num) + punto + " " + texto)

def numeros(*sinNom,**conNom):
    print(str(sinNom) + str(conNom))