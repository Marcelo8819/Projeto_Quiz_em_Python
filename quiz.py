print("Bem vindo ao meu Quiz do Marcelo Henrique")
answer_user = input("Quer começar ? (S/N) ")
print(answer_user)

if answer_user != "S":
   quit()

score = 0 
   
print("Començando...")
print("Em que ano Marcelo nasceu? \n (A) 1995 \n (B) 1988 \n (C) 1888 \n (D) 1992 ")
answer_1 = input("Resposta: ")

if answer_1 == "B":
    print("Correto!")
    score = score + 1 
else:
    print("Errado!")

print("Marcelo é estudante de qual curso superior? \n (A) Direito \n (B) Engenharia da computação \n (C) Ciências do consumo \n (D) Matemática ")
answer_2 = input("Resposta: ")

if answer_2 == "C":
    print("Correto!")
    score = score + 1 
else:
    print("Errado!")

print("Quiz acabou... Pontuação :{}/2 " .format(score))




