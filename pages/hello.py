import streamlit as st

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

st.write("# Welcome to DocGPT! 👋")

st.markdown(
    """
    **DocGPT** is an innovative web application developed using Streamlit. It allows users to upload PDF documents and interact with them through an intelligent chatbot. The application leverages advanced technologies such as the **Retrieval-Augmented Generation (RAG)** architecture and **Large Language Models (LLM)** to provide accurate and context-aware responses. With the integration of the **Groq API** for enhanced performance, **DocGPT** ensures efficient and reliable document interaction. The user-friendly interface makes it easy for users to upload documents and query information seamlessly.

    ### DocGPT WorkFlow!

    ![DocGPT WorkFlow](https://media.giphy.com/media/3o7aD5tv1ogNBtDhDi/giphy.gif)
    
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
