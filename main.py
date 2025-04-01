from Bloc_1 import bloc_1
from Bloc_2 import bloc_2
from Bloc_3 import bloc_3


def main():
    with open("ENSTAP1.txt", "r", encoding="utf-8") as file:
        texte = file.read()

    resultats = bloc_1(texte)

    print("Partie 1:", resultats[0] if len(resultats) > 0 else "Aucune donnée")
    print("Partie 2:", resultats[1] if len(resultats) > 1 else "Aucune donnée")
    print("Partie 3:", resultats[2] if len(resultats) > 2 else "Aucune donnée")

    for i, partie in enumerate(resultats):
        print(f"Résultats Bloc_2 pour Partie {i + 1}:")
        bloc2_results = bloc_2(partie)

        print("Bloc_2 Results:", bloc2_results)

        print(f"Résultats Bloc_3 pour Partie {i + 1}:")
        bloc3_results = bloc_3(bloc2_results)
        for result in bloc3_results:
            print(f"Entity: {result['entity']}")
            print(f"Best Match: {result['best_match_code']} - {result['best_match_description']}")
            print(f"Second Best: {result['second_best_match_code']} - {result['second_best_match_description']}")
            print(f"Third Best: {result['third_best_match_code']} - {result['third_best_match_description']}")
            print()


if __name__ == "__main__":
    main()
