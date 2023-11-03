import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Nvidia is developing a graphics card in collaboration with Asus ROG which is estimated tobe worth $500 million and will be launched in New York.")
for ent in doc.ents:
    print(ent.text, ent.label_)