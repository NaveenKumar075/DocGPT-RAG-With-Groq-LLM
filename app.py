import os
import re
import bs4
import pdfplumber
import streamlit as st
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader

# load the environment variables from the .env file
load_dotenv()

# get API key's from the environmental variables
hugging_face_token = os.getenv('HF_TOKEN')
groq_api_key = os.getenv('GROQ_API_KEY')


# pdf-to-text extraction process
def pdf_text_extraction(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = []
        for page in pdf.pages:
            page_text = page.extract_text(x_tolerance=1, y_tolerance=1)
            if page_text:
                all_text.append(page_text)
        return "\n".join(all_text)


# to remove the non-alphanumeric lines
def text_preprocessing(text):
    lines = text.split('\n')
    alphanumeric_lines = [line for line in lines if re.search(r'\w', line)]
    return "\n".join(alphanumeric_lines)


# splitting the data into chunks
def chunking_data(filtered_text):
    document = Document(page_content=filtered_text)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512,chunk_overlap=64)
    splitted_data = text_splitter.split_documents([document])
    return splitted_data


pdf_path = "Attention Is All You Need.pdf"
text = pdf_text_extraction(pdf_path)
filtered_text = text_preprocessing(text)
splitted_data = chunking_data(filtered_text)
print(text)
print(filtered_text)

# to print the chunking data results
for i, chunk in enumerate(splitted_data):
    print(f"Chunk {i+1}:\n{chunk.page_content}\n")
    

# initializing hugging face embedding - UAE-Large-V1 (Universal AnglE Embedding)
embeddings = HuggingFaceInferenceAPIEmbeddings(api_key=hugging_face_token, model_name="WhereIsAI/UAE-Large-V1")


# words to vectorization and storing them in a chromadb (Vector Database)
vectorstore = Chroma.from_documents(splitted_data, embeddings, persist_directory="./db")
vector_retriever = vectorstore.as_retriever(search_kwargs={"k":2})


# integrating vector_retriever and keyword_retriever (Hybrid Search)
keyword_retriever = BM25Retriever.from_documents(splitted_data).k=2
retriever = EnsembleRetriever(retrievers=[vector_retriever,keyword_retriever], weights= [0.5,0.5])