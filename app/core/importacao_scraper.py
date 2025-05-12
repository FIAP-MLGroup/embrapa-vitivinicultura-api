# core/scraper_importacao.py
from typing import List, Optional
from app.core.data_loader import URL, load_page
from app.models.item_importacao import ItemImportacao

def scrap_data(url: URL, year: int) -> List[ItemImportacao]:
    
    soup = load_page(url, year)

    tabela = soup.find("table", class_="tb_base tb_dados")
    if not tabela or not tabela.tbody:
        return []

    resultados: List[ItemImportacao] = []

    for linha in tabela.tbody.find_all("tr"):
        colunas = linha.find_all("td")
        if len(colunas) != 3:
            continue

        pais = colunas[0].get_text(strip=True)

        def parse_value(texto: str) -> Optional[int]:
            texto = texto.replace(".", "").strip()
            return int(texto) if texto.isdigit() else None

        quantidade = parse_value(colunas[1].get_text())
        valor = parse_value(colunas[2].get_text())

        item = ItemImportacao(
            pais=pais,
            quantidade=quantidade,
            valor=valor
        )
        resultados.append(item)

    return resultados
