# salario= float(input("Qual o seu salário mensal? "))
# horas= float(input("Qual a quantidade de horas trabalhadas na semana? "))
# mensal= (horas) * 4
# print (f"O total de horas trabalhadas no mês é: {mensal}")
# salariohora= (divisao,salario/horas)
# print (f"O seu salário por hora é de: {salariohora}  ")

salario_mensal= float(input("Qual o seu salário mensal? "))
horas_semana= float(input("Qual a quantidade de horas trabalhadas na semana? "))
horas_mes= horas_semana*4
salariohora= salario_mensal/horas_mes
print(salariohora)