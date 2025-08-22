import meilisearch
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로드

MASTER_key = os.getenv("MAILSEARCH_API_MASTER_KEY")
MAILSEARCH_LOCAL_HOST_t = os.getenv("MAILSEARCH_LOCAL_HOST")

client = meilisearch.Client(MAILSEARCH_LOCAL_HOST_t, MASTER_key)

def stock_search(query):
    return client.index('nasdaq').search(query)