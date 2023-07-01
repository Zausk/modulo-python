meuDicionario = {
'nome'      : 'Thiago',
'sobrenome' : 'Levino',
'anos'      :  30
}

print(meuDicionario);

frutaDicionario = {
    'maçã'      : 3,
    'banana'    : 6,
    'uva'       : 8,
};

print("Significado encontrado no dicionario: ", frutaDicionario["maçã"]);
print();
frutaDicionario["maça"] = 5;
frutaDicionario["laranja"] = 10;
print("Significado encontrado no dicionario: ", frutaDicionario["maçã"]);
print();
print(frutaDicionario);

print(frutaDicionario);
print();
animaisDicionario = {};
animaisDicionario["cachorro"] = "Melissa";
print(animaisDicionario);


aluno = {
    'nome'     : 'Thiago',
    'idade'    : 35,
    'hobbies'  : ['jogar', 'csgo',
    'esporte' ]
}

print(aluno);

frutaDicionario = {
    'maçã'      : 3,
    'banana'    : 6,
    'uva'       : 8,
    'laranja'   : 10
};

print();
print("Quantidade de maçãs: ",
frutaDicionario.get("maçã"));
print("Quantidade de bananas: ", 
frutaDicionario.get("banana"));

print("Quantidade de morangos: ",
frutaDicionario.get("morangos", "Não foi encontrado a definição de morango")); 

elementoRemovido = frutaDicionario.pop("laranja");
print(elementoRemovido);
print("Dicionaário atualizado: ", 
frutaDicionario);

frutaDicionario = {
    'maçã'      : 3,
    'banana'    : 6,
    'uva'       : 8,
    'laranja'   : 10
};

print();
print("Chaves encontrados no dicionário", frutaDicionario.keys());
print("Valores encontrados no dicionário: ", frutaDicionario.values());
print(frutaDicionario.items());


# apaga

