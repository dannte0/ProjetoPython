#Algotimo ESTDEC_LT01_23
#Declarar.
a: int = 0
b: int = 0
c: int = 0
d: int = 0

#Início.
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))

if(d > c):
    print("Em ordem crescente: ", a, b, c, d)
elif(d > a and d < b):
    print("Em ordem crescente: ", a, d, b, c)
elif(d > b and d < c):
    print("Em ordem crescente: ", a, b, d, c)
elif(d < a):
    print("Em ordem crescente: ", d, a, b, c)
else:
    print("Igual a um dos valores")

#Fim.