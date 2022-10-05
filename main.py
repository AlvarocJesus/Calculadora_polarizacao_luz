# Estamos utilizando o sistema internacional de medidas

# Constantes:
from math import cos
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

""")


def message():
  input("""
-------------------------------------------
Digite ENTER para continuar com os cálculos
-------------------------------------------
""")

def calcPolarizai0(ang1, ang2, ang3, i0):
  i1 = i0/2
  # Está dando erro nesta linha de baixo "unsupported operand type(s) for *: 'float' and 'function'"
  i2 = ((cos((ang2 - ang1)*PI/180))**2)*i1 
  i3 = ((cos((ang3 - ang2)*PI/180))**2)*i2 
  if i3 == i2:
    pass;
  

def calcPolarizai1(ang1, ang2, ang3, i1):
  i0 = 2*i1
  # Está dando erro nesta linha de baixo "unsupported operand type(s) for *: 'float' and 'function'"   ¯\_(ツ)_/¯ ???
  i2 = i1*((cos((ang2 - ang1)*PI/180))**2)
  i3 = i2*((cos((ang3 - ang2)*PI/180))**2)
  if i3 == i2:
    pass;

def calcPolarizai2(ang1, ang2, ang3, i2):
  # Está dando erro nesta linha de baixo "unsupported operand type(s) for *: 'float' and 'function'"  ¯\_(ツ)_/¯ ???
  i1 = i2/(cos((ang2 - ang1)*PI/180)**2)
  i0 = 2*i1
  i3 = i2*((cos((ang3 - ang2)*PI/180))**2) 
  if i3 == i2:
    pass;

def calcPolarizai3(ang1, ang2, ang3, i3):
  # Está dando erro nesta linha de baixo "unsupported operand type(s) for *: 'float' and 'function'"  ¯\_(ツ)_/¯ ???
  i2 = i3/(cos((ang3 - ang2)*PI/180)**2)
  i1 = i2/(cos((ang2 - ang1)*PI/180)**2)
  i0 = 2*i1
  pass;


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
    ang3 = ang2 
    i0 = float(input("Intensidade inicial (i0) [W/m^2]: "))
    calcPolarizai0(ang1, ang2, ang3, i0)
    message()
  elif option == '2':
    ang1 = float(input("Digite o ângulo do primeiro polarizador [em graus]:"))
    ang2 = float(input("Digite o ângulo do segundo polarizador [em graus]:"))
    ang3 = ang2 
    i1 = float(input("Intensidade (i1) [W/m^2]: "))
    calcPolarizai1(ang1, ang2, ang3, i1)
    message()
  elif option == '3':
    ang1 = float(input("Digite o ângulo do primeiro polarizador [em graus]:"))
    ang2 = float(input("Digite o ângulo do segundo polarizador [em graus]:"))
    ang3 = ang2 
    i2 = float(input("Intensidade (i2) [W/m^2]: "))
    calcPolarizai2(ang1, ang2, ang3, i2)
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
