
import streamlit as st
import fitz  # PyMuPDF
import docx
import spacy

st.title("📄 Document Theme Identifier")

uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_themes(text):
    doc = nlp(text)
    themes = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "GPE", "PRODUCT", "EVENT", "PERSON", "WORK_OF_ART"]]
    return list(set(themes))

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_docx(uploaded_file)

    st.subheader("Extracted Text")
    st.write(text[:1000] + "...")  # Display first 1000 characters

    st.subheader("Identified Themes")
    themes = extract_themes(text)
    st.write(themes if themes else "No clear themes identified.")
