import csv
import json

from sets import dificuldade, paradigma, seguranca, utilizacoes, velocidade

# lista para armezenar dicionarios referentes a cada uma das linguagens
linguagens = []

salario: int = 0

dict_escolha: dict = {
    "nome": None,
    "utilizacoes": None,
    "dificuldade": None,
    "salario": None,
    "paradigma": None,
    "seguranca": None,
    "velocidade": None
}

def print_options(option: list[str]):
    count = 0
    for i in option:
        print('(', count, ')', i)
        count += 1

with open('data.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    linguagens = [{
        "nome": rows["nome"],
        # lista de utilizacoes possíveis, separacao em ','
        "utilizacoes":rows["utilizacoes"].split(', '),
        "dificuldade":rows["sintaxe"],
        "salario":rows["salario"],
        # lista de paradigmas de programacao, separacao em ','
        "paradigma":rows["paradigma"].split(', '),
        "seguranca":rows["seguranca"] or 'N/A',
        "velocidade":rows["velocidade"]
    } for rows in reader]

print("selecione uma utilizacao (digite o numero)")
print_options(utilizacoes)
choice = int(input("escolha uma das opcoes acima: "))
dict_escolha["utilizacoes"] = utilizacoes[choice]

print("selecione uma dificuldade (digite o numero)")
print_options(dificuldade)
choice = int(input("escolha uma das opcoes acima: "))
dict_escolha["dificuldade"] = dificuldade[choice]

print("selecione um paradigma (digite o numero)")
print_options(paradigma)
choice = int(input("escolha uma das opcoes acima: "))
dict_escolha["paradigma"] = paradigma[choice]

print("selecione um nivel de seguranca (digite o numero)")
print_options(seguranca)
choice = int(input("escolha uma das opcoes acima: "))
dict_escolha["seguranca"] = seguranca[choice]

print("selecione uma velocidade de compilacao (digite o numero)")
print_options(velocidade)
choice = int(input("escolha uma das opcoes acima: "))
dict_escolha["velocidade"] = velocidade[choice]

salario = int(input("insira uma faixa salarial (valor por ano): "))
dict_escolha["salario"] = salario

print(json.dumps(dict_escolha, indent=4))
