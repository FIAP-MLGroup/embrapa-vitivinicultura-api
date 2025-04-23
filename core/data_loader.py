import os
import pandas as pd
from enum import Enum

class URL(Enum):
    PRODUCAO = os.getenv("URL_PRODUCAO", "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv")
    PROCESSAMENTO_VINIFERAS = os.getenv("URL_PROCESSAMENTO_VINIFERAS", "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv")
    PROCESSAMENTO_AMERICANAS_HIBRIDAS = os.getenv("URL_PROCESSAMENTO_AMERICANAS_HIBRIDAS", "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv")
    PROCESSAMENTO_UVAS_MESA = os.getenv("URL_PROCESSAMENTO_UVAS_MESA", "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv")
    PROCESSAMENTO_SEM_CLASSIFICACAO = os.getenv("URL_PROCESSAMENTO_SEM_CLASSIFICACAO", "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv")
    COMERCIALIZACAO = os.getenv("URL_COMERCIALIZACAO", "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv")
    IMPORTACAO_VINHOS_MESA = os.getenv("URL_IMPORTACAO_VINHOS_MESA", "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv")
    IMPORTACAO_ESPUMANTES = os.getenv("URL_IMPORTACAO_ESPUMANTES", "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv")
    IMPORTACAO_UVAS_FRESCAS = os.getenv("URL_IMPORTACAO_UVAS_FRESCAS", "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv")
    IMPORTACAO_UVAS_PASSAS = os.getenv("URL_IMPORTACAO_UVAS_PASSAS", "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv")
    IMPORTACAO_SUCO_UVA = os.getenv("URL_IMPORTACAO_SUCO_UVA", "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv")
    EXPORTACAO_VINHOS_MESA = os.getenv("URL_EXPORTACAO_VINHOS_MESA", "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv")
    EXPORTACAO_ESPUMANTES = os.getenv("URL_EXPORTACAO_ESPUMANTES", "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv")
    EXPORTACAO_UVAS_FRESCAS = os.getenv("URL_EXPORTACAO_UVAS_FRESCAS", "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv")
    EXPORTACAO_SUCO_UVA = os.getenv("URL_EXPORTACAO_SUCO_UVA", "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv")

def get_separador(url: URL):

    tsv="\t"
    csv=";"
    
    if url in (
        URL.PROCESSAMENTO_AMERICANAS_HIBRIDAS,
        URL.PROCESSAMENTO_UVAS_MESA,
        URL.PROCESSAMENTO_SEM_CLASSIFICACAO,
        URL.IMPORTACAO_VINHOS_MESA, 
        URL.IMPORTACAO_ESPUMANTES, 
        URL.IMPORTACAO_UVAS_FRESCAS,
        URL.IMPORTACAO_UVAS_PASSAS,
        URL.EXPORTACAO_VINHOS_MESA,
        URL.EXPORTACAO_ESPUMANTES,
        URL.EXPORTACAO_UVAS_FRESCAS,
        URL.EXPORTACAO_SUCO_UVA):
        # Se o URL for um dos tipos específicos, use o separador de tabulação
        return tsv
    
    return csv

def carregar_dados(url: URL) -> pd.DataFrame:
    try:
        return pd.read_csv(url.value, sep=get_separador(url))
    except Exception as e:
        raise Exception(f"Erro ao carregar dados do tipo '{url.name}' a partir de {url.value}: {e}")