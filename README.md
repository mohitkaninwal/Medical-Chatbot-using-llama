# 🧠 Medical Chatbot Using Local LLM and Vector Search

A **local LLM-powered medical chatbot** that intelligently answers user queries using a medical book PDF as its knowledge base. The chatbot processes the PDF, creates embeddings, stores them in Pinecone, and retrieves the most relevant context to generate responses using a local LLaMA2 model.

---

## 📌 Features

- 🔍 **PDF Knowledge Base**: Ingests and indexes a medical textbook.
- 🧠 **Local LLM (LLaMA2)**: Generates responses without relying on cloud APIs.
- 🧾 **Semantic Search**: Retrieves relevant content using vector similarity.
- 🧰 **Embeddings**: HuggingFace Sentence Transformers for text vectorization.
- 🌲 **Pinecone**: Cloud vector database for storing and retrieving embeddings.
- 🌐 **Flask Frontend**: Simple HTML UI to interact with the chatbot.

---

## 🖼️ Demo Screenshots

> 📸 Upload your UI/UX screenshots in the `images/` folder and display them here.

| Chat UI | LLM Response |
|---------|--------------|
| ![Chat UI](https://github.com/user-attachments/assets/5d70a5e9-0659-4c7c-8216-67d645e3ed2c) | ![LLM Reply](https://github.com/user-attachments/assets/40c55aaf-9868-4f99-aeea-3fba5b2b2f1f) |


---

## 🛠️ Tech Stack

| Component            | Library/Tool                  |
|----------------------|-------------------------------|
| Language Model       | LLaMA2 (local)                |
| Embeddings           | `sentence-transformers`       |
| Vector DB            | Pinecone                      |
| Backend Logic        | LangChain                     |
| Web Framework        | Flask                         |
| UI                   | HTML/CSS (Bootstrap)          |

---

## 🧩 Architecture

```mermaid
graph TD
    A[User Query] --> B[Flask Frontend]
    B --> C[LangChain Chain]
    C --> D[Pinecone Vector Search]
    C --> E[LLaMA2 Local LLM]
    D --> C
    E --> C
    C --> F[Final Response to User]
