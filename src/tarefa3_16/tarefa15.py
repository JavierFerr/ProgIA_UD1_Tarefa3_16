#Para tributar un determinado imposto débese ser maior de 16 anos e ter uns ingresos iguais ou superiores a 1000 € mensuais.

#Escribir un programa que pregunte ao usuario a súa idade e os seus ingresos mensuais e mostre por pantalla se o usuario ten que tributar ou non.

if __name__ == '__main__':

    print("Introduzca idade e ingresos")

    idade,ingresos = int(input()),int(input())

    if idade >= 16:
        if ingresos > 1000:
            print("Felicidades debe tributar a Hacienda")

        else:
            print("Ingresos minimos non alcanzados")

    else:
        print("Idade minima no alcanzada")