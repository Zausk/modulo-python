"""
Estruturas condicionais
"""

#Verificaçao de idade para entrada em clube noturno
idade = int(input("Digite sua idade: "));

if idade >= 18:
    print("Bem-vindo,(a)(e) você pode entrar na festa!");
else:
    print("Desculpe, você não tem idade suficiente para entrar na festa");
    
#Verificação se um número está dentro de um intervalo entre 10 e 20;
numero = 21;

if (numero >= 10) and (numero <=20): 
    print("O numero está dentro do intervalo");
else:
    print("O numero está fora do intervalo");
    
#Comparar o tamanho de duas listas
lista1 = [1,2,3,4.5];
lista2 = [5,4,3,2, 'a'];

if len(lista1) > len(lista2):
    print("A lista 1 e maior que a lista2");
elif len(lista2) > len(lista1):
    print("A lista 2 é maior que a 1");
else: 
    print("As Listas tem o mesmo tamanho")

#Verificação de acesso um sistema 
senha = input("Digite sua senha: ");

senha_correta = "123456";

if senha == senha_correta:
    print("Usuário logado com sucesso");
else:
    print("A senha informada está errada");
    
#Verificação de acesso um sistema com login e senha 
usuario = input("Dgite o seu usuário: ");
senha   = input("Digite sua senha: ");

usuarioCorreto = "admin";
usuarioCorreta = "admin";

if (usuarioCorreto == usuarioCorreto) and (senha == senha_correta):
    print("Login bem - sucedido");
else: 
    print("O usuário ou a senha estão incorreto!")
    