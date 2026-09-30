# ============================================================================
# 4. Affichage des résultats
# ============================================================================


def print_report(report: dict,subsidiary:str,data_columns:list[str]) -> None:
    """_summary_.

    Args:
        report (dict): _description_
        subsidiary (str): _description_
        data_columns (list[str]): _description_
    """

    # Affichage d'en-tête
    print(f"{"="*59}")
    print(f"{subsidiary}")
    print(f"{"="*59}")

    for data in report:
        # Pour l'entreprise global, le traitement est légèrement différent
        if subsidiary == "Entreprise":
            if data != "mean income":
                print(f"{data}: {report[data]:.2f}€")
            else:
                print(f"mean income: {report[data]:.2f}€")
        else:
            # affichage des données
            if data == "datas":
                # tri des données par salaires
                for item in sorted(
                    report[data], 
                    key=lambda x: x[data_columns[2]], 
                    reverse=True
                ):
                    print(
                        f"{item[data_columns[1]]: <10} | "
                        f"{item[data_columns[0]]: <15} | "
                        f"{item[data_columns[2]]:.2f}"
                    )

            # affichage des statistiques
            if data == "stats":
                for item in report[data]:
                    print(f"{item}: {report[data][item]:.2f}€")
    print()


def afficher_rapport_salaire(rapport: dict, nom_entreprise: str) -> None:
    """Affiche le rapport salarial de l'entreprise

    Args:
        rapport (dict): rapport à afficher
        nom_entreprise (str): nom de l'entreprise cible
    """
    print(f"{"="*59}")
    print(f"{nom_entreprise} : Salaires mensuels")
    print(f"{"="*59}")

    for ligne in rapport[nom_entreprise]:

        print(
            f"{ligne["name"]: <10} | "
            f"{ligne["job"]: <15} | "
            f"salaire mensuel: {ligne["salary"]:>10.2f}€"
        )
    print(f"{"="*59}\n")


def afficher_stats(rapport: dict) -> None:
    """Affiche les statisiques à partir d'un rapport données

    Args:
        rapport (dict): rapport dont les statistiques sont tirées
    """
    for filiale in rapport:
        print(f"{"="*59}")
        print(f"{filiale.upper()} : statistiques")
        print(f"{"="*59}")

        for donnees in rapport[filiale]:
            print(
                f"{"le salaire le plus élevé est ":^40}" \
                f"{donnees["maximum"]:>15.2f}€"
            )

            print(
                f"{"le salaire le plus bas est ":^40}"\
                f"{donnees["minimum"]:>15.2f}€"
            )
            print(
                f"{"le salaire moyen est de ":^40}" \
                f"{donnees["mean"]:>15.2f}€"
            )
            print(f"{"="*59}\n")
