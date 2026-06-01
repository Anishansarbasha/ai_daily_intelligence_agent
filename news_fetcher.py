from source_reader import get_sources

def fetch_news():

    sources = get_sources()

    articles = []

    for source in sources:

        articles.append({
            "title": f"Latest updates from {source}",
            "description": f"Monitoring news and updates from {source}"
        })

    return articles