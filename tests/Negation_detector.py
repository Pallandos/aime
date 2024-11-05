#Tuto:
#https://medkit-lib.org/user_guide/first_steps.html

#pip install medkit-lib

from pathlib import Path
from medkit.core.text import TextDocument
from medkit.text.segmentation import SentenceTokenizer
from medkit.text.segmentation import SyntagmaTokenizer
from medkit.text.ner.hf_entity_matcher import HFEntityMatcher
from medkit.text.context import NegationDetector, NegationDetectorRule
from medkit.text.ner import RegexpMatcher, RegexpMatcherRule

#importation du texte
doc = TextDocument.from_file(Path(r"C:\Users\Administrateur\Documents\ENSTA Bretagne\2A\aime\tests\ENSTAP1.txt"))

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

for entity in entities:
    neg_attr = entity.attrs.get(label="is_negated")[0]
    if neg_attr.value and entity.label == "problem":
        print(f"text='{entity.text}', label={entity.label}, is_negated={neg_attr.value}")
    #print(f"text='{entity.text}', label={entity.label}, is_negated={neg_attr.value}")

# #affichage des entités
# msg = "|".join(f"'{entity.label}':{entity.text}" for entity in detected_entities)
# print(msg)