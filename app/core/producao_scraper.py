from typing import List
from app.models.item_producao import ItemProducao
from app.core.data_loader import URL, load_page
from app.core.scraper_cache import ScraperCache

class ProducaoScraper(ScraperCache):
    """
    Scraper para coletar dados de produção de vinho do site da Embrapa.
    """
    def __init__(self, url: URL, year: int):
        self.year = year
        self.url = url

    def get_cache_key(self) -> str:
        return f"{self.url.name}_{self.year}"

    def scrape_data(self) -> List[ItemProducao]:

        soup = load_page(self.url, self.year)

        tabela = soup.find("table", class_="tb_base tb_dados")
        linhas = tabela.tbody.find_all("tr")

        produtos: List[ItemProducao] = []
        produto_atual: ItemProducao = None

        for linha in linhas:
            colunas = linha.find_all("td")
            if len(colunas) != 2:
                continue

            nome = colunas[0].get_text(strip=True)
            qtd_str = colunas[1].get_text(strip=True).replace(".", "")
            quantidade = int(qtd_str) if qtd_str.isdigit() else 0
            classes = colunas[0].get("class", [])

            if "tb_item" in classes:
                produto_atual = ItemProducao(produto=nome, quantidade=quantidade, sub_items=[])
                produtos.append(produto_atual)
            elif "tb_subitem" in classes and produto_atual:
                subitem = ItemProducao(produto=nome, quantidade=quantidade, sub_items=[])
                produto_atual.sub_items.append(subitem)

        return produtos