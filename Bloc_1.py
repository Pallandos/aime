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

    resultats = []

    if match:
        partie_1 = match.group(1).strip()
        resultats.append(partie_1)
    if match2:
        partie_2 = match2.group(1).strip()
        resultats.append(partie_2)
    if match3:
        partie_3 = match3.group(1).strip()
        resultats.append(partie_3)
    else:
        print("Aucun texte trouvé entre les deux phrases.")

    print(partie_1)
    return resultats
