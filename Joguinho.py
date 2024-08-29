import random
import os
os.system('cls')

print('Bem-vindo a "A Lenda do Cofre de Eldoria: Uma Aventura Personalizada"! \n')
print("Em um reino longínquo chamado Eldoria, reside uma masmorra misteriosa que guarda um artefato de poder inimaginável. Para obtê-lo, os aventureiros devem superar uma série de desafios, sendo o principal deles um enigma numérico que protege o cofre \n")
input("Envie qualquer coisa para continuar \n")
os.system('cls')

totalLooses = 0

name = input("Olá aventureiro! Posso saber seu nome? \n")
level = 1
xp = 0
healthPoints = 3
goldCoins = 0

os.system('cls')

print(f"Sua ficha: \nNome: {name}\nExperiência: {xp}\nPontos de vida: {healthPoints}\nMoedas de ouro: {goldCoins}\n")

print(f"Boas vindas {name}! Que nome bonito haha \n")
print(f"{name}. Hoje você fará o enigma principal, O Desafio do Cofre. \n")
print("O enigma funcionará da seguinte maneira, o cofre terá um numero aleatório de 1 a 18, e você terá 3 dados de 6 faces, jogue os 3 dados e tenha a sorte do total dos números ser o número do cofre escolhido. \nBoa sorte aventureiro!\n")

vaultNum = random.randint(1, 18)

while True:    
    
    input("Envie qualquer coisa para rodar os dados.")
    os.system('cls')
    
    total = 0
    
    for x in range(0, 3):
        print(f"Jogando o dado numero {x + 1}")
        
        randomNum = random.randint(1, 6)
        total += randomNum
        
        print(f"O dado caiu no número {randomNum}! \n")
    
    print(f"O total foi {total}")
    
    if (total == vaultNum):
        print(f"Parabéns {name}! O número do cofre era {total}, você ganhou 10 moedas de ouro e 2 pontos de experiência \n")
        
        goldCoins += 10
        xp += 2
        
        if xp >= 4:
            level += 1
            xp = 0
            print(f"Seu nível aumentou para o nível {level}! \n")
            
        print("O que você deseja fazer agora, aventureiro? \n")
            
        answer = input("1 - Continuar a aventura\n2 - Procurar outro cofre\n3 - Sair da masmorra com meus ganhos\n")
        os.system('cls')
            
        match answer:
            case "2":
                print("Você foi em busca de outro cofre e encontrou um com outro número aleatório. \n")
                vaultNum = random.randint(3, 18)
            case "3":
                print("Você saiu da masmorra vivo, meus parabéns!\n")
                
                print(f"Sua ficha: \nNome: {name}\nExperiência: {xp}\nPontos de vida: {healthPoints}\nMoedas de ouro: {goldCoins}\n")
                break
        
    else:
        print("Poxa! Parece que o número total não é igual ao número do cofre \n")
        
        totalLooses += 1
        if totalLooses >= 2:
             totalLooses = 0
             healthPoints -= 1
             print(f"Você perdeu 1 ponto de vida! Você possui agora {healthPoints} pontos de vida\n")
        
        if healthPoints <= 0:
            print(f"Meus pesâmes, aventureiro {name}, parece que a sua vida chegou a 0, você morreu, sua aventura acaba aqui.")
            break