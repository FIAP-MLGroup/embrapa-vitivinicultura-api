import json
import boto3
import threading
from typing import List, TypeVar, Type, Optional
from pydantic import BaseModel
import os

T = TypeVar("T", bound=BaseModel)

BUCKET_NAME = os.getenv("S3_CACHE_BUCKET", "embrapa-vitivinicultura")
s3 = boto3.client("s3")


def _get_object_key(cache_key: str) -> str:
    return f"{cache_key}.json"


def read_from_s3(cache_key: str, model_cls: Type[T]) -> Optional[List[T]]:
    """
    Lê dados do S3 e os desserializa usando o model informado.
    """
    try:
        object_key = _get_object_key(cache_key)
        response = s3.get_object(Bucket=BUCKET_NAME, Key=object_key)
        content = response['Body'].read().decode('utf-8')
        raw_data = json.loads(content)
        return [model_cls.model_validate(item) for item in raw_data]
    except Exception as e:
        print(f"[S3] Falha ao ler cache do S3: {e}")
        return None


def _write_to_s3_sync(cache_key: str, data: List[BaseModel]):
    """
    Escreve os dados serializados no S3.
    """
    try:
        object_key = _get_object_key(cache_key)
        payload = json.dumps([item.model_dump() for item in data], ensure_ascii=False)
        s3.put_object(Body=payload.encode("utf-8"), Bucket=BUCKET_NAME, Key=object_key)
    except Exception as e:
        print(f"[S3] Falha ao salvar cache no S3: {e}")


def write_to_s3_async(cache_key: str, data: List[BaseModel]):
    """
    Dispara a gravação assíncrona dos dados no S3.
    """
    thread = threading.Thread(target=_write_to_s3_sync, args=(cache_key, data))
    thread.start()
