#Algotimo ESTDEC_LT01_22
#Declarar.
a: int = 0
b: int = 0

#Início.
def verifica_maior():
    global a
    global b
    if(a < b):
        print("Em ordem crescente:", a, b)
    elif(a > b):
        print("Em ordem crescente:", b, a)
    else:
        print("Valores iguais")

def main():
    global a
    global b
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    verifica_maior()
    
if(__name__ == '__main__'):
    main()
#Fim.