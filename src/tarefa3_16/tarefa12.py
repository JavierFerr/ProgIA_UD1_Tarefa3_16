#Escribir un programa que almacene a cadea de caracteres contrasinal nunha variable, terá un valor predifinido.

#Logo debe preguntar ao usuario polo contrasinal e imprima por pantalla se o contrasinal introducido polo usuario coincide ou non coa variable.
# #Non importan as maiúsculas e minúsculas.

if __name__ == '__main__':
    CONTRASINAL = "abc123."
    print("Introduzca a contrasinal")
    con = input().lower()
    if con == CONTRASINAL:
        print("Contrasinal correcta")
    else:
        print("Contrasinal erronea")
