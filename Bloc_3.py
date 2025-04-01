import pdfplumber
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Charger le modèle BioLORD depuis Hugging Face
model = SentenceTransformer('C:\\Users\\roman\\Desktop\\Ensta_2024\\Projet_AIME\\BioLORD-2023-M')
D = []
C = []


with open('descriptions.txt', 'r', encoding='utf-8') as fichier:
    for ligne in fichier:
        D.append(ligne)

with open('codes.txt', 'r', encoding='utf-8') as fichier:
    for ligne in fichier:
        C.append(ligne)


icd10_embeddings = model.encode(D)

# Exemples de descriptions médicales extraites
medical_descriptions = [
    "Ingestion excessive de nourriture suivis de comportements compensatoires",
    "Le patient présente une consommation régulière de cannabis",
    "Exposition inappropriée d'attributs corporels en public"
]

# Encoder les descriptions médicales
medical_embeddings = model.encode(medical_descriptions)

similarities = cosine_similarity(medical_embeddings, icd10_embeddings)

for i, medical_descriptions in enumerate(medical_descriptions):
    # Tri des indices par ordre décroissant de similarité
    best_match_indices = np.argsort(similarities[i])[::-1]

    # Récupération des trois meilleures correspondances
    best_match_index = best_match_indices[0]  # Premier maximum
    second_best_match_index = best_match_indices[1] # Deuxième maximum
    third_best_match_index = best_match_indices[2] # Troisième maximum

    best_icd10_description = D[best_match_index]
    best_icd10_code = C[best_match_index]
    second_best_icd10_description = D[second_best_match_index]
    second_best_icd10_code = C[second_best_match_index]
    third_best_icd10_description = D[third_best_match_index]
    third_best_icd10_code = C[third_best_match_index]
    print(f"Description médicale: {medical_descriptions}")
    print(f"Code ICD-10 correspondante: {best_icd10_code, second_best_icd10_code, third_best_icd10_code}")
    print(f"Description ICD-10 correspondante: {best_icd10_description, second_best_icd10_description, third_best_icd10_description}")