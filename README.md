# Information Retrieval System

A complete local information retrieval system implementing hybrid BM25 + TF-IDF retrieval for CS 516: Information Retrieval and Text Mining course.

Repository: [https://github.com/mscs24025-cmyk/ir_system.git](https://github.com/mscs24025-cmyk/ir_system.git)

## Features

- Hybrid Retrieval**: Combines BM25 and TF-IDF for improved ranking
- Text Preprocessing**: Normalization, tokenization, stopword removal, and stemming
- Efficient Indexing**: Fast retrieval with pre-built indexes
- Evaluation Metrics**: Precision@K, Recall@K, MRR, MAP
- Fully Local**: No cloud dependencies

## Requirements

- Python 3.8+
- See `requirements.txt` for dependencies

## Installation

1. Clone this repository:
```bash
git clone https://github.com/mscs24025-cmyk/ir_system.git
cd ir_system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download NLTK data (if not auto-downloaded):
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Dataset

Place your `Articles.csv` file in the `dataset/` directory with the following columns:
- `Article`: Main text content
- `Heading`: Article headline
- `Date`: Publication date
- `NewsType`: Category/type

## Usage

### Interactive Search

Run the interactive search interface:
```bash
python run_system.py
```

### Command Line Query

Execute a single query:
```bash
python -m src.main --query "your search query"
```

### Rebuild Index

To rebuild the index from scratch:
```bash
python -m src.main --rebuild
```

### Evaluate System

Run evaluation metrics:
```bash
python evaluate_system.py
```

## System Architecture

1. Preprocessing: Normalizes, tokenizes, removes stopwords, and stems text
2. Indexing: Builds BM25 and TF-IDF indexes
3. Retrieval: Combines BM25 and TF-IDF scores for ranking
4. Evaluation: Computes standard IR metrics

## Project Structure

```
ir_system/
├── dataset/
│   └── Articles.csv
├── src/
│   ├── __init__.py
│   ├── preprocessor.py      # Text preprocessing
│   ├── indexer.py           # Indexing (BM25 + TF-IDF)
│   ├── retriever.py         # Retrieval and ranking
│   ├── evaluator.py         # Evaluation metrics
│   └── main.py              # Main interface
├── requirements.txt
├── README.md
├── run_system.py            # Entry point
└── evaluate_system.py       # Evaluation script
```

## Evaluation

The system supports standard IR evaluation metrics:
- Precision@K: Fraction of retrieved documents that are relevant
- Recall@K: Fraction of relevant documents that are retrieved
- MRR (Mean Reciprocal Rank): Average of reciprocal ranks of first relevant document
- MAP (Mean Average Precision): Mean of average precision scores

To evaluate the system, use the `IREvaluator` class in `src/evaluator.py`:

```python
from src.evaluator import IREvaluator
from src.retriever import IRRetriever

# ... build retriever ...

results = retriever.retrieve("query", top_k=10)
relevant_docs = [0, 5, 12]  # Known relevant document IDs

metrics = IREvaluator.evaluate_retrieval(
    [(doc_id, score) for doc_id, score, _, _ in results],
    relevant_docs,
    k_values=[1, 5, 10]
)
```

## Technical Details
### Preprocessing Pipeline
1. Normalization: Remove special characters, normalize whitespace
2. Lowercasing: Convert to lowercase
3. Tokenization: Split into words using NLTK
4. Stopword Removal: Remove common English stopwords
5. Stemming: Apply Porter stemmer
### Retrieval Strategy
- BM25: Okapi BM25 algorithm for term frequency and document length normalization
- TF-IDF: Term frequency-inverse document frequency weighting
- Hybrid Scoring: Weighted combination (default: 60% BM25, 40% TF-IDF)
### Index Storage
Indexes are saved as pickle files for fast loading. The index includes:
- BM25 index
- TF-IDF vectorizer and matrix
- Original documents
- Processed documents
- Document metadata
