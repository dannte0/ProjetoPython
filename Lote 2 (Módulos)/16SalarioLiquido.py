#Algoritmo ESTSEQ_LT02_16
#Declarar.
horas_trabalhadas: int = 0
valor_hora: int = 0
desconto: float = 0.0
dependentes: int = 0
salario_bruto: float = 0.0
salario_liquido: float = 0.0

#Início.
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))
valor_hora = int(input('Digite o valor pago por hora: '))
desconto = float(input('Digite o valor percentual a ser descontado: '))
dependentes = int(input('Digite a quantidade de dependentes: '))
salario_bruto = horas_trabalhadas * valor_hora
salario_liquido = salario_bruto - (salario_bruto * desconto/100) + dependentes * 100
print('O salario líquido é: R$', salario_liquido)

#Fim.