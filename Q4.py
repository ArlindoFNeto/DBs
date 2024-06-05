def get_n_int():
    while True:
        try:
            n = int(input("Informe um valor inteiro positivo: "))
            if n > 0:
                return n
        except:
            print("\tERRO: O valor deve ser inteiro: ")
        else:
            print("\tERRO: o valor deve ser positivo.")

for i in range(1, get_n_int()):
    if i%2 == 0:
        print(f"{i}")
