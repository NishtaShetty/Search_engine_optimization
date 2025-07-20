
# 🔍 Search Engine Optimization Project

This project implements a lightweight and efficient text-based search engine using Python. It features modules for **preprocessing**, **duplicate detection using SimHash**, **inverted index construction**, **vocabulary compression using front coding**, and a **Flask-based web interface** for querying the dataset.

---

## 🚀 Features

- **Text Preprocessing**: Tokenization, stopword removal, and text cleaning using NLTK.
- **SimHash Deduplication**: Identifies and filters near-duplicate documents using SimHash.
- **Inverted Index**: Enables fast keyword-based search across large text corpora.
- **Front Coding Compression**: Compresses vocabulary to save memory using shared prefixes.
- **Search Interface**: Web interface built with Flask for user queries and displaying results.

---

## 📁 Directory Structure

```
project_root/
├── data/
│   ├── cleaned/             # Preprocessed .txt files
│   ├── unique_files/        # Unique documents after SimHash deduplication
├── index/
│   ├── inverted_index.json  # Final inverted index
│   └── compressed_vocab.txt # Compressed vocabulary file (front coded)
├── scripts/
│   ├── preprocess.py        # Text preprocessing
│   ├── generatesimhash.py   # SimHash deduplication
│   ├── build_index.py       # Inverted index construction
│   ├── front_coding.py      # Front coding compression
│   └── search.py            # Command-line search interface
├── web/
│   ├── app.py               # Flask server
│   ├── templates/
│   │   └── index.html       # Search UI
│   └── static/
│       └── main.js          # Frontend logic
└── README.md
```

---

## 📜 Main Scripts

- `scripts/preprocess.py`: Cleans and tokenizes text data using NLTK.
- `scripts/generatesimhash.py`: Removes near-duplicate documents using SimHash.
- `scripts/build_index.py`: Constructs the inverted index from unique files.
- `scripts/front_coding.py`: Compresses the vocabulary using front coding.
- `scripts/search.py`: Enables search from the command line using the index.
- `web/app.py`: Flask app for the web-based search interface.

---

## ⚙️ How to Run

### 1. Install Dependencies

```bash
pip install flask simhash nltk
```

### 2. Download NLTK Resources

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 3. Run the Pipeline

```bash
# Preprocess text
python scripts/preprocess.py

# Deduplicate using SimHash
python scripts/generatesimhash.py

# Build inverted index
python scripts/build_index.py

# Apply front coding compression
python scripts/front_coding.py
```

### 4. Start the Web Server

```bash
cd web
python app.py
```

### 5. Use the Interface

Open your browser and go to:  
`http://127.0.0.1:5000`

---

## 📌 Notes

- Modify the SimHash threshold in `generatesimhash.py` for stricter or more lenient deduplication.
- Ensure all required folders (`data/`, `index/`, etc.) exist or are created by the scripts.
- The web UI currently displays basic search results based on exact keyword match.

---

## 🧰 Tools & Techniques

- **Languages & Libraries**: Python 3, NLTK, SimHash, Flask, JSON
- **Concepts Used**:
  - Text Preprocessing
  - SimHash for near-duplicate detection
  - Inverted Indexing
  - Front Coding Compression
  - Boolean Search Logic

---

## 📄 License

MIT License
