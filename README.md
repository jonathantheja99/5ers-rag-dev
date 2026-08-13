# 🚀 The 5ers RAG Knowledge Base

Welcome to the **5ers RAG (Retrieval-Augmented Generation) Knowledge Base** repository! 

This repository was designed to act as the single source of truth for an automated AI Agent built on **Google AI Studio**. It aggregates and compiles comprehensive FAQ data from [The 5%ers](https://the5ers.com/faqs/) into a format that Large Language Models can easily digest.

## 🌟 What is this project?
The goal of this project is to provide a highly accurate, RAG-based AI assistant for The 5%ers platform. Since program rules, pricing, and FAQs change over time, this repository automates the extraction and compilation of that data.

Instead of manually feeding an AI updated information, this system:
1. **Scrapes** the latest FAQ and Hypergrowth program data.
2. **Compiles** it into a single, clean markdown file (`data/faq_data.md`).
3. **Integrates** directly into Google AI Studio as the ground truth context for the custom agent.

## 📂 Repository Structure

- `data/faq_data.md` - The master compiled FAQ markdown file. This is the file that is uploaded to Google AI Studio.
- `backend/` - Contains the Python-based data scraper (`scraper.py`), the markdown compiler (`compiler.py`), and the core LangChain RAG prototype (`agent.py`).
- `frontend/` - Contains a sleek, glassmorphism-themed React/Vite UI built as an interactive chat prototype.
- `.github/workflows/scrape.yml` - A GitHub Action that runs automatically every Sunday to re-scrape the latest data from The 5%ers website, ensuring the AI agent's knowledge base is never out of date.

## ⚙️ Automated Updates

To guarantee the agent is always giving the right answers regarding leverage, account sizes, pricing, or rules, a **GitHub Action** triggers weekly. It runs the Python scraper, updates `data/faq_data.md`, and commits the changes directly to this repository.

## 🤝 Using with Google AI Studio

To use this data:
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Create a new prompt or agent.
3. Upload `data/faq_data.md` as a knowledge source.
4. The agent will now have comprehensive knowledge of all Bootcamp, High Stakes, and Hyper Growth programs.

---
*Maintained by [@jonathantheja99](https://github.com/jonathantheja99)*
