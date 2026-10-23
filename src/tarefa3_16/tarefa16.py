#Os alumnos dun curso dividíronse en dous grupos A e B de acordo ao sexo e o nome.

#    O grupo A esta formado polas mulleres cun nome anterior á M e os homes cun nome posterior á N
#    O grupo B esta formado polo resto.

#Escribir un programa que pregunte ao usuario o seu nome e sexo, e mostre por pantalla o grupo que lle corresponde.

#Ten en conta que os operadores maior que menor que tamén funcionan con cadenas de caracteres.


if __name__ == '__main__':
    print("Introduzca nome e sexo(H/M)")
    nome,sexo = input(),input().upper()
    letran = nome[0]

    if (sexo == "M" and letran < "m") or (sexo == "H" and letran > "n"):
        print("Grupo A")
    elif (sexo == "M" and letran >= "m") or (sexo == "H" and letran <= "n"):
        print("Grpo B")
    else:
        print("Formato incorrecto")


#    if sexo == "M":
#        if letran < "m":
#            print("Grupo A")
#        else:
#            print("Grupo B")
#    elif sexo == "H":
#        if letran > "n":
#            print("Grupo A") 
#        else:
#            print("Grupo B")
#    else:
#        print("Campo sexo mal introducido")