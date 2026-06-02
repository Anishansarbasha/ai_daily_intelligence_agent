# InsightPulse AI

### Automated Technology Intelligence Agent

## Overview

InsightPulse AI is an automated intelligence agent that collects the latest AI, Data Science, Cloud, Cybersecurity, and Technology news from multiple RSS sources, analyzes trends, and delivers a daily intelligence report directly to the user's email.

The system runs automatically using GitHub Actions, allowing users to receive daily updates even when their computer is turned off.

---

## Problem Statement

Technology professionals and students often spend significant time browsing multiple websites to stay updated with industry trends, emerging technologies, and important news.

---

## Solution

InsightPulse AI automates the entire process by:

* Fetching news from multiple RSS sources
* Removing duplicate articles
* Identifying trending topics and technologies
* Generating intelligence-based insights
* Recommending relevant skills
* Sending a daily email report automatically

---

## Who Can Use This?

* Data Analysts
* Data Scientists
* AI Engineers
* Software Developers
* Students
* Tech Enthusiasts

---

## Tech Stack

* Python
* RSS Feeds
* GitHub Actions
* Gmail SMTP
* Feedparser
* Requests
* Python-Dotenv

---

## Project Structure

| File                             | Purpose                               |
| -------------------------------- | ------------------------------------- |
| app.py                           | Main application workflow             |
| rss_fetcher.py                   | Fetches news articles from RSS feeds  |
| rss_sources.py                   | Stores RSS source URLs                |
| source_reader.py                 | Reads RSS sources from file           |
| deduplicator.py                  | Removes duplicate articles            |
| news_analyzer.py                 | Generates trend analysis and insights |
| sources.txt                      | List of RSS feed sources              |
| requirements.txt                 | Project dependencies                  |
| README.md                        | Project documentation                 |
| .github/workflows/daily_news.yml | Automates daily execution             |

---

## Workflow

RSS Sources → News Collection → Duplicate Removal → Trend Analysis → Intelligence Report → Email Delivery → Daily Automation

---

## Key Features

✅ Automated News Collection

✅ Trend Analysis

✅ Duplicate Removal

✅ Daily Email Reports

✅ Cloud-Based Automation

✅ Runs Even When Laptop Is Off

---

## Author

**Anish Ansarbasha**

*InsightPulse AI is an original project idea developed to automate daily technology intelligence gathering and delivery.*
