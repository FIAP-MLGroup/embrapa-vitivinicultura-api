import os
import pandas as pd
from enum import Enum
import requests
from bs4 import BeautifulSoup

class URL(Enum):
    PRODUCAO = {
        "endpoint": os.getenv("ENDPOINT_PRODUCAO", "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02")
    }
    PROCESSAMENTO_VINIFERAS = {
        "endpoint": os.getenv("ENDPOINT_PROCESSAMENTO_VINIFERAS", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_03")
    }
    PROCESSAMENTO_AMERICANAS_HIBRIDAS = {
        "endpoint": os.getenv("ENDPOINT_PROCESSAMENTO_AMERICANAS_HIBRIDAS", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_03")
    }
    PROCESSAMENTO_UVAS_MESA = {
        "endpoint": os.getenv("ENDPOINT_PROCESSAMENTO_UVAS_MESA", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_03")
    }
    PROCESSAMENTO_SEM_CLASSIFICACAO = {
        "endpoint": os.getenv("ENDPOINT_PROCESSAMENTO_SEM_CLASSIFICACAO", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_03")
    }
    COMERCIALIZACAO = {
        "endpoint": os.getenv("ENDPOINT_COMERCIALIZACAO", "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04")
    }
    IMPORTACAO_VINHOS_MESA = {
        "endpoint": os.getenv("ENDPOINT_IMPORTACAO_VINHOS_MESA", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_05")
    }
    IMPORTACAO_ESPUMANTES = {
        "endpoint": os.getenv("ENDPOINT_IMPORTACAO_ESPUMANTES", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_05")
    }
    IMPORTACAO_UVAS_FRESCAS = {
        "endpoint": os.getenv("ENDPOINT_IMPORTACAO_UVAS_FRESCAS", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_05")
    }
    IMPORTACAO_UVAS_PASSAS = {
        "endpoint": os.getenv("ENDPOINT_IMPORTACAO_UVAS_PASSAS", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_05")
    }
    IMPORTACAO_SUCO_UVA = {
        "endpoint": os.getenv("ENDPOINT_IMPORTACAO_SUCO_UVA", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_05&opcao=opt_05")
    }
    EXPORTACAO_VINHOS_MESA = {
        "endpoint": os.getenv("ENDPOINT_EXPORTACAO_VINHOS_MESA", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_06")
    }
    EXPORTACAO_ESPUMANTES = {
        "endpoint": os.getenv("ENDPOINT_EXPORTACAO_ESPUMANTES", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_06")
    }
    EXPORTACAO_UVAS_FRESCAS = {
        "endpoint": os.getenv("ENDPOINT_EXPORTACAO_UVAS_FRESCAS", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_06")
    }
    EXPORTACAO_SUCO_UVA = {
        "endpoint": os.getenv("ENDPOINT_EXPORTACAO_SUCO_UVA", "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_06")
    }

def load_page(url: URL, year: int) -> BeautifulSoup:
    endpoint = f"{url.value["endpoint"]}&ano={year}"
    print(f"Scraping data for year: {year}")
    print(f"URL: {endpoint}")
    response = requests.get(endpoint)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'html.parser')
