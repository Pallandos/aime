import re

def bloc_1(texte):
    # Compiler l'expression rationnelle
    pattern = re.compile(r'HISTOIRE DE LA MALADIE(.*?)EXAMEN CLINIQUE', re.DOTALL)
    pattern2 = re.compile(r'SYNTHESE DE L\'HOSPITALISATION(.*?)TRAITEMENT DE SORTIE', re.DOTALL)
    pattern3 = re.compile(r'MOTIF D\'HOSPITALISATION(.*?)MEDECIN ADRESSEUR', re.DOTALL)

    # Utiliser search pour trouver le texte entre les deux phrases
    match = pattern.search(texte)
    match2 = pattern2.search(texte)
    match3 = pattern3.search(texte)

    # Initialiser les variables pour éviter l'erreur d'accès
    partie_1 = ""
    partie_2 = ""
    partie_3 = ""

    if match:
        partie_1 = match.group(1).strip()
    if match2:
        partie_2 = match2.group(1).strip()
    if match3:
        partie_3 = match3.group(1).strip()

    if not (match or match2 or match3):
        print("Aucun texte trouvé entre les deux phrases.")

    return [partie_1, partie_2, partie_3]