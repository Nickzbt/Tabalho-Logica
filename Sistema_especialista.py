import csv
import json

from sets import dificuldade, paradigma, seguranca, utilizacoes, velocidade

# lista para armezenar dicionarios referentes a cada uma das linguagens
linguagens = []

dict_escolha: dict = {
    "nome": None,
    "utilizacoes": None,
    "dificuldade": None,
    "salario": None,
    "paradigma": None,
    "seguranca": None,
    "velocidade": None
}


def print_options(options: list[str]):
    count = 0
    for i in options:
        print('(', count, ')', i)
        count += 1


def get_choice(options: list[str]) -> str:
    choice = None
    while choice == None:
        choice = int(input("escolha uma das opcoes acima: "))
        if choice >= len(options) or choice < 0:
            print("opa! escolha", choice, "nao e uma das opcoes...")
            choice = None
    return options[choice]


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
dict_escolha["utilizacoes"] = get_choice(utilizacoes)

print("selecione uma dificuldade (digite o numero)")
print_options(dificuldade)
dict_escolha["dificuldade"] = get_choice(dificuldade)

print("selecione um paradigma (digite o numero)")
print_options(paradigma)
dict_escolha["paradigma"] = get_choice(paradigma)

print("selecione um nivel de seguranca (digite o numero)")
print_options(seguranca)
dict_escolha["seguranca"] = get_choice(seguranca)

print("selecione uma velocidade de compilacao (digite o numero)")
print_options(velocidade)
dict_escolha["velocidade"] = get_choice(velocidade)

salario = int(input("insira uma faixa salarial (valor por ano): "))
dict_escolha["salario"] = salario

print(json.dumps(dict_escolha, indent=4))
