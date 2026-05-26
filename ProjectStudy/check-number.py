import random

print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 50.")

numero = random.randint(1, 50)

tentativas = 0

while True:

   chute = int(input("Adivinhe o numero: "))
   
   tentativas += 1
   
   if chute < numero:
       print("Muito baixo! Tente novamente.")
   elif chute > numero:
       print("Muito alto! Tente novamente.")
   else:
       print(f"Parabéns! Você adivinhou o número {numero} em {tentativas} tentativas.")
       break
   
   if tentativas == 3:
        print(f"Suas tentativas acabaram! O número era {numero}.")
        break
   
   
    
