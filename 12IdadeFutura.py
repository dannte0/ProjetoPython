#Algoritmo ESTSEQ_LT01_12
#Declarar.
ano_nascimento: int = 0
ano_atual: int = 0
idade: int = 0
idade_futura: int = 0

#Início.
ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = ano_atual - ano_nascimento
idade_futura = idade + 17
print('Idade atual:', idade)
print('Idade daqui a 17 anos:', idade_futura)

#Fim.