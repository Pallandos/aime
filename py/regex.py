import re

def extract_text(text : str):
    """Extrait le texte entre les sections interessantes du rapport médical.

    Args:
        text (string): compte rendu médical (brut sans mise en forme nécessaire)

    Returns:
        liste (List of string): liste de texte extrait entre les sections (normalement 3 sections)
    """
    sortie = []

    pattern1 = re.compile(r'HISTOIRE DE LA MALADIE(.*?)EXAMEN CLINIQUE', re.DOTALL)
    pattern2 = re.compile(r'SYNTHESE DE L\'HOSPITALISATION(.*?)TRAITEMENT DE SORTIE', re.DOTALL)
    pattern3 = re.compile(r'MOTIF D\'HOSPITALISATION(.*?)MEDECIN ADRESSEUR', re.DOTALL)

    # recherche :
    match1 = pattern1.search(text)
    match2 = pattern2.search(text)
    match3 = pattern3.search(text)

    if match1:
        sortie.append(match1.group(1).strip())
    if match2:
        sortie.append(match2.group(1).strip())
    if match3:
        sortie.append(match3.group(1).strip())
    
    return sortie

if __name__ == "__main__":
    # Texte très long avec des sauts de ligne
    texte = """
    MOTIF D'HOSPITALISATION : Hospitalisation 
    ce jour pour sevrage 1 mois. MEDECIN ADRESSEUR : par le psychiatre du service ANTECEDENTS PERSONNELS : Antécédents Psychiatriques : Oui Suivi ancien pour mésusage de substance Absence de notion de cures de sevrages antérieures Antécédents Médicaux : Oui Antécédents Chirurgicaux : Oui Fractures OPN ( foot ) Antécédents Gynécologiques : Non Conduites suicidaires : Non CONTRE INDICATIONS MEDICAMENTEUSES/ALLERGIES : Absence ANTECEDENTS FAMILIAUX : Antécédents Psychiatriques : Notion de mésusage d'alcool chez son père (marin pécheur) Antécédents Médicaux : Non Conduites suicidaires : Non Patient dénutri : Non CONSOMMATION DE TOXIQUES : Toxiques : Tabac :Oui 25 ans / 15 / / Alcool : 2005 contexte d'exposition professionnelles, festive initiale affirme aimer l'ivresse Cannabis : / / / Stupéfiants autres : / / / TRAITEMENTS A L'ENTREE : Seresta /Vitamine/Selincro MODE DE VIE : Vit en couple. peu de centres d'intérêt hormis le jardin PARCOURS SCOLAIRE ET PROFESSIONNEL : Parcours scolaire : Prépa math physique puis échec pilote de chasse. Engagement à 23 ans à l'issu du service militaire avec la spécialité de détecteur. Mutliples affectations embarquées ( frégates puis Aviso). Se dit moins bien depuis l'année dernière. Parcours professionnel :
    HISTOIRE DE LA MALADIE : Patient suivi habituellement en ambulatoire 
    pour un trouble de l'usage de substance. Demande à être hospitalisé il y a un mois dans un contexte difficile à préciser qu'il met en lien avec la pression familiale. EXAMEN CLINIQUE DES 24 HEURES : Sénior : THOMAS Patient vu aux urgences : Non Plaintes fonctionnelles : Absence. Demande à être hospitalisé pour sevrage. Observation Clinique : Détachement affectif, maniérisme, tendance à la bizzarerie des association et perplexité à l'entretien. Absence de signes francs d'imprégnation sur le plan physique comme biologique. Test de personnalité : Non Evaluation du risque suicide : Absence Conclusion : Hospitalisation pour cure de sevrage et a visée diagnostic chez un patient présentant une bizarrerie du contact. Informations au patient sur la conduite du projet thérapeutique et le traitement psychotrope en cours : Délivrée EVOLUTION DANS LE SERVICE : 18/07/2024 : Bonne tolérance du cadre hospitalier et du traitement. Absence de constat de symptômes de sevrage. N'évoque pas d'envies. Revient ce jour sur ses modalités habituelles de relation. Tendance à beaucoup douter et éviter le conflit. Utilise l'alcool à visée de désinhibition. Pas de modification du cadre et du traitement pour l'instant. GTH 22/07/2024 : Garde une tendance à la maitrise des affects et des particularités du contact. Plus authentique à l'entretien. Evoque en permanence une peur de ne pas être à la hauteur dans les différents secteurs de sa vie relationnelle avec une tendance à avoir peur de l'échec. On explore alors son passé professionnel. Beaucoup d'affectation embarquée, détecteur radar, travaillait en quart. Tendance à être tout le temps volontaire. Sur le fin de carrière, la mer lui manque, voudrait quitter la marine et trouver un travail à temps partiel avec moins de pression. Impression de trop penser depuis La Réunion. Fait un constat d'échec, est rentré en vol blanc. Parle alors de son bateau précédent. Impression que quelque chose s'est cassé. Engagé depuis 26 ans, 22 ans d'embarquement. Continue à penser à l'alcool actuellement mais n'évoque pas d'envies. Parle ensuite de son père. Il était aussi réservé et introverti. Il buvait. Ca a été à l'origine de la séparation parentale. Trouve qu'il lui ressemble. 24/07/2024 : Apaisé et calme. Le contact s'améliore progressivement, avec moins de méfiance et de réticence. Reconnaît qu'il a du mal à accepter la bienveillance. Moins hermétique dans ce contexte. Revient ce jour sur la séparation de ses parents. Impression d'avoir été traumatisé par leur séparation. Décrit son père comme dépressif qui communiquait peu. Impression d'avoir été le témoin de la dégradation de l'entente familiale. : " je regardais le bateau couler". 29/07/2024 : Meilleur contact, moins réticent, plus spontané. Communique avec Mme par SMS. C'est compliqué pour lui d'en parler car il a tendance à l'idéaliser. Regrette qu'ils n'aient pas d'enfant. Pense que ça peut venir de lui. N'a jamais consulté. Affirme tenir à elle. Impression qu'il est son seul centre d'intérêt. On enchaîne sur sa crainte d'être jugé. Fait le lien avec ses parents. Impression qu'ils ont toujours été jugés. 01/08/2024 : L'humeur est stable. Se sent beaucoup plus apaisé par rapport à l'entrée. Va quitter son poste. Voudrait être affecté hors spé. Avoir un poste moins opérationnel, être moins exposé au stress. Le vit avec ambivalence. On le renforce, dans ce choix. Commence à se renseigner pour d'autres postes. Se pose aussi la question de changer de passer à autre chose. Sur le plan médicamenteux, diminution progressive Seresta avec maintien Olanzapine 1 coucher. Sur le plan du suivi, proposition participation groupe de parole une fois tous les 15 jpurs. sortie prévue le 16/08. Réhosp à 1.5 mois. 04/08/2024. Rechute hier durant la sortie. Du mal a en dire quoi que ce soit. Etait en train de vider son studio. Il restait de l'alcool dedans 3 bières à 50 cc à 7.9 %. Évoque une perte de contrôle. Pas de sortie ce jour. proposition de mise en place Selincro dans une perspective de l'aider à maîtriser en cas de rechute. 06/08/2024 : Entretien familiale ce jour. Épouse qui se dit fatiguée par l'ancieneté du mésusage et l'augmentation des consommations ces derniers mois. C'est elle qui lui aurait mis un ultimatum pour les soins. C'est l'occasion de commencer à anticiper la sortie avec la mise en place d'une participation au groupe de parole tous les 15 jours et d'un suivi en hospitalisation séquentielle. Effet d'apaisement de l'entretien. GTH 08/08/2024 : Sortie prévue ce WE. A l'examen, bon contact, plus dans l'échange et l'humour. GTH 13/08/2024 : We bien passé, affirme avoir juste consommé un verre de cidre. Est revenu rapidement le dimanche. Sortie prévu vendredi. Projet de revenir au groupe de parole tous les 15 jours. Angoisse de reprendre le travail. Ne sait pas ou il va être affecté. Sur le plan somatique : : aucune plaintes somatique. perte de 8kg constatée par MT en contexte d'alcoolotabagisme. bilan bio récent normal. - TDM TAP prescrit. - Echo hépatique prescrite - vitaminothérapie - surveillance sevrage - CS ORL - CS DIET - CS tabaco? SYNTHESE DE L'HOSPITALISATION : Donc hospitalisation programmée pour cure de sevrage. Bonne tolérance de la cure et du cadre hospitalier. Effet d'apaisement et de socialisation de l'hospitalisation. Persistance d'une tendance constitutionnelle à l'altération du contact. Poursuite d'un suivi spécialisé très étayant. TRAITEMENT DE SORTIE : OLANZAPINE 5 mg (Labo ARROW), cpr orodisp 1 comprimé, Nuit, Voie orale, pendant 2 Mois NALMEFENE (SELINCRO) 18 mg, cpr 1 comprimé, Soir, Voie orale, pendant 2 Mois ORIENTATION DU PATIENT : Prolongation arrêt de travail jusqu'au 8 septembre 2024. Prochaine Hospitalisation pour une semaine le 30/09/2024. Bien Confraternellement.
    """

    # Compiler l'expression rationnelle
    pattern = re.compile(r'HISTOIRE DE LA MALADIE(.*?)EXAMEN CLINIQUE', re.DOTALL)
    pattern2 = re.compile(r'SYNTHESE DE L\'HOSPITALISATION(.*?)TRAITEMENT DE SORTIE', re.DOTALL)
    pattern3 = re.compile(r'MOTIF D\'HOSPITALISATION(.*?)MEDECIN ADRESSEUR', re.DOTALL)

    # Utiliser search pour trouver le texte entre les deux phrases
    match = pattern.search(texte)
    match2 = pattern2.search(texte)
    match3 = pattern3.search(texte)
    if match:
        texte_interesse = match.group(1).strip()
        print(f"Texte trouvé 1 \n: {texte_interesse}")
    if match2:
        texte_interesse2 = match2.group(1).strip()
        print(f"Texte trouvé 2 \n: {texte_interesse2}")
    if match3:
        texte_interesse3 = match3.group(1).strip()
        print(f"Texte trouvé 3 \n: {texte_interesse3}")
    else:
        print("Aucun texte trouvé entre les deux phrases.")