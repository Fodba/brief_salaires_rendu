# 1. Importation et préparation des données
# 2. Calcul des salaires mensuels
# 3. Calcul des statistiques salariales
# 4. Affichage des résultats
# 5. Qualité du code, optimisation


# =============================================================================
# 1. Importation et préparation des données
# =============================================================================

# Import des modules python nécessaires
import json
from affichage import print_report
from functions import (
    get_stats,
    get_subsidiary_salaries,
)

file: str = "datas/employes-data.json"
# file: str = "datas/employes_data_test.json"

# Ouverture du fichier de données et enregistrement dans la variable "datas"
with open(file, "r", encoding="utf-8") as f:
    datas: dict = json.load(f)

# préparation des variables du programme
# liste des filiales
subsidiaries: list = list(datas)
# liste des noms de colonnes du jeu de données
columns: list = datas[list(datas)[0]][0].keys()
# colonnes lié au salaire
salary_columns: list = sorted([key for key in set(columns) if "hour" in key])
# colonnes d'information
data_columns: list = sorted([key for key in set(columns) if "hour" not in key])

stat_columns: list[str] = ["maximum income", "minimum income", "mean income"]

salaries_report: dict = {}
salaries_list: list = []



# boucle de préparation et de récupération des champs principaux
for filiale in datas:
    
    salaries_report[filiale] = {
        "datas": [],
        "stats": {}
    }
    # Calcul des salaires pour chaque filiale
    salaries_report[filiale]["datas"],salaries = get_subsidiary_salaries(
        filiale,datas[filiale],
        columns
    )

    # Calcul des stats de filiale et préparation du calcul des stats global
    salaries_list.extend(salaries)
    stats = get_stats(salaries,stat_columns)
    salaries_report[filiale]["stats"] = stats

    # Affichage des salaires et stats par filiale
    report_columns = data_columns.copy() + ["incomes"]
    print_report(salaries_report[filiale],filiale, report_columns)

# Calcul et affichage des stats global
global_stats = get_stats(salaries_list,stat_columns)
print_report(global_stats, "Entreprise", stat_columns)

