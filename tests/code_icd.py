import pdfplumber
from sentence_transformers import SentenceTransformer
import time
from sklearn.metrics.pairwise import cosine_similarity

# Charger le modèle BioLORD depuis Hugging Face
model = SentenceTransformer('C:/Projets_pycharm/AIME/Scripts/BioLORD-2023-M')
D = []
C = []


with open('ICD-10 descriptions.txt', 'r', encoding='utf-8') as fichier:
    for ligne in fichier:
        D.append(ligne)

with open('ICD-10 codes.txt', 'r', encoding='utf-8') as fichier:
    for ligne in fichier:
        C.append(ligne)


icd10_embeddings = model.encode(D)

# Exemples de descriptions médicales extraites
medical_descriptions = [
    "Nudité excessive en public",
    "Patient avec antécédents d'hypertension"
]

# Encoder les descriptions médicales
medical_embeddings = model.encode(medical_descriptions)

similarities = cosine_similarity(medical_embeddings, icd10_embeddings)

for i, medical_description in enumerate(medical_descriptions):
    best_match_index = similarities[i].argmax()
    best_icd10_description = D[best_match_index]
    best_icd10_code = C[best_match_index]
    print(f"Description médicale: {medical_description}")
    print(f"Code ICD-10 correspondante: {best_icd10_code}")
    print(f"Description ICD-10 correspondante: {best_icd10_description}")
