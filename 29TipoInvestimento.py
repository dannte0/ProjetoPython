#Algotimo ESTDEC_LT01_29
#Declarar.
tipo_investimento: int = 0
valor: float = 0.0
montante: float = 0.0

#Início.
tipo_investimento = int(input("Digite o tipo de investimento (1 - Poupanca) (2 - Renda fixa):"))
valor = float(input("Digite o valor a ser investido: "))

if(tipo_investimento == 1):
    montante = valor + valor * 0.03
    print("Valor corrigido: R$", montante)
elif(tipo_investimento == 2):
    montante = valor + valor * 0.05
    print("Valor corrigido: R$", montante)
else:
    print("Tipo de investimento invalido.")
    
#Fim.