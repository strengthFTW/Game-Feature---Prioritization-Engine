# Game Feature Prioritization Engine (GFPE.SH)

An NLP and Machine Learning pipeline that analyzes 287,937 Steam reviews to generate a data-driven, developer-ready feature priority roadmap.

## Overview
- **Analyzes** massive amounts of raw Steam review data.
- **Categorizes** feedback into 10 distinct game feature areas using a regex keyword taxonomy.
- **Measures** sentiment using VADER.
- **Clusters** reviews using K-Means to discover underlying themes.
- **Outputs** a ranked priority score for game features based on mentions, negative sentiment ratio, and helpfulness weight.

## Tech Stack
- **NLP:** NLTK, spaCy, VADER
- **ML:** scikit-learn (TF-IDF, K-Means)
- **Data:** pandas, Steam API
- **Frontend (Dashboard/Portfolio):** HTML, CSS, vanilla JS, Chart.js

## Project Structure
- `index.html` - The main portfolio landing page showcasing the design and pipeline.
- `dashboard/` - Contains the interactive data visualization dashboard.
- `data/` - Holds raw and processed datasets.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/strengthFTW/Game-Feature---Prioritization-Engine.git
   ```
2. Open `index.html` in your web browser to view the portfolio.
3. Open `dashboard/index.html` in your web browser to view the interactive data dashboard.