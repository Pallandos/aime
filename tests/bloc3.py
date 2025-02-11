import pdfplumber
from sentence_transformers import SentenceTransformer
import time
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


from pathlib import Path
from medkit.core.text import TextDocument
from medkit.text.segmentation import SentenceTokenizer
from medkit.text.segmentation import SyntagmaTokenizer
from medkit.text.ner.hf_entity_matcher import HFEntityMatcher
from medkit.text.context import NegationDetector, NegationDetectorRule
from medkit.text.ner import RegexpMatcher, RegexpMatcherRule


#importation du texte
doc = TextDocument.from_file(Path(r"C:\Projets_pycharm\AIME\ENSTAP1.txt"))
#initialisation du tokenizer de phrases
sent_tokenizer = SentenceTokenizer(
    output_label="sentence",
    punct_chars=[".", "?", "!"],
)

#segmentation du texte en phrases
sentences = sent_tokenizer.run([doc.raw_segment])

# #affichage des phrases
# for sentence in sentences:
#     print(f"uid={sentence.uid}")
#     print(f"text={sentence.text!r}")
#     print(f"spans={sentence.spans}, label={sentence.label}\n")

#initialisation du tokenizer de syntagmes
synt_tokenizer = SyntagmaTokenizer(
    output_label="syntagma",
    separators=[r"\bmais\b", r"\bet\b"],
)

#segmentation des phrases en syntagmes
syntagmas = synt_tokenizer.run(sentences)





#Détection des négations

#initialisation des règles de détection
neg_rules = [
    NegationDetectorRule(regexp=r"\bpas\s*d[' e]\b"),
    NegationDetectorRule(regexp=r"\bsans\b", exclusion_regexps=[r"\bsans\s*doute\b"]),
    NegationDetectorRule(regexp=r"\bne\s*semble\s*pas"),
]
#initialisation du détecteur de négations
neg_detector = NegationDetector(output_label="is_negated", rules=neg_rules)
#détection des négations
neg_detector.run(syntagmas) #ne renvoie rien, ajoute un booléan à chaque syntagme pour indiquer si une négation a été détectée ou non

# #affichage des syntagmes avec négation
# for syntagma in syntagmas:
#     neg_attr = syntagma.attrs.get(label="is_negated")[0]
#     if neg_attr.value:
#         print(syntagma.text)

#Entity Matcher

#initialisation du matcher
matcher = HFEntityMatcher(model="medkit/DrBERT-CASM2", attrs_to_copy=["is_negated"])

#detection des entités
entities = matcher.run(syntagmas)

#for entity in entities:
    #neg_attr = entity.attrs.get(label="is_negated")[0]
    #if neg_attr.value and entity.label == "problem":
        #print(f"text='{entity.text}', label={entity.label}, is_negated={neg_attr.value}")
    #print(f"text='{entity.text}', label={entity.label}, is_negated={neg_attr.value}")

# #affichage des entités
# msg = "|".join(f"'{entity.label}':{entity.text}" for entity in detected_entities)
# print(msg)

#problem = []
#for entity in entities:
#    problem.append(entity.text)


# Charger le modèle BioLORD depuis Hugging Face
model = SentenceTransformer('C:/Projets_pycharm/AIME/Scripts/BioLORD-2023-M')
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
    print(f"Description ICD-10 correspondante: {best_icd10_description, second_best_icd10_description, third_best_icd10_d
