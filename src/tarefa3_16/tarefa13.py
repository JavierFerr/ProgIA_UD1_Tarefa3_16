#Escribir un programa que pida ao usuario dous números, dividendo e divisor.

#Logo debe amosar por pantalla a súa división, aínda que se o divisor é 
#cero debes amosar unha mensaxe de erro (do estilo non se pode dividir por 0).

if __name__ == '__main__':
    print("Introduzca dividendo e divisor")

    dividendo,divisor = int(input()),int(input())

    resul = dividendo/divisor

    print(f"Resultado: {resul}")
