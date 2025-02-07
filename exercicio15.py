quanto_hora = float(input("quanto voce ganha por hora?"))
quanto_dias = int(input("quantos dias trabalhou no mes"))
quantas_horas = int (input("quantas horas voce trabalha no dia?"))
total_salario = (quanto_dias * quantas_horas) * quanto_hora
imposto = (11 * total_salario) / 100
inss = (8 * total_salario) / 100
sindicato = (5 * total_salario) / 100
descontos = imposto + inss + sindicato
print ("salario bruto:", total_salario)
print ("salario com imposto:", total_salario - imposto)
print ("salario com inss:", total_salario - inss)
print ("salario liquido:", total_salario - descontos )