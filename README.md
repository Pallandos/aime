# AIME

*Artificial Intelligence for Medical Encoding* ou **AIME** est un projet qui vise à aider les psychiatres dans leur tâche d'encodage des actes médicaux. Notre système vise à donner une liste de codes CIM10 correspondants à un compte rendu d'hospitalisation pris en entrée.

Le projet a été réalisé en collaboration avec le service psychiatrie de l'hopital Clermont-Tonerre de Brest. 

> Aussi, il ne fonctionne que pour un type précis de comptes rendus médicaux (voir [compatibilité](#compatibilité)).

## Licence

Ce projet est sous licence MIT. 

Voir [LICENCE](./LICENSE) pour plus d'informations.

## Compatibilité

### Requis logiciels

Le projet a été codé avec `Python 3.12.3` et n'a pas été testé sur d'autres versions. 

Les bilbiothèques externes requises sont les suivantes : // SERONT INSTALLEES

- medkit-lib
- PyQt5
- transformers
- torch
- numpy
- sentence-transformers

Elles peuvent être installées rapidement avec la commande : 

    pip install -r ./py/requirements

### Comptes rendus 

Le projet a été réalisé en collaboration avec l'hopital Clermont-Tonerre à Brest. Aussi, le format des comptes rendus en entrée du programme est stricte et fixé. 

## Installation

### Ubuntu 

1. Télécharger l'archive correspondante : /////
2. Décompresser l'archive 
3. Executer le script `install.sh` avec la commande `./install.sh`
## Références

Le projet **AIME** se base sur plusieurs modèles, bibliothèques et outils développés en open source. Nous avons utilisés 2 modèles : DrBERT-CASM2 et BioLORD-2023-M.

### DrBERT-CASM2

Dans AIME, ce modèle réalise l'extraction des pathologies à partir du compte rendu d'hospitalisation.

DrBERT-CASM2 est un modèle issu de DrBERT (modèle français), de la bibliothèque *Medkit*. DrBERT-CASM2 a été fine-tuned par l'équipe *Heka* : un laboratoire de recherche sur l'IA qui regroupe des chercheurs de l'INRIA, l'INSERM, l'université de Paris-Cité et plusieurs hoitaux français comme Necker, George Pompidou...

Le modèle a été entrainé sur un corpus français de documents médicaux annotés par des étudiants en médecine de l'université Paris-Cité : *"corpusCasM2: A corpus of annotated clinical texts"*.

Le corpus contient des documents de : 

    Natalia Grabar, Vincent Claveau, and Clément Dalloux. 2018. CAS: French Corpus with Clinical Cases.
    In Proceedings of the Ninth International Workshop on Health Text Mining and Information Analysis,
    pages 122–128, Brussels, Belgium. Association for Computational Linguistics.


Liens : 
- [HuggingFace](https://huggingface.co/medkit/DrBERT-CASM2)
- [Heka team](https://team.inria.fr/heka/)  
- [Pypi de medkit](https://pypi.org/project/medkit-lib/)
- [DrBERT](https://huggingface.co/Dr-BERT/DrBERT-4GB-CP-PubMedBERT)

### BioLORD-2023-M

Dans notre projet, ce modèle match les pathologies avec la CIM-10.

BioLORD-2023-M est la version multilangue de BioLORD, un large modèle entrainé sur des données médicales. BioLORD-M a été entrainé pour comprendre les 7 langues européennes suivantes : English, Spanish, French, German, Dutch, Danish and Swedish. Les données d'entrainements sont issues de 2 datasets internationaux : *BioLORD dataset* et *Automatic Glossary of Clinical Terminology (AGCT)*. 

BioLORD a été conçu par FremyCompany, une entité qui désigne François REMY, un développeur belge.

Liens : 
- [HuggingFace BioLORD-M](https://huggingface.co/FremyCompany/BioLORD-2023-M)
- [BioLORD dataset](https://huggingface.co/datasets/FremyCompany/BioLORD-Dataset)
- [Automatic Glossary of Clinical Terminology (AGCT)](https://huggingface.co/datasets/FremyCompany/AGCT-Dataset)
- [FremyCompany](https://fremycompany.com/)

## Auteurs
