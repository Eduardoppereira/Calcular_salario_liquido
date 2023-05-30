def calcular_salario():
    valor_hora = float(input("Informe o valor da sua hora de trabalho: "))
    horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
    
    salario_bruto = valor_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - ir - inss - sindicato
    
    print("Salário Bruto: R$", salario_bruto)
    print("Imposto de Renda (11%): R$", ir)
    print("INSS (8%): R$", inss)
    print("Sindicato (5%): R$", sindicato)
    print("Salário Líquido: R$", salario_liquido)


calcular_salario()