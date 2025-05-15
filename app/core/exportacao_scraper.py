# core/scraper_exportacao.py
from typing import List, Optional
from app.core.data_loader import URL, load_page
from app.models.item_exportacao import ItemExportacao
from app.core.scraper_cache import ScraperCache

class ExportacaoScraper(ScraperCache[ItemExportacao]):
    """
    Scraper para coletar dados de exportação de vinho do site da Embrapa.
    """
    def __init__(self, url: URL, year: int):
        super().__init__(ItemExportacao)
        self.year = year
        self.url = url

    def get_cache_key(self) -> str:
        return f"{self.url.name}_{self.year}"

    def scrape_data(self) -> List[ItemExportacao]:
        
        soup = load_page(self.url, self.year)

        tabela = soup.find("table", class_="tb_base tb_dados")
        if not tabela or not tabela.tbody:
            return []

        resultados: List[ItemExportacao] = []

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

            item = ItemExportacao(
                pais=pais,
                quantidade=quantidade,
                valor=valor
            )
            resultados.append(item)

        return resultados
