import streamlit as st
from pypdf import PdfReader

# TITLE
st.title("📚 Simple Research PDF Chatbot")

# PDF TEXT EXTRACT
def get_pdf_text(pdf):

    text = ""

    pdf_reader = PdfReader(pdf)

    for page in pdf_reader.pages:

        content = page.extract_text()

        if content:
            text += content

    return text

# FILE UPLOAD
pdf = st.file_uploader(
    "Upload Research Paper PDF",
    type="pdf"
)

# PROCESS PDF
if pdf is not None:

    text = get_pdf_text(pdf)

    st.success("PDF Uploaded Successfully ✅")

    # QUESTION INPUT
    question = st.text_input("Ask Question from PDF")

    if question:

        # SIMPLE SEARCH
        if question.lower() in text.lower():

            st.write("✅ Answer Found in PDF")

        else:

            st.write("❌ Answer not found")
