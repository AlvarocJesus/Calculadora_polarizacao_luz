# Estamos utilizando o sistema internacional de medidas

# Constantes:
from math import cos, pi
from time import sleep
from xml.etree.ElementTree import PI

# Exibe integrantes dos grupos
print("""
----------INTEGRANTES------------
Alvaro Coelho Jesus 22.221.002-3
Fernando Shiraishi 22.221.014-8
Vinicius Alves Pedro 22.221.036-1
---------------------------------
""")

# Exibe descrição do projeto:
print("""
Este código desenvolvido na linguagem Python explora o tema da física óptica da polarização da luz. 
Para a utilização do programa, primeiramente deve-se escolher entre as opções mostradas no menu, respondendo 
com o número correspondente ao cálculo desejado, e então as entradas requeridas, que variam de acordo
com a opção. Desse modo, o programa é capaz de calcular a intensidade em todas as etapas com dois a 
três polarizadores.
""")


def message():
  input("""
-------------------------------------------
Digite ENTER para continuar com os cálculos
-------------------------------------------
""")

def calcPolarizai0(ang1, ang2, ang3, i0):
  if ang1==90: ang1 = cos((ang1*pi)/180)
  else: ang1=ang1

  i1 = i0/2
  i2 = (cos(((ang2 - ang1)*pi)/180)**2) * i1
  i3 = (cos(((ang3 - ang2)*pi)/180)**2) * i2
  if ang3 == 0:
    print(f'Intensidade 1: {i1:.3}\nIntensidade 2: {i2:.3}')
  else:
    print(f'Intensidade 1: {i1:.3} W/m^2\nIntensidade 2: {i2:.3} W/m^2\nIntensidade 3: {i3:.3} W/m^2')
  

def calcPolarizai1(ang1, ang2, ang3, i1):
  if ang1==90: ang1 = cos((ang1*pi)/180)
  else: ang1=ang1

  i0 = 2*i1
  i2 = i1*((cos((ang2 - ang1)*pi/180))**2)
  i3 = i2*((cos((ang3 - ang2)*pi/180))**2)
  if ang3 == 0:
    print(f'Intensidade inicial: {i0:.3}\nIntensidade 2: {i2:.3}')
  else:
    print(f'Intensidade inicial: {i0:.3} W/m^2\nIntensidade 2: {i2:.3} W/m^2\nIntensidade 3: {i3:.3} W/m^2')

def calcPolarizai2(ang1, ang2, ang3, i2):
  if ang1==90: ang1 = cos((ang1*pi)/180)
  else: ang1=ang1

  i1 = i2/(cos((ang2 - ang1)*pi/180)**2)
  i0 = 2*i1
  i3 = i2*((cos((ang3 - ang2)*pi/180))**2) 
  if ang3 == 0:
    print(f'Intensidade 0: {i0:.3}\nIntensidade 1: {i1:.3}')
  else:
    print(f'Intensidade inicial: {i0:.3} W/m^2\nIntensidade 1: {i1:.3} W/m^2\nIntensidade 3: {i3:.3} W/m^2')

def calcPolarizai3(ang1, ang2, ang3, i3):
  if ang1==90: ang1 = cos((ang1*pi)/180)
  else: ang1=ang1

  i2 = i3/(cos((ang3 - ang2)*pi/180)**2)
  i1 = i2/(cos((ang2 - ang1)*pi/180)**2)
  i0 = 2*i1
  print(f'Intensidade inicial: {i0:.3} W/m^2\nIntensidade 1: {i1:.3} W/m^2\nIntensidade 2: {i2:.3} W/m^2')

while True:
  print("\n--------------------Menu--------------------")
  print(""" Selecione sua opção desejando calcular com:

1 - I0 e 2 Polarizadores
2 - I1 e 2 Polarizadores
3 - I2 e 2 Polarizadores

4 - I0 e 3 Polarizadores
5 - I1 e 3 Polarizadores
6 - I2 e 3 Polarizadores
7 - I3 e 3 Polarizadores

0 - Sair
  """)
  option = input()

  if option == '0':
    sleep(1)
    print('Até a proxima... (^.^) 👉️👈️')
    sleep(1)
    break
  elif option == '1':
    ang1 = float(input("Digite o ângulo do primeiro polarizador [em graus]:"))
    ang2 = float(input("Digite o ângulo do segundo polarizador [em graus]:"))
    i0 = float(input("Intensidade inicial (i0) [W/m^2]: "))
    calcPolarizai0(ang1, ang2, 0, i0)
    message()
  elif option == '2':
    ang1 = float(input("Digite o ângulo do primeiro polarizador [em graus]:"))
    ang2 = float(input("Digite o ângulo do segundo polarizador [em graus]:"))
    i1 = float(input("Intensidade (i1) [W/m^2]: "))
    calcPolarizai1(ang1, ang2, 0, i1)
    message()
  elif option == '3':
    ang1 = float(input("Digite o ângulo do primeiro polarizador [em graus]:"))
    ang2 = float(input("Digite o ângulo do segundo polarizador [em graus]:"))
    i2 = float(input("Intensidade (i2) [W/m^2]: "))
    calcPolarizai2(ang1, ang2, 0, i2)
    message()
  elif option == '4':
    ang1 = float(input("Digite o ângulo do primeiro polarizador [em graus]:"))
    ang2 = float(input("Digite o ângulo do segundo polarizador [em graus]:"))
    ang3 = float(input("Digite o ângulo do terceiro polarizador [em graus]:"))
    i0 = float(input("Intensidade inicial (i0) [W/m^2]: "))
    calcPolarizai0(ang1, ang2, ang3, i0)
    message()
  elif option == '5':
    ang1 = float(input("Digite o ângulo do primeiro polarizador [em graus]:"))
    ang2 = float(input("Digite o ângulo do segundo polarizador [em graus]:"))
    ang3 = float(input("Digite o ângulo do terceiro polarizador [em graus]:"))
    i1 = float(input("Intensidade (i1) [W/m^2]: "))
    calcPolarizai1(ang1, ang2, ang3, i1)
    message()
  elif option == '6':
    ang1 = float(input("Digite o ângulo do primeiro polarizador [em graus]:"))
    ang2 = float(input("Digite o ângulo do segundo polarizador [em graus]:"))
    ang3 = float(input("Digite o ângulo do terceiro polarizador [em graus]:"))
    i2 = float(input("Intensidade (i2) [W/m^2]: "))
    calcPolarizai2(ang1, ang2, ang3, i2)
    message()
  elif option == '7':
    ang1 = float(input("Digite o ângulo do primeiro polarizador [em graus]:"))
    ang2 = float(input("Digite o ângulo do segundo polarizador [em graus]:"))
    ang3 = float(input("Digite o ângulo do terceiro polarizador [em graus]:"))
    i3 = float(input("Intensidade (i3) [W/m^2]: "))
    calcPolarizai3(ang1, ang2, ang3, i3)
    message()
  else:
    print("Por favor, selecione uma opção disponível! 😉 ")
    message()
