listafrutas = ["maça", "banana", "laranja", "abacaxi", "melancia"];
print(listafrutas);

listafrutas.append("uva");
print(listafrutas);

listafrutas.remove("banana");
print(listafrutas);

print(listafrutas[1]);
fruta_selecionada = (listafrutas[1]);
print(fruta_selecionada);
listafrutas = ["maça", "laranja", "melancia"];

tupla = ("vermelho", "azul", "verde", "amarelo", "roxo");
print(tupla);

#NAO COLOCOU ANTES LINHA 21 POR ISSO NAO APARECE COR LARANJA
print(tupla[4]);
cor_selecionada = (tupla[4]);
tupla = ["vermelho", "azul", "verde", "amarelo", "roxo"];
tupla = ["vermelho", "azul", "verde", "amarelo", "roxo", "LARANJA"];

meuDicionario = {
    'Nome'   :   'Thiago',
    'Idade'  :   25,
    'Cidade' :  'São Paulo'
}
print(meuDicionario);

aluno = (15, 17, 18, 19);
print(aluno);

print(aluno[2]);
idade_aluno = (aluno[2]);
idade = (15, 17, 18, 19);
print(idade_aluno);
aluno = [15, 17, 18];

print(aluno[1]);
genero = (aluno[1]);
print("masculino, idade: ", genero);

cidade = ["Sao Paulo", "Sao Caetano", "Centro"];
cidade.append("Santo Andre");
print(cidade);

cidade.insert(1, "Av. Paulista");     
print(cidade);        
print(); 
cidadeRemovida = cidade.remove("Sao Paulo");
cidadeRemovida = cidade.pop(0);
print("cidade");
print(cidadeRemovida);

cidade.sort();

print("Embaralhado ", cidade);













