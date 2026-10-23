#Escribir un programa que pregunte ao usuario a súa idade e mostre por pantalla se é maior de idade ou non.
if __name__ == '__main__':
    print("Introduzca a sua idade:")
    idade = int(input())

    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")