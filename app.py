import streamlit as st
from utils.text_extractor import extract_text_from_pdf, extract_text_from_docx
from utils.theme_identifier import extract_themes

st.title("📄 Document Theme Identifier")

uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])

if uploaded_file:
    # Extract text
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_docx(uploaded_file)

    # Show extracted text preview
    st.subheader("Extracted Text")
    st.write(text[:1000] + "...")  # first 1000 chars

    # Show identified themes
    st.subheader("Identified Themes")
    themes = extract_themes(text)
    st.write(themes if themes else "No clear themes identified.")

