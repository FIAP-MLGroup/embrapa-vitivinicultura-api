import json
import boto3
import threading
from typing import List
from pydantic import BaseModel
import os

# Nome do bucket, pode vir de uma variável de ambiente
BUCKET_NAME = os.getenv("S3_CACHE_BUCKET", "embrapa-vitivinicultura-cache")

# Cliente S3
s3 = boto3.client("s3")

def _get_object_key(cache_key: str) -> str:
    return f"{cache_key}.json"

def read_from_s3(cache_key: str, model: type[BaseModel]) -> List[BaseModel] | None:
    try:
        object_key = _get_object_key(cache_key)
        response = s3.get_object(Bucket=BUCKET_NAME, Key=object_key)
        content = response['Body'].read().decode('utf-8')
        data = json.loads(content)
        return [model.model_validate(item) for item in data]
    except Exception:
        return None

def _write_to_s3_sync(cache_key: str, data: List[BaseModel]):
    try:
        object_key = _get_object_key(cache_key)
        payload = json.dumps([item.model_dump() for item in data], ensure_ascii=False)
        s3.put_object(Body=payload.encode("utf-8"), Bucket=BUCKET_NAME, Key=object_key)
    except Exception as e:
        print(f"[S3] Falha ao salvar cache no S3: {e}")

def write_to_s3_async(cache_key: str, data: List[BaseModel]):
    thread = threading.Thread(target=_write_to_s3_sync, args=(cache_key, data))
    thread.start()
