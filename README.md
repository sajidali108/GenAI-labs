# 🧪 genai-labs

A collection of practical GenAI mini-apps and experiments covering LLMs, embeddings, RAG, AI_Agents and prompt engineering using LangChain, Langraph and HuggingFace.

---

## 📌 About

This repo contains hands-on experiments and mini-apps built while exploring Generative AI concepts. Each folder is a self-contained app focusing on a specific GenAI concept or technique. Not polished products but deliberate practice.

---

## 🗂️ Structure

```
genai-labs/
├── 01_similarity_search/       # Semantic similarity using embeddings
├── 02_chatbot/                 # Chatbot using prompt templates (coming soon)
├── 03_rag_app/                 # RAG pipeline (coming soon)
└── ...
```

---

## 🔬 Experiments

| # | App | Concepts Covered | Status |
|---|-----|-----------------|--------|
| 01 | Similarity Search | Embeddings, Cosine Similarity, Vector Search | ✅ Done |
| 02 | Chatbot | Prompt Templates, Chat History, LLM Chains | 🔜 Coming Soon |
| 03 | RAG App | Document Loader, Vector Store, Retrieval Chain | 🔜 Coming Soon |

---

## 🛠️ Tech Stack

- **[LangChain](https://www.langchain.com/)** — LLM application framework
- **[HuggingFace](https://huggingface.co/)** — Open-source models and Inference API
- **[Python](https://www.python.org/)** — Core language
- **[FastAPI](https://fastapi.tiangolo.com/)** *(where applicable)* — API layer

---

## ⚙️ Setup

1. **Clone the repo**
```bash
git clone https://github.com/sajidali108/genai-labs.git
cd genai-labs
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Add your API keys inside .env
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
Groq_API_KEY= your_api_key
```

---

## 📚 References

- [LangChain Docs](https://docs.langchain.com/)
- [HuggingFace Docs](https://huggingface.co/docs)
- [CampusX YouTube](https://www.youtube.com/@campusx-official)

---

## 👤 Author

**Sajid Ali**
- GitHub: [@sajidali108](https://github.com/sajidali108)
- LinkedIn: [sajidali-ai](https://linkedin.com/in/sajidali-ai)

---

