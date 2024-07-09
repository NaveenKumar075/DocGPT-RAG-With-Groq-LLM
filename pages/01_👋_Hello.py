import streamlit as st

st.set_page_config(
    page_title="About Us",
    page_icon="👋",
)

st.write("# Welcome to DocGPT! 👋")

st.markdown(
    """
    <div style="text-align: justify;">
    
    **DocGPT** is an innovative web application developed using Streamlit. It allows users to upload PDF documents and interact with them through an intelligent chatbot. The application leverages advanced technologies such as the **Retrieval-Augmented Generation (RAG)** architecture and **Large Language Models (LLM)** to provide accurate and context-aware responses. With the integration of the **Groq API** for enhanced performance, **DocGPT** ensures efficient and reliable document interaction. The user-friendly interface makes it easy for users to upload documents and query information seamlessly.

    ### DocGPT WorkFlow!

    ![DocGPT WorkFlow](https://github.com/NaveenKumar075/DocGPT-RAG-With-Groq-LLM/assets/104119173/547730ea-f3e3-40c0-8a32-1294df34a6de)
    
    The **DocGPT** workflow for the RAG architecture involves several key steps. It starts with document ingestion, followed by text extraction and preprocessing. The data is then chunked and converted into embeddings, which are stored in a vector database. User queries are matched with relevant data through hybrid search and retrieval. The results are processed by an LLM model, enhanced with a prompt template, and the final response is delivered to the user.

    ### Features:
    - **Document Summarization:** Quickly summarize key points from large PDF documents.
    - **Information Retrieval:** Easily find relevant information or specific sections within documents.
    - **Interactive Q&A:** Ask questions about the document content and get precise answers.
    - **Content Analysis:** Analyze and extract data or insights from uploaded documents.
    - **Document Navigation:** Navigate through documents with ease using the chatbot interface

    ### Future Works for DocGPT
    - Implementation of AI Agents for Specific Roles or Tasks
    - Support for All Types of Documents
    - User Chat History Storage

    #### User Feedback Integration:
    - Collect and utilize user feedback to improve and refine our application continuously.
    - **DocGPT** aims to offer a more versatile, user-centric, and powerful document interaction experience.

    </div>
""", unsafe_allow_html=True
)
