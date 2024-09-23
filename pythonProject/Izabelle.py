#soma de 2 números
'''
A= float(input("digite um número"))
B= float(input("digite um número"))

resultado= A + B
print("o resultado é", resultado,)

#resultado

N1= 10
N2= 3
N3= 8
N4= 2

numero = (10*3)-(8/2)
print("o resultado é", numero)2
'''
'''
#Condições

A= (float(input("digite um numero")))
B= (float(input("digite um numero")))
if(A>3)or(B>4):
    print("verdadeiro")

else:
    print("false")
'''

'''
#IMC
peso= (float(input("digite o seu peso")))
altura=(float(input("digite sua altura")))

IMC= peso/altura**2
print("o seu IMC é", IMC)

from colorama import Fore, Style, init
if (IMC < 18.5):
    print(f"{Fore.BLUE}Baixo Peso")

elif(IMC >= 18.5) and (IMC <= 24.9):
    print(f"{Fore.GREEN}Normal")

elif(IMC >= 25) and (IMC <= 29.9):
    print(f"{Fore.CYAN}Sobrepeso")

elif(IMC >= 30) and (IMC <= 34.9):
    print(f"{Fore.YELLOW}Obesidade")

elif(IMC >= 35) and (IMC <= 39.9):
    print(f"{Fore.RED}Obesidade mórbida")

else:
    print(f"{Fore.RED}Obesidade mórbida")

'''
"""
#raiz cúbica

A= float(input("digite um numero"))
resultado= A**(1/3)
print(resultado)
"""
'''
#juros composto

capital = float(input("digite o capital"))
juros= float(input("digite o juros"))
anos= float(input("digite os anos"))

calculo= capital*(1*juros/100)**anos
print(calculo)
'''
#verificação voto

'''
idade=int(input("digite sua idade"))

if idade>=18:
    print("voto obrigatorio")

elif idade <=17 and idade >=16:
    print("voto facultativo")

else:
    print("nao eleitor")
'''
"""
#Hora valida

hora=float(input("digite a hora"))
minuto=float(input("digite a minuto"))
segundo=float(input("digite a segundo"))

if(hora>0)and(hora<24)and(minuto<=59)and(segundo<=59):
    print("horario valido")

else:
    print("horario invalido")   
""""

#desconto de produto

quantidade= float(input("digite a quantidade de produtos"))
VU=float(input("digite o valor de cada unidade"))

if(quantidade>100)

