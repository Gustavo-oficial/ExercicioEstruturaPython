# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xjlIJ5NfPl8ztT65aPqyMCFvAlxE-PPh
"""

higherNumber = float('-inf')

for index in range(5):
  currentNumber = float(input("Digite o  numero: "))
  if currentNumber > higherNumber:
    higherNumber = currentNumber

print(f"Maior número é {higherNumber}")

for index in range(2000):
  if (index > 1000 and index < 2000) and (index % 11 == 2):
    print(f"Número {index} ta dentro")

previousNumber = float(0)

for index in range(5):
  currentNumber = float(input("Digite o  numero: "))
  previousNumber += currentNumber

print(f"Soma total dos numeros é {previousNumber}")
print(f"Média é de {previousNumber / 5}")

number = int(input("Digite o numero: "))

for index in range(10):
  increment = index + 1
  print(f"{increment} X {number} = {number * (increment)}")

number = int(input("Digite o numero: "))

for index in range(10):
  increment = index + 1
  print(f"{increment} X {number} = {number * (increment)}")

max = int(10)

for first in range(max):
  indice = first + 1
  number = max - (max - indice)
  print(f"Tabuada do {number}")
  for second in range(10):
    primary = second + 1
    print(f"{primary} x {number} = {primary * number}")

for index in range(1, 21):
    print(index)

for secondIndex in range(1, 21):
    print(secondIndex, end=" ")

for index in range(50):
  if (index % 2) != 0:
     print(index)

number1 = int(input("Digite o numero: "))
number2 = int(input("Digite o numero: "))

for index in range(number1 + 1, number2):
  print(index, end=" ")

faturamentoLojaB = 5400
faturamentoLojaA = float(0)

for i in  range(5):
  cliente = float(input("Quanto cliente gastou? "))
  faturamentoLojaA += cliente

print(f"Faturamento loja A foi de R$ {faturamentoLojaA}")

if faturamentoLojaA > faturamentoLojaB:
  print(f"Diferença entre a loja A e a loja B foi de R$ {faturamentoLojaA - faturamentoLojaB} para a loja A")
else:
  print(f"Diferença entre a loja A e a loja B foi de R$ {faturamentoLojaB - faturamentoLojaA} para a loja B")

impar = int(0)
par = int(0)

for i in range(10):
  inteiro = int(input("Digite um numero inteiro: "))
  for ii in range(inteiro):
    if (ii % 2) != 0:
      impar+=1
    elif (ii % 2) == 0:
      par+=1

print(f"Par: {par} Impares: {impar}")

salario = 1400
anosTrabalhados = (2024 - 1995)
aumento = 0.015
percentualFixo = 1

for i in range(anosTrabalhados):
  salario *= 1 + aumento
  aumento *= 2
  print(f"Salario atual é de {salario}")

for i in range(999):
  nota = int(input("Digite um numero "))
  if nota > 10 and nota > 0:
    print("Valor invalido")
  else:
    break

base = int(input("Digite o valor base "))
expoente = int(input("Digite o valor expoente "))
result = 0

for i in range(expoente):
  if i == 0:
    result = base
  else:
    result *= base

print(f"{result}")