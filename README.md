
# ⚖️ Law Chatbot – Powered by Groq & RAG

A simple AI chatbot that uses **Groq’s blazing-fast LLM**, **Vector Search (RAG)**, and **Streamlit** to answer questions related to **law**. Perfect for quick legal insights, definitions, and document-based answers.

---

## 🚀 Features

- 💬 Natural-language Q&A powered by Groq's LLM  
- 📚 Vector search over legal documents (RAG)  
- 🧠 Chat memory with Streamlit session state  
- 🎨 Clean, minimal UI  
- ⚡ Fast and lightweight backend  

---

## 📦 Installation & Setup

Follow these steps to set up the chatbot locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/law-chatbot
cd law-chatbot


###2. Create a .env file
In the root folder, create a .env file and add your Groq API key:

```
api_key_grok="your_groq_api_key_here"

```
###3. Install dependencies

```
pip install -r requirements.txt

```
###4. Run the Streamlit app

```
streamlit run main.py

```
##💡 Example Questions
You can ask things like:

"What are my rights during an arrest?"

"Explain Section 498A of the IPC."

"How can I register a legal firm in India?"

"What is natural justice?"

"Difference between civil and criminal law?"

```

###🧠 File Structure

```

├── main.py              # Streamlit app interface
├── llm.py               # vector_search() logic using Groq + RAG
├── requirements.txt     # Python dependencies
├── .env                 # API key (not committed)
└── README.md            # This file

```

###  ✍️ Built by Shivanshu Prajapati

###  ------------screenshot----------------

![App Screenshot](https://github.com/shivanshu099/law_chatbot/blob/main/sc_1.png)

![App Screenshot](https://github.com/shivanshu099/law_chatbot/blob/main/sc_2.png)

![App Screenshot](https://github.com/shivanshu099/law_chatbot/blob/main/sc_3.png)














