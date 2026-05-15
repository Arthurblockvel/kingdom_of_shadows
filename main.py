import random
import time
# ! dicionarios sao usados quando queremos mais de um atributo em uma variavel
# ! usamos a estrutura de chaves com o nome do atributo dois pontos e o valor que queremos
print()
print(" esse eo jogo kingdom of shadows")

print("ola grande cavalheiro")
time . sleep (1)
print()
print("nesse jogo voce ira salvar um reino entre as trevas")
print(" seu personagem eo draven")
draven = {
    "nome" : "draven",
     "hp" :110,
     "dano_base" : 15
}
print()
print(" o inimigo principal e a sombra")
print()
sombra = {
"nome" : "sombra",
"hp" : 80,
"dano_base" : 10
    }

print (" ataques do sombra 1 soco 2 aranhar 3 assustar ")
print("1 soco tira 10 de hp")
print(" aranhar tira 18 de hp")
print("assustar causa um debuff de 28% de dano")
print(" voce atacara primeiro por que voce é mais rapido do que seu inimigo")
print("draven tem tres opçoes de ataque escolha")
print("escolha 1 se voce quer usar corte 2 se voce quer usar multiplos cortes digite 3 se voce quer usar corte sagrado ")
print("1 = corte tira 15 de hp")
print("2 = multiplos cortes tira 24 de hp")
print("3 = corte sagrado tira 35 de hp e deixa o inimigo sangrando")
ataque =  input("digite 1,2,3 para qual ataque voce utilizara ")
print()
if ataque =="1":
    print(" voce usou corte voce tirou 15 de hp")
elif ataque =="2":
    print("voce usou multiplos cortes voce tirou 24 de hp")
elif ataque == "3":
    print("voce usou corte sagrado voce tirou 35 de hp e deixou seu inimigo sangrando")
print()
print("agora a sombra ira atacar")
print()
print("sombra usou aranhar tirou 18 de hp")
print()
num_round = 0
rounds_sangramento = 0
while draven["hp"] > 0 and sombra["hp"] > 0:
    num_round += 1 # num_round = num_round + 1
    print()
    print(f"---------- ROUND {num_round}----------")
print()
ataque =  input("digite 1,2,3 para qual ataque voce utilizara ")
print()
if ataque =="1":
    print(" voce usou corte voce tirou 15 de hp")
elif ataque =="2":
    numero = random.randint(7,12)
    print(f"voce usou multiplos cortes voce tirou {numero} de hp")
elif ataque == "3":
    print("voce usou corte sagrado voce tirou 35 de hp e deixou seu inimigo sangrando")
    print()