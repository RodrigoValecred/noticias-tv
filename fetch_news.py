import feedparser
import json
from datetime import datetime
import time

# URL do feed RSS de notícias. Usando o do Google Notícias para o Brasil.
RSS_URL = "https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-BR"
OUTPUT_FILE = "news.json"
MAX_ITEMS = 6

def fetch_and_process_news():
    """
    Busca notícias de um feed RSS, processa os dados e salva em um arquivo JSON.
    """
    print(f"Buscando notícias do feed: {RSS_URL}")
    feed = feedparser.parse(RSS_URL)

    if feed.bozo:
        print(f"Erro ao processar o feed: {feed.bozo_exception}")
        return

    news_list = []
    for entry in feed.entries[:MAX_ITEMS]:
        # O título da notícia geralmente está no campo 'title'
        title = entry.get("title", "Sem título")

        # A fonte da notícia pode estar no campo 'source' ou 'author'
        source = entry.get("source", {}).get("title", "Fonte desconhecida")

        # O feedparser já converte a data para uma estrutura padrão (time.struct_time)
        # Vamos convertê-la para o formato ISO 8601, que é o padrão do JSON
        timestamp_struct = entry.get("published_parsed", time.gmtime())
        timestamp_iso = datetime.fromtimestamp(time.mktime(timestamp_struct)).isoformat() + "Z"

        news_list.append({
            "source": source,
            "title": title,
            "timestamp": timestamp_iso
        })

    if not news_list:
        print("Nenhuma notícia encontrada no feed.")
        return

    print(f"{len(news_list)} notícias processadas. Salvando em {OUTPUT_FILE}...")
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(news_list, f, ensure_ascii=False, indent=4)
        print(f"Arquivo {OUTPUT_FILE} atualizado com sucesso.")
    except IOError as e:
        print(f"Erro ao escrever no arquivo {OUTPUT_FILE}: {e}")

if __name__ == "__main__":
    fetch_and_process_news()