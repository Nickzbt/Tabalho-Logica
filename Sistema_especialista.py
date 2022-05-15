import csv
import json
import os

from sets import dificuldade, paradigma, seguranca, utilizacoes, velocidade

# lista para armezenar dicionarios referentes a cada uma das linguagens
linguagens = []

dict_escolha: dict = {
    "utilizacoes": [],  # dado como lista para poder adicionar novas opcoes se necessario
    "dificuldade": None,
    "paradigma": [],  # dado como lista para poder adicionar novas opcoes se necessario
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
        # lista de utilizacoes possíveis, separacao em ', '
        "utilizacoes":rows["utilizacoes"].split(', '),
        "dificuldade":rows["sintaxe"],
        # lista de paradigmas de programacao, separacao em ', '
        "paradigma":rows["paradigma"].split(', '),
        "seguranca":rows["seguranca"] or 'N/A',
        "velocidade":rows["velocidade"]
    } for rows in reader]

print("Selecione uma utilizacao (digite o numero): ")
print_options(utilizacoes)
dict_escolha["utilizacoes"].append(get_choice(utilizacoes))
os.system("cls")

print("Selecione uma dificuldade (digite o numero): ")
print_options(dificuldade)
dict_escolha["dificuldade"] = get_choice(dificuldade)
os.system("cls")

print("Selecione um paradigma (digite o numero): ")
print_options(paradigma)
dict_escolha["paradigma"].append(get_choice(paradigma))
os.system("cls")

print("Selecione um nivel de seguranca (digite o numero): ")
print_options(seguranca)
dict_escolha["seguranca"] = get_choice(seguranca)
os.system("cls")

print("Selecione uma velocidade de compilacao (digite o numero): ")
print_options(velocidade)
dict_escolha["velocidade"] = get_choice(velocidade)
os.system("cls")

def ling_resultado():
    possible_l = []
    for i in linguagens:
        count = 0

        if bool([l for l in i["utilizacoes"] if l in dict_escolha["utilizacoes"]]):
            count += 1

        if i["dificuldade"] == "N/A" or dict_escolha["dificuldade"] == "N/A" or i["dificuldade"] == dict_escolha["dificuldade"]:
            count += 1

        if bool([l for l in i["paradigma"] if l in dict_escolha["paradigma"]]):
            count += 1

        if i["seguranca"] == "N/A" or dict_escolha["seguranca"] == "N/A" or i["seguranca"] == dict_escolha["seguranca"]:
            count += 1

        if i["velocidade"] == "N/A" or dict_escolha["velocidade"] == "N/A" or i["velocidade"] == dict_escolha["velocidade"]:
            count += 1

        if count > 3:
            possible_l.append(i)

    if len(possible_l) == 0:
        print("Selecione uma utilizacao (digite o numero): ")
        uti = [u for u in utilizacoes if u not in dict_escolha["utilizacoes"]]
        print_options(uti)
        dict_escolha["utilizacoes"].append(get_choice(uti))
        os.system("cls")

        print("Selecione um paradigma (digite o numero): ")
        par = [p for p in paradigma if p not in dict_escolha["paradigma"]]
        print_options(par)
        dict_escolha["paradigma"].append(get_choice(par))
        os.system("cls")

        ling_resultado()
    else:
        print("Parametros de linguagem escolhidos:\n",dict_escolha)
        result = ""
        for i, idx in zip(possible_l, range(0, len(possible_l))):
            result += i["nome"]
            if idx < len(possible_l)-1:
                result += ", "
        print("Pode usar essa(s) linguagem(ns):", result)        
            
ling_resultado()
