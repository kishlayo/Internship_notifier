# 📢 Internship Notifier

A learning project to build an automated system that finds internship and job opportunities online and notifies me when new ones appear.

This project is being developed step by step while learning Python automation, web data extraction, and basic system design.

---

## 🎯 Motivation

While searching for internships, I realized that the hardest part isn’t applying — it’s finding the right opportunities on time.

Many publicly available job scrapers:
- break when websites change  
- get blocked or stop working unexpectedly  
- rely on heavy scraping  
- or return duplicate and irrelevant results  

This project explores a simpler and more reliable approach using **public RSS feeds and structured data**, without requiring logins or personal information.

---

## 🚧 Current Status

This project is a **work in progress**.

### Implemented
- RSS-based job feed scanning
- Keyword-based filtering
- Location-based filtering
- Duplicate detection across runs
- Result summary and count

### Planned
- Email notifications
- Automation using GitHub Actions
- Internship-specific filtering
- Support for multiple data sources

---

## 🛠️ Tech Stack

- Python
- feedparser
- Git & GitHub

---

## ▶️ Usage

1. Clone the repository:
```bash
git clone https://github.com/kishlayo/Internship_notifier.git
cd Internship_notifier
```
2.Install dependencies:
```bash
pip install feedparser
```
3. Run the scanner:
```bash
python scanner.py
```
