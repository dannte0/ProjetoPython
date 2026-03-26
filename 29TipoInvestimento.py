#Algotimo ESTDEC_LT01_29
#Declarar.
tipo_investimento: int = 0
valor: float = 0.0

#Início.
def calcula_investimento(ti, v):
    montante: float = 0.0
    if(ti == 1):
        montante = v + v * 0.03
        print("Valor corrigido: R$", montante)
    elif(ti == 2):
        montante = v + v * 0.05
        print("Valor corrigido: R$", montante)
    else:
        print("Tipo de investimento invalido.")

def main():
    global tipo_investimento
    global valor
    tipo_investimento = int(input("Digite o tipo de investimento (1 - Poupanca) (2 - Renda fixa):"))
    valor = float(input("Digite o valor a ser investido: "))
    calcula_investimento(tipo_investimento, valor)
    
if(__name__ == '__main__'):
    main()
#Fim.