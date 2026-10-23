if __name__ == '__main__':
    print('Introduce un télfono con este formato "prefixo-número-extension"')
    telefono = input()

    print(str(telefono[4:-3]))
