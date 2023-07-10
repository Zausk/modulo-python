a =     10;
b =     5;

soma            = a  +  b;
substracao      = a  -  b;
multiplicacao   = a  *  b;
divisao         = a  /  b;
resto           = a  %  b;
potencia        = a  ** b;

print("Soma: ", soma);
print("Substracao: ", substracao);
print("multiplicacao: ", multiplicacao);
print("divisao:", divisao);
print("resto: ", resto);
print("potencia:", potencia);


numero = float(input('Digite um numero para saber se é par ou ímpar: '))
resto = numero % 2

if resto == 0:
    print ('numero é par')
else:
    print('numero é ímpar') 
    
   
#Verificação de acesso um sistema 
senha = input("Digite sua senha: ");

senha_correta = "123456";

if senha == senha_correta:
    print("Usuário logado com sucesso");
else:
    print("A senha informada está errada");
    
    
#Verificaçao de idade para entrada em clube noturno
idade = int(input("Digite sua idade: "));

if idade >= 18:
    print("Bem-vindo,(a)(e) você pode entrar na balada!");
else:
    print("Desculpe, você não tem idade suficiente para entrar na balada3");
    
numero = 30;

num1 = input("Insira um numero (1/2): ")
num2 = input("Insira um numero (2/3): ")

if num1 == num2:
    print("Os dois numeros sao iguais")
    
elif num1 > num2:
    print("Seu primeiro numero: "+num1+" .E maior que o segundo numero: "+num2+".")
elif num2 > num1:
    print("Seu segundo numero: "+num2+". E maior que o primeiro numero: "+num1+".")
    
frase = input("Digite uma frase: ")
vogais  = 0 
espacos = 0
for letra in frase:
    if letra == " ":
        espacos += 1
    elif letra in "aeiou":
        vogais +=1
    print(" A frase tem %d vogais e %d espaco." % (vogais,espacos))
    
num1 = input("positivo")
num2 = input("negativo")
num3 = input("zero")
   
if num1 == num2 == num3:
    print("Numero positivo: "+num2+". E maior que o primeiro numero: "+num1+".")
elif num1 > num2 > num3:
    print("Numero negativo: "-num3-". E maior que o segundo numero: "-num2-".")
elif num3 > num2 > num1:
    print("Numero zero: "+num3+". E maior que o terceiro numero: "+num1+".")
          

Ordem = 3
int = 1, 2, 3;

if (1 <=2):
    print("ordem = 1 =>2")
else:
    print("ordem = 2 <=3")
    

