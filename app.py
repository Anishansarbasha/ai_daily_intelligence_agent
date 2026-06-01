import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

from rss_fetcher import fetch_all_articles
from deduplicator import remove_duplicates
from news_analyzer import create_report

# -----------------------------
# LOAD ENVIRONMENT VARIABLES
# -----------------------------
load_dotenv()

EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

if not EMAIL or not EMAIL_PASSWORD:
    print("❌ EMAIL or EMAIL_PASSWORD not found")
    exit()

# -----------------------------
# FETCH ARTICLES FROM RSS FEEDS
# -----------------------------
print("📡 Fetching articles from RSS feeds...")

articles = fetch_all_articles()
if len(articles) == 0:
    print("❌ No articles fetched")
    exit()

print(f"Total Articles Fetched: {len(articles)}")

# -----------------------------
# REMOVE DUPLICATES
# -----------------------------
articles = remove_duplicates(articles)

print(f"Unique Articles: {len(articles)}")

# -----------------------------
# GENERATE AI REPORT
# -----------------------------
report = create_report(articles)

print("\n")
print(report)

# -----------------------------
# EMAIL CONTENT
# -----------------------------
news_content = report + "\n\n"

news_content += "📰 Top News Headlines\n\n"

for article in articles[:10]:

    title = article.get("title", "No Title")

    summary = article.get(
        "summary",
        article.get("description", "No Description")
    )

    news_content += f"📰 {title}\n"

    news_content += f"{summary}\n\n"

    news_content += "-" * 50 + "\n\n"

# -----------------------------
# CREATE EMAIL
# -----------------------------
msg = MIMEText(news_content, "plain", "utf-8")

from datetime import datetime

today = datetime.now().strftime("%d-%m-%Y")

msg["Subject"] = (
    f"📅 AI & Tech Daily Intelligence Report - {today}"
)

msg["From"] = EMAIL

msg["To"] = EMAIL

# -----------------------------
# SEND EMAIL
# -----------------------------
try:

    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        server.starttls()

        server.login(
            EMAIL,
            EMAIL_PASSWORD
        )

        server.send_message(msg)

    print("✅ Email Sent Successfully!")

except Exception as e:

    print("❌ Email Error:", e)