from collections import Counter

def create_report(news_articles):

    report = "📅 AI & Tech Daily Intelligence Report\n\n"

    # ---------------------------
    # TOP TRENDS
    # ---------------------------
    report += "Top Trends:\n"

    titles = []

    for article in news_articles:

        title = article.get("title", "No Title")

        titles.append(title)

        report += f"• {title}\n"

    # ---------------------------
    # KEYWORD ANALYSIS
    # ---------------------------
    text = " ".join(titles).lower()

    keywords = [
        "ai",
        "artificial intelligence",
        "openai",
        "google",
        "microsoft",
        "meta",
        "anthropic",
        "nvidia",
        "cloud",
        "data",
        "security",
        "cybersecurity",
        "bitcoin",
        "agent",
        "agents",
        "llm",
        "robotics"
    ]

    found_keywords = []

    for word in keywords:

        count = text.count(word)

        for _ in range(count):
            found_keywords.append(word)

    keyword_count = Counter(found_keywords)

    # ---------------------------
    # KEY INSIGHTS
    # ---------------------------
    report += "\n\nKey Insights:\n"

    if keyword_count:

        for word, count in keyword_count.most_common(5):

            report += f"• {word.upper()} appeared {count} times\n"

    else:

        report += "• No major trend detected\n"

    # ---------------------------
    # RECOMMENDED SKILLS
    # ---------------------------
    report += "\n\nRecommended Skills:\n"

    skills = []

    if "ai" in text:
        skills.append("AI Agents")

    if "agent" in text or "agents" in text:
        skills.append("LangGraph")

    if "cloud" in text:
        skills.append("Cloud Computing")

    if "data" in text:
        skills.append("Data Analysis")

    if "security" in text or "cybersecurity" in text:
        skills.append("Cyber Security")

    if "robotics" in text:
        skills.append("Robotics & Physical AI")

    # Always include Python
    skills.append("Python")

    # Remove duplicates
    skills = list(set(skills))

    for skill in skills:

        report += f"• {skill}\n"

    # ---------------------------
    # OVERALL ANALYSIS
    # ---------------------------
    report += "\n\nOverall Analysis:\n\n"

    if keyword_count:

        most_topic = keyword_count.most_common(1)[0][0]

        report += f"Most discussed topic: {most_topic.upper()}\n"

    else:

        report += "Most discussed topic: Unknown\n"

    # Most active company
    companies = [
        "openai",
        "google",
        "microsoft",
        "meta",
        "anthropic",
        "nvidia"
    ]

    company_counts = {}

    for company in companies:

        company_counts[company] = text.count(company)

    most_active_company = max(
        company_counts,
        key=company_counts.get
    )

    report += (
        f"Most active company: "
        f"{most_active_company.capitalize()}\n"
    )

    # Most growing skill
    if "agent" in text or "agents" in text:

        report += "Most growing skill: AI Agents\n"

    elif "cloud" in text:

        report += "Most growing skill: Cloud Computing\n"

    elif "data" in text:

        report += "Most growing skill: Data Analysis\n"

    else:

        report += "Most growing skill: Python\n"

    # Market Direction
    report += (
        "Market direction: Enterprise AI adoption "
        "and automation are increasing\n"
    )

    return report