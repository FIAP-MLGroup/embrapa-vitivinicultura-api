import os
import pandas as pd
from enum import Enum

class URL(Enum):
    PRODUCAO = {
        "endpoint": os.getenv("ENDPOINT_PRODUCAO", "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"),
        "separator": os.getenv("SEPARATOR_PRODUCAO", ";")
    }
    PROCESSAMENTO_VINIFERAS = {
        "endpoint": os.getenv("ENDPOINT_PROCESSAMENTO_VINIFERAS", "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv"),
        "separator": os.getenv("SEPARATOR_PROCESSAMENTO_VINIFERAS", ";")
    }
    PROCESSAMENTO_AMERICANAS_HIBRIDAS = {
        "endpoint": os.getenv("ENDPOINT_PROCESSAMENTO_AMERICANAS_HIBRIDAS", "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv"),
        "separator": os.getenv("SEPARATOR_PROCESSAMENTO_AMERICANAS_HIBRIDAS", "\t")
    }
    PROCESSAMENTO_UVAS_MESA = {
        "endpoint": os.getenv("ENDPOINT_PROCESSAMENTO_UVAS_MESA", "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv"),
        "separator": os.getenv("SEPARATOR_PROCESSAMENTO_UVAS_MESA", "\t")
    }
    PROCESSAMENTO_SEM_CLASSIFICACAO = {
        "endpoint": os.getenv("ENDPOINT_PROCESSAMENTO_SEM_CLASSIFICACAO", "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv"),
        "separator": os.getenv("SEPARATOR_PROCESSAMENTO_SEM_CLASSIFICACAO", "\t")
    }
    COMERCIALIZACAO = {
        "endpoint": os.getenv("ENDPOINT_COMERCIALIZACAO", "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"),
        "separator": os.getenv("SEPARATOR_COMERCIALIZACAO", ";")
    }
    IMPORTACAO_VINHOS_MESA = {
        "endpoint": os.getenv("ENDPOINT_IMPORTACAO_VINHOS_MESA", "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv"),
        "separator": os.getenv("SEPARATOR_IMPORTACAO_VINHOS_MESA", "\t")
    }
    IMPORTACAO_ESPUMANTES = {
        "endpoint": os.getenv("ENDPOINT_IMPORTACAO_ESPUMANTES", "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv"),
        "separator": os.getenv("SEPARATOR_IMPORTACAO_ESPUMANTES", "\t")
    }
    IMPORTACAO_UVAS_FRESCAS = {
        "endpoint": os.getenv("ENDPOINT_IMPORTACAO_UVAS_FRESCAS", "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv"),
        "separator": os.getenv("SEPARATOR_IMPORTACAO_UVAS_FRESCAS", "\t")
    }
    IMPORTACAO_UVAS_PASSAS = {
        "endpoint": os.getenv("ENDPOINT_IMPORTACAO_UVAS_PASSAS", "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv"),
        "separator": os.getenv("SEPARATOR_IMPORTACAO_UVAS_PASSAS", "\t")
    }
    IMPORTACAO_SUCO_UVA = {
        "endpoint": os.getenv("ENDPOINT_IMPORTACAO_SUCO_UVA", "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv"),
        "separator": os.getenv("SEPARATOR_IMPORTACAO_SUCO_UVA", ";")
    }
    EXPORTACAO_VINHOS_MESA = {
        "endpoint": os.getenv("ENDPOINT_EXPORTACAO_VINHOS_MESA", "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"),
        "separator": os.getenv("SEPARATOR_EXPORTACAO_VINHOS_MESA", "\t")
    }
    EXPORTACAO_ESPUMANTES = {
        "endpoint": os.getenv("ENDPOINT_EXPORTACAO_ESPUMANTES", "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv"),
        "separator": os.getenv("SEPARATOR_EXPORTACAO_ESPUMANTES", "\t")
    }
    EXPORTACAO_UVAS_FRESCAS = {
        "endpoint": os.getenv("ENDPOINT_EXPORTACAO_UVAS_FRESCAS", "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv"),
        "separator": os.getenv("SEPARATOR_EXPORTACAO_UVAS_FRESCAS", "\t")
    }
    EXPORTACAO_SUCO_UVA = {
        "endpoint": os.getenv("ENDPOINT_EXPORTACAO_SUCO_UVA", "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv"),
        "separator": os.getenv("SEPARATOR_EXPORTACAO_SUCO_UVA", "\t")
    }

def carregar_dados(url: URL) -> pd.DataFrame:
    endpoint = url.value["endpoint"]
    separator = url.value["separator"]
    try:
        return pd.read_csv(endpoint, sep=separator)
    except Exception as e:
        raise Exception(f"Erro ao carregar dados do tipo '{url.name}' a partir de {endpoint}: {e}")