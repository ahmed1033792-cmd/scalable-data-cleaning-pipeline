# 🚀 Scalable Data Extraction & Cleaning Pipeline

A memory-efficient Python ETL pipeline designed to ingest raw CSV data, perform automated sanitization (trimming whitespace, coercing types, imputing missing values, regex validation), and scale seamlessly across multi-gigabyte files using Pandas chunking.

## 🌟 Key Features
- **Memory-Efficient Processing:** Employs chunking (`chunksize`) to process massive files without exceeding RAM limits.
- **Data Sanitization & Cleaning:** Standardizes text formatting, converts data types, and imputes missing numeric values.
- **Regex Validation:** Detects malformed email entries using Regular Expressions.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Engineering:** Pandas, RegEx, OS

## 📁 Repository Structure
```text
Project_1_Data_Cleaning/
│
├── data/
│   ├── raw_data.csv             # Sample raw input data
│   └── cleaned_data.csv         # Sanitized output data
├── src/
│   └── clean_pipeline.py        # Core ETL cleaning script
├── requirements.txt
└── README.md