# 🚀 Scalable Data Extraction, Cleaning & NLP Pipeline

An end-to-end Python data pipeline designed to ingest raw data, execute dynamic data sanitization at scale using memory-efficient chunking, and perform automated NLP Sentiment Analysis on customer feedback.

---

## 🌟 Key Features
- **Scalable Data Ingestion:** Processes multi-gigabyte CSV datasets in configurable batches (`chunksize`) using Pandas to avoid memory (`MemoryError`) crashes.
- **Automated Data Sanitization:** Strips leading/trailing whitespace, standardizes text casing, enforces correct data types, and imputes missing numeric values.
- **Regex Validation:** Uses Regular Expressions to detect malformed data entries (such as email syntax validation).
- **AI/NLP Sentiment Analysis:** Employs Natural Language Processing (`TextBlob`) to score text polarity and classify reviews into Positive, Negative, or Neutral sentiment categories.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Processing:** Pandas, RegEx, OS
- **AI / NLP:** TextBlob

---

## 📁 Repository Structure

```text
data-cleaning-nlp-pipeline/
│
├── data/
│   ├── raw_data.csv             # Sample raw dataset
│   └── cleaned_data.csv         # Processed clean output dataset
│
├── src/
│   ├── clean_pipeline.py        # Scalable Data Cleaning Pipeline
│   └── sentiment_analysis.py    # AI / NLP Sentiment Analysis Script
│
├── requirements.txt             # Dependencies
└── README.md                    # Project documentations