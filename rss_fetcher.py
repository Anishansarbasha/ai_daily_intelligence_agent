import feedparser
from source_reader import get_sources

def fetch_all_articles():

    all_articles = []

    sources = get_sources()

    for source in sources:

        try:

            feed = feedparser.parse(source)

            if feed.entries:

                for entry in feed.entries[:5]:

                    all_articles.append(
                        {
                            "title": entry.get("title", "No Title"),
                            "link": entry.get("link", ""),
                            "summary": entry.get("summary", "")
                        }
                    )

        except Exception as e:

            print(f"Error reading {source}: {e}")

    return all_articles