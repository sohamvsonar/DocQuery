import streamlit as st
import os
from langchain.llms import GooglePalm
from langchain_community.embeddings import GooglePalmEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from langchain_community.callbacks import get_openai_callback


# Set your API key as an environment variable
os.environ['GOOGLE_API_KEY'] = "your_google_api_key"

text = ""

def main():
    global text
    st.set_page_config("LangChain application to chat with PDFs")
    st.header("Ask a Question")

    pdf = st.file_uploader("Upload your PDF", type="pdf")

    if pdf is not None:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        except Exception as e:
            st.error(f"Error reading PDF: {e}")
            return

    if not text:
        st.error("Upload a PDF file.")
        return

    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )

    chunks = text_splitter.split_text(text)

    if not chunks:
        st.error("Error: Text chunks not generated.")
        return

    embeddings = GooglePalmEmbeddings()
    if not embeddings:
        st.error("Error: Embeddings not generated.")
        return

    knowledge = FAISS.from_texts(chunks, embeddings)
    if not knowledge:
        st.error("Error: Knowledge not generated.")
        return

    user = st.text_input("Ask a question about your PDFs: ")
    
    if user:
        docs = knowledge.similarity_search(user)
        llm = GooglePalm()
        chain = load_qa_chain(llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user)
            print(cb)
        st.write(response)

main()
 