# Calculadora de IMC / IMC Calculator
# name: Luiz Gustavo de Medeiros
# Lógica e Programação (Anhanguera)
# 05/08/2023



""" Para esse trabalho foi usado a formula que encontrei
no website TuaSaude.

Para algumas sintaxes foi usado o google em conjunto à
um pré conhecimento inicial em Java.

[ENGLISH]
This is a Basic IMC calculator, it's all in portuguese because it's
for my college and it must be in PT/BR. The program will give 
user current IMC and if not normal, ideal weight will also
be given.
"""

print("\n\
Calculadora de IMC para Adultos \n")

peso = float(input("Informe seu peso (kg) exemplo: \"60.15\": "))
altura = float(input("Informe sua altura (m) (exemplo 1.78): "))

# Formula para descobrir o IMC e calcular max e min peso
imc = float(peso) / (float(altura) ** 2)
pesoIdealMin = 18.5 * altura ** 2
pesoIdealMax = 24.9 * altura ** 2

# Teste para descobrir em que nível de IMC usuário está
print("\nO seu IMC é: ", round(imc, 2))
print("Você está ", end="")
if (imc < 18.5):
    print("Abaixo do peso")
elif (imc < 24.9):
    print("com Peso Normal")
elif (imc < 29.9):
    print("com Sobrepeso")
elif (imc < 34.9):
    print("com Obesidade Grau 1")
elif (imc < 39.9):
    print("com Obesidade Grau 2")
else:
    print("\ncom Obesidade Grau 3")

# Teste para sugerir pesos ideais
if (imc < 18.5 or imc > 24.9):
    print("Seu peso ideal é de", round(pesoIdealMin, 2), "kg à",
          round(pesoIdealMax), "kg")
print("\n")

#  Seu peso ideal é: 25 a 29.9
# 25 = x / 1.70 ** 2
