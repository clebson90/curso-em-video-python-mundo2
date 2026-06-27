#36-
casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
ano = int(input("Em quantos anos vai pagar? "))
ano = ano * 12
limite = salario * 0.30
prestacao = casa/ano
if prestacao > limite:
    print("emprestimo negado")
elif prestacao <= limite:
    print("emprestimo concedido")

#37-
num = int(input("Digite um número inteiro! "))
print('''Escolha uma das bases para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input("Qual sua opção? "))
if opcao == 1:
    print(f"o número é {num} convertido ficou {bin(num)[2:]}")
elif opcao == 2:
     print(f"o número é {num} convertido ficou {oct(num)[2:]}")
elif opcao == 3:
     print(f"o número é {num} convertido ficou {hex(num)[2:]}")
else:
    print("opção inválida")

#38-
num1 = int(input("Digite um número! "))
num2 = int(input("Digite outro número! "))
if num1 > num2:
    print(f"O primeiro valor {num1} é maior")
elif num2 > num1:
    print(f"O segundo valor {num2} é maior")
else:
    print("não existe valor maior, os dois números são iguais")

#39-
from datetime import date
ano = date.today().year
nasc = int(input("Qual seu ano de nascimento? "))
alistamento = ano - nasc
if alistamento < 18:
    tempo_restante = 18 - alistamento
    print(f"a idade é {alistamento} \n muito novo pra se alistar! \n falta {tempo_restante} anos pro alistamneto!")
elif alistamento == 18:
    print(f"a idade é {alistamento} \n está na idade pra se alistar! \n se aliste agora!")
elif alistamento > 18:
    tempo_restante = alistamento - 18 
    print(f" a idade é {alistamento} \n já passou do tempo de se alistar! \n passou {tempo_restante} anos do alistamento! \n se aliste agora!")

#40-
nota1 = float(input("Qual a sua primeira nota? "))
nota2 = float(input("Qual a sua segunda nota? "))
media = (nota1 + nota2) / 2
if media < 5.0:
    print("REPROVADO")
elif media >= 5.0 and media <= 6.9:
    print("RECUPERAÇÃO")
elif media >= 7.0:
    print("APROVADO")

#41-
from datetime import date
ano = date.today().year
nasc = int(input("Qual seu ano de nascimento? "))
idade = ano - nasc
if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 25:
    print("SÊNIOR")
elif idade > 25:
    print("MASTER")

#42-
l1 = int(input("qual o comprimento? "))
l2 = int(input("qual o comprimento? "))
l3 = int(input("qual o comprimento? "))
if l1 + l2 > l3 and l2 < l1 + l3 and l3 < l1 +l2:
    print("é um triangulo")
    if l1 == l2 and l2 == l3:
        print("Equilátero")
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("não é um triangulo")

#43-
from math import trunc
peso = float(input("Qual seu peso?"))
altura = float(input("Qual sua altura?"))
imc = peso/(altura**2)
print(f"seu peso é {peso} \n sua altura é {altura} ")
print(f"seu imc é: {trunc(imc)}")
if imc < 18.5:
    print("você está abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("você está no peso ideal")
elif imc >= 25 and imc < 30:
    print("você está sobrepeso")
elif imc >= 30 and imc < 40:
    print("você está obeso")
elif imc >= 40:
    print("você está com obsidade morbida")

#44-
produto = float(input("Qual o valor do produto? "))
condicao_de_pagamento = input("Qual a condição de pagamneto? \n à vista dinheiro? \n à vista cartão? \n 2x no cartão? \n 3x ou mais no cartão? ")
if condicao_de_pagamento == "à vista dinheiro":
    desconto = produto * 0.9
    print(f"o preço final com desconto ficou {desconto}")
elif condicao_de_pagamento == "à vista cartão":
    desconto = produto * 0.95
    print(f"o preço final com desconto ficou {desconto}")
elif condicao_de_pagamento == "2x no cartão":
    print(f"não tem desconto, preço final {produto}")
elif condicao_de_pagamento == "3x ou mais no cartão":
    aumento = produto * 1.2
    print(f"o preço final com juros ficou {aumento}")

#45-
import random
jokenpo = ("pedra", "papel", "tesoura")
computador = random.choice(jokenpo)
usuario = input("pedra? papel? tesoura? \n").strip().lower()
if usuario not in jokenpo:
    print("opção inválida. Digite: pedra, papel ou tesoura")
elif computador == usuario:
    print(f"deu empate, {computador} e {usuario}")
elif (usuario == "pedra" and computador == "tesoura") or \
     (usuario == "papel" and computador == "pedra") or \
     (usuario == "tesoura" and computador == "papel"):
    print(f"vc ganhou, {computador} e {usuario}")
else:
    print(f"vc perdeu, {computador} e {usuario}")

#46-
from time import sleep
for c in range (10, 0 , -1):
    print(c)
    sleep(1)
print("Boom")

#47-
for c in range (2, 51, 2):
    print(c)
print("Fim")

#48-
soma = 0
cont = 0
for c in range (1 , 500 , 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print(f"a soma de todos os {cont} valores solicitados é {soma}")

#49-
n = int(input("digite o numero pra ver sua tabuada! "))
for c in range (0 , 11):
    r = n * c
    print(f"{n} X {c} = {r}")

#50-
s = 0
cont = 0
for c in range (0 , 6):
    n = int(input("digite um número! "))
    cont = cont + 1
    if n % 2 == 0:
        s = s + n
print(f"vc digitou {cont} valores e a soma dos números pares é {s}")

#51-
primeiro_termo = int(input("qual o primeiro termo? "))
razao = int(input("qual a razão? "))
decimo = primeiro_termo + (11 - 1) * razao
for c in range (primeiro_termo , decimo , razao):
    print(c)
print("fim!")

#52-
num = int(input("Digite um número! "))
total = 0
for c in range (1 , num + 1):
    if num % c == 0:
        total = total + 1
if total == 2:
    print(f"o número {num} é primo")
else:
    print(f"o número {num} não é primo")

#53-
frase = input("Digite uma frase? ").strip().upper()
palvra = frase.split()
junto = "".join(palvra)
inverso = ""
for letra in range (len(junto) -1 , -1 , -1):
    inverso = inverso + junto[letra] 
print(f"o inverso de {junto} é {inverso}")
if inverso == junto:
    print("é um políndromo")
else:
    print("não é um palíndromo")

#54-
from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for c in range (0 , 7):
    ano = int(input("Qual seu ano de nascimento? "))
    if ano_atual - ano >= 18:
        maior = maior + 1
    if ano_atual - ano < 18:
        menor = menor + 1
print(f" a quantidades de pessoas maiores de idade são {maior} \n a quantidades de pessoas menores de idade são {menor}")

#55-
maior = 0
menor = 0
for c in range (0 , 5):
    p = float(input("Qual o seu peso? "))
    if c == 0:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f"o maior peso é {maior} e o menor é {menor}")

#56-
soma = 0
media = 0
maioridade = 0
nomemaisvelho = ""
mulher = 0
for c in range (1 , 5):
    print(f"{c}ª PESSOA")
    nome = input("Qual o seu nome? ").strip().lower()
    s = input("Qual seu sexo? H/M! ").strip().upper()
    idade = int(input("Qual sua idade? "))
    soma = soma + idade
    if c == 0 and s == "H":
        maioridade = idade
    if s == "H" and idade > maioridade:
        maioridade = idade
        nomemaisvelho = nome
    if s == "M" and idade < 20:
        mulher = mulher + 1
media = soma / 4
print(f"A média das idades é {media} \nO homem mais velho é {nomemaisvelho} \nE a quantidade de mulheres com menos de 20 é {mulher}")

#57-
c = input("Qual o seu sexo? M/F! ").strip().upper()[0]
while c != "M" and c != "F":
    print("Você digitou errado! digite M ou F!")
    c = input("Digite novamente! M/F! ").strip().upper()[0]
print(f"Seu sexo é {c}")

#58-
import random
n_sorteado = random.randint(1 , 10)
palpites = 0
acertou = False
while not acertou:
    n = int(input("Digite um numero! "))
    palpites = palpites + 1
    if n == n_sorteado:
        acertou = True
    else:
        if n > n_sorteado:
            print("O número sorteado é menor!")
        elif n < n_sorteado:
            print("O número sorteado é maior!")
print(f"Você acertou o número sorteado era {n_sorteado} e você tentou {palpites} vezes")

#59-
n = int(input("Digite um número! "))
n2 = int(input("Digite outro número! "))
opcao = 0
while opcao != 5:
    print("Qual opção você quer?\n"
    "[ 1 ] Somar\n" 
    "[ 2 ] Multiplicar\n"
    "[ 3 ] Maior\n"
    "[ 4 ] Novos números\n"
    "[ 5 ] sair do programa\n")
    opcao = int(input("Qual sua opção? "))
    if opcao == 1:
        soma = n + n2
        print(f"A soma é {soma}\n")
    elif opcao == 2:
        multiplicar = n * n2
        print(f"A multiplicação é {multiplicar}\n")
    elif opcao == 3:
        if n > n2:
            print(f"O primeiro valor {n} é maior que {n2}\n")
        else:
            print(f"O segundo valor {n2} é maior que {n}\n")
    elif opcao == 4:
        n = int(input("Digite um novo número! "))
        n2 = int(input("Digite outro número! \n"))
print("Fim do programa")

#60-
n = int(input("digite um número! "))
r = 1
while n > 0:
    print(f"{n}", end = " ")
    print("X" if n > 1 else "=", end = " ")
    r = r * n
    n = n - 1
print(r)

#61-
n = int(input("Digite um número! "))
r = int(input("Qual a razão"))
c = 0
while c < 10:
    print(n)
    n = n + r
    c = c + 1

#62-
n = int(input("Digite um número! "))
r = int(input("Qual a razão? "))
c = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c < total:
        print(n , end = " ")
        n = n + r
        c = c + 1
    mais = int(input("\nQuantos termos a mais você quer ver? "))
print(f"O programa mostrou {total} termos\nFIM")

#63-
n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print(t1 , t2 , end = " ")
c = 2
while c < n:
    t3 = t1 + t2
    print(t3 , end = " ")
    t1 = t2
    t2 = t3
    c = c + 1

#64-
soma = 0
total = 0
n = 0
n = int(input("Digite um número [999 para parar]: "))
while n != 999:
    total = total + 1
    soma = soma + n
    n = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {total} números e a soma entre eles foi {soma}")

#65-
total = 0
media = 0
soma = 0
maior = 0
menor = 0
condicao = "S"
while condicao == "S":
    n = int(input("Digite um número! "))
    total += 1
    soma += n
    if total == 1:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    condicao = input("Quer continuar? [S/N] ").strip().upper()
media = soma / total
print(f"Você digitou {total} números e a média foi {media}\nO maior valor foi {maior} e o menor valor foi {menor}")

#66-
c = 0
n = 0
s = 0
while True:
    n = int(input("digite um número! [999 para parar]: "))
    if n == 999:
        break
    c += 1
    s += n
print(f"A soma dos {c} valores foi {s}!")

#67-
c = 0
n = 0
while True:
    n = int(input("Qual tabuada você quer ver? "))
    if n < 0:
        break
    for c in range (1 , 11):
        print(f"{n} X {c} = {n * c}")
        c += 1
print("Acabou")

#68-
from random import randint
c = 0
while True:
    n = int(input("Dgite um número! "))
    computador = randint(0 , 10)
    s = n + computador
    par_impar = " "
    while par_impar not in "PI":
        par_impar = input("Par ou Ímpar? [P/I]! ").strip().upper()[0]
    if par_impar == "P":
        if s % 2 == 0:
            print(f"Você jogou {n} e o computador {computador}. Total somando deu {s}.\nDeu par!\nVocê Ganhou!\nVamos continuar...")
            c += 1
        else:
            print(f"Você jogou {n} e o computador {computador}. Total somando deu {s}. Deu Ímpar!\nVocê PERDEU")
            break
    elif par_impar == "I":
        if s % 2 == 1:
            print(f"Você jogou {n} e o computador {computador}. Total somando deu {s}. Deu Ímpar!\nVocê Ganhou!\nVamos continuar")
            c += 1
        else:
            print(f"Você jogou {n} e o computador {computador}. Total somando deu {s}. Deu Par!\nVocê PERDEU")
            break
print(f"GAME OVER! Você venceu {c} vezes!")

#69-
maior = 0
h = 0
m = 0
while True:
    print("-"*20)
    print("CADASTRE UMA PESSOA")
    print("-"*20)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "HM":
        sexo = input("Sexo: [H/M] ").strip().upper()[0]
    print("-"*20)
    condicao = " "
    while condicao not in "SN":
        condicao = input("Quer continuar? [S/N] ").strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == "M" and idade < 20:
        m += 1
    if sexo == "H":
        h += 1
    if condicao == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {maior}\nAo todo temos {h} homens cadastrados\nE temos {m} mulheres com menos de 20 anos")

#70-
print("-"*20)
print("LOJA SUPER BARATÃO")
print("-"*20)
s = 0
menor = 0
c1000 = 0
c = 0
pr = ""
while True:
    produto = input("Nome do Produto: ")
    preco = float(input("Preço: "))
    condicao = " "
    c += 1
    s += preco
    menor = preco
    if preco > 1000:
        c1000 += 1
    if c == 1:
        menor = preco
        pr = produto
    else:
        if preco < menor:
            menor = preco
            pr = produto
    while condicao not in "SN":
        condicao = input("Quer continuar? [S/N]").strip().upper()[0]
    if condicao == "N":
        break
print(f"FIM DO PROGRAMA\nO total da compra foi {s}\nTemos {c1000} produtos custando mais de R$1000 reais\nO produto mais barato foi {pr} que custa R${menor}" )

#71-
print("-"*20)
print("BANCO CEV")
print("-"*20)
valor = int(input("Qual valor você quer sacar? R$"))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f"Total de {totalced} células de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print("="*20)
print("Volte sempre ao BANCO CEV! tenha um bom dia!")