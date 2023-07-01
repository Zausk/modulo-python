print("Olá, meu nome Thiago");
print("Tenho 30 anos");

print("Abacate", "Kiwi", "Limão");

nomeCompleto = "Thiago " + '' + "Levino Nunes";
print(nomeCompleto);


#Arredododamento de numeros
numeroFloat = 5.20;
numeroArrendodado = round(numeroFloat);
print("Arrendodamento: ", numeroArrendodado);
#Funcções matemáticas de biblioteca math 
import math 

num = 4.7;
print("Funções matemáticas: ");
print("Valor abosulto: ", abs(-5.9));
print("Arredondamento pra cima", math.ceil(num));
print("Arredondamento pra baixo", math.floor(num));

#Geração números aleatórios
import random
print("Números aleatórios: ")
print("Números aleatórios de 1 a 10", random.randint(1, 10));
print("Números float aleatório entre 0 e 1", random.random())

#Formatação de números

numeroFormatado = 1234.56789;
print("Formatação de números:");
print("Número com 2 casas decimais{numeroFormatado:.2f}");
print("Número formatado com 2 casas decimais {:.2f}".format(numeroFormatado))


fraseNova = "Olá Python";
print(fraseNova.upper());

num1 = 10;
num2 = 30;
soma = num1 + num2;

