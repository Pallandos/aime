from transformers import pipeline

# ce fichier réalise une tokenisation d'un texte passé en argument 
# et affiche les résultats dans un fichier txt
# chaque mot sera associé à un tag qui lui est propre, qui correspond à une catégorie grammaticale

# Charger un modèle de base (non-classification)
model_name = "Dr-BERT/CAS-Biomedical-POS-Tagging"

# charger le pipeline
nlp = pipeline('ner', model=model_name)

# Texte à analyser
text = "Au total, aptient de 45 ans présentant une décompensation anxieuse et dépressive réactionnelle à une annonce de séparation de sa conjointe et des difficultés interpersonnelles évoluant depuis deux-trois ans chez un sujet pris en charge pour un neurocytome intraventriculaire présentant des séquelles cognitives post-radique et chirurgicale. Organisation progressive par le SAMSAH d'un retour à domicile avec poursuite du traitement par FLUOXETINE. "

# Analyse du texte
result = nlp(text)

# affichage des resultats dans un txt

with open ('results.txt', 'w', encoding = 'utf-8') as f:
    for r in result:
        f.write(str(r) + '\n')