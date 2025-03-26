print("bem vindo ao buscador de letras")
print("primeiro: escolha uma frase")

word = input()
    
size = len(word)

print("agora escolha um número")

num = int(input()) - 1

word = word.replace(" ", "")


if num > size:
    num = size - 1

if num < 0:
    num = 0


print("você escolheu a letra: " + word[num])