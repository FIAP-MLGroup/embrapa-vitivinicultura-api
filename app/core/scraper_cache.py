from abc import ABC, abstractmethod
from typing import List
from app.core.s3_cache import read_from_s3, write_to_s3_async
from pydantic import BaseModel

# Cache local em memória usando variável estática (dicionário global)
LOCAL_CACHE = {}

class ScraperCache(ABC):
    @abstractmethod
    def get_cache_key(self) -> str:
        """Método para gerar chave única de cache (baseado no ano ou outro parâmetro)"""
        pass
    
    @abstractmethod
    def scrape_data(self) -> List[BaseModel]:
        """Método que será implementado nas subclasses para fazer o scraping específico"""
        pass
    
    def load_local_cache(self, cache_key: str) -> List[BaseModel] | None:
        """Tenta carregar os dados do cache local"""
        return LOCAL_CACHE.get(cache_key)

    def save_local_cache(self, cache_key: str, data: List[BaseModel]):
        """Salva os dados no cache local"""
        LOCAL_CACHE[cache_key] = data

    def get_data(self) -> List[BaseModel]:
        """Lógica comum de cache: tenta carregar os dados da cache local, depois do scraping e do S3"""
        cache_key = self.get_cache_key()

        # 1. Tenta carregar do cache local (em memória)
        if cached := self.load_local_cache(cache_key):
            return cached
        
        print(f"[Cache] Cache local não encontrado para {cache_key}. Iniciando scraping...")

        try:
            # 2. Faz o scraping dos dados
            scraped_data = self.scrape_data()

            # 3. Salva no cache local (em memória)
            self.save_local_cache(cache_key, scraped_data)

            # 4. Dispara gravação assíncrona no S3
            write_to_s3_async(cache_key, scraped_data)

            return scraped_data

        except Exception:
            # 5. Se falhar, tenta recuperar do S3 (leitura síncrona)
            if backup := read_from_s3(cache_key=cache_key, model=type(BaseModel)):
                # Salva no cache local (em memória)
                self.save_local_cache(cache_key, backup)
                return backup

            # Se tudo falhar, lança exceção
            raise RuntimeError("Erro ao recuperar os dados.")
