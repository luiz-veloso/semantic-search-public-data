# Semantic Search over Public Government Contracts (RAG)

A semantic search and question-answering system over Brazilian public contracts using embeddings, FAISS, and a local language model (LLM).

---

## Problem

Public contract datasets are large and difficult to explore:

* Keyword search is limited
* Information is unstructured
* Hard to answer questions directly

---

## Solution

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that allows:

* Semantic search over contracts
* Natural language queries
* Answer generation based on real data

---

## How it works

```text
Dataset (CSV - Transparency Portal)
        ↓
Pandas (data loading & preprocessing)
        ↓
Embeddings (Sentence Transformers)
        ↓
FAISS (vector search)
        ↓
Top-K relevant contracts
        ↓
Local LLM (Gemma2 via Ollama)
        ↓
Generated answer + supporting evidence
```

---

## Technologies

* Python
* Pandas
* Sentence Transformers
* FAISS
* Ollama (local LLM - Gemma2)
* Requests (communication with local model)

---

## Dataset

Source: Brazilian Transparency Portal

File used:

* `Contracts / Purchases`

Main fields:

* `Objeto` → contract description
* `Nome Órgão` → organization name

---

## How to run

### 1. Clone the repository

```bash
git clone https://github.com/luiz-veloso/semantic-search-public-data.git
cd semantic-search-public-data
```

---

### 2. Create environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Install and run the local model

Install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Download model:

```bash
ollama pull gemma2
```

Run model:

```bash
ollama run gemma2
```

---

### 4. Add dataset

Place the CSV file in:

```text
data/202601_Compras.csv
```

---

### 5. Run the application

```bash
python app.py
```

---

## Example usage

### Input

```
Question: contracts related to information technology
```

### Output

```
Answer:
Contracts related to information technology mainly involve
equipment acquisition, software licensing, and automation solutions...

Retrieved context:
[score: ...] Contracting technology solutions...
[score: ...] Software licensing acquisition...
```

---

## Key Features

* Uses **real public data**
* Complete **RAG pipeline**
* Semantic search (not keyword-based)
* Runs **100% locally (no external API required)**
* Modular and extensible architecture

---

## Limitations

* Depends on quality of contract descriptions (`Objeto`)
* No model fine-tuning
* Answers depend on retrieved context quality

---

## Future Improvements

* Web interface (Streamlit or FastAPI)
* Better retrieval (ranking / re-ranking)
* Support for multiple datasets
* Evaluation metrics for answer quality

---

## Project Structure

```text
src/
 ├── ingest.py
 ├── embed.py
 ├── index.py
 ├── query.py
 └── generate.py

app.py
data/
requirements.txt
```

---

## Author

This project demonstrates practical skills in:

* Applied NLP
* Vector search
* LLM-based systems

---

## License

MIT

---

## Important Note

This system does **not rely on keyword search**.
Answers are generated using semantic similarity + retrieved context.

---
