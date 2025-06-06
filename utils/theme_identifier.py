import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_themes(text):
    doc = nlp(text)
    themes = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "GPE", "PRODUCT", "EVENT", "PERSON", "WORK_OF_ART"]]
    return list(set(themes))
 
