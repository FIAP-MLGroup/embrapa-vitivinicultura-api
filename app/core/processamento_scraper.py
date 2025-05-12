# core/scraper_processamento.py
from typing import List
from app.core.data_loader import URL, load_page
from app.models.item_processamento import ItemProcessamento

def scrap_data(url: URL, year: int) -> List[ItemProcessamento]:
    
    soup = load_page(url, year)

    tabela = soup.find("table", class_="tb_base tb_dados")
    if not tabela or not tabela.tbody:
        return []

    produtos: List[ItemProcessamento] = []
    produto_atual: ItemProcessamento = None

    for linha in tabela.tbody.find_all("tr"):
        colunas = linha.find_all("td")
        if len(colunas) != 2:
            continue

        nome = colunas[0].get_text(strip=True)
        qtd_str = colunas[1].get_text(strip=True).replace(".", "")
        quantidade = int(qtd_str) if qtd_str.isdigit() else 0
        classes = colunas[0].get("class", [])

        if "tb_item" in classes:
            produto_atual = ItemProcessamento(produto=nome, quantidade=quantidade, sub_items=[])
            produtos.append(produto_atual)
        elif "tb_subitem" in classes and produto_atual:
            sub = ItemProcessamento(produto=nome, quantidade=quantidade, sub_items=[])
            produto_atual.sub_items.append(sub)

    return produtos
