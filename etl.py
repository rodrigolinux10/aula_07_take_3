
 

import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Função para ler um arquivo CSV e retornar uma lista de dicionários
    """
    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo)
        for linha in reader:
            lista.append(linha)
    return lista

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Função para filtrar os produtos onde entrega = True

    """
    lista_com_produtos_filtrados =[]
    for produto in lista:
        if produto.get("entregue") == "False":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    """
    Soma todos os valores dos produtos que estão na lista
    """
    total = 0
    for produto in lista_com_produtos_filtrados:
  
            total += int(produto.get("price"))
    return total

