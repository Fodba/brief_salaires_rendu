import statistics

# ============================================================================
# 2. Calcul des salaires mensuels
# ============================================================================


def get_salary(
        employe:dict, 
        contract_hours: float, 
        hourly_rate: float, 
        weekly_hours: float
    ) -> float:
    """Calcule le salaire mensuel d'un employé à partir des données fournies

    Args:
        hourly_rate (float): taux horaire de l'employé
        weekly_hours (float): nombre d'heures effectivement travaillées
        contract_hours (float): nombre d'heures prévues au contrat

    Returns:
        float: salaire mensuel calculé sur le taux horaire et les heures
        travaillées
    """
    salaire_hebdo: float = 0

    # Calcul du salaire hebdomadaire sur la base horaire du contrat ou sur les
    # heures vraiment travaillées
    if employe[weekly_hours] <= employe[contract_hours]:
        salaire_hebdo = employe[hourly_rate] * employe[weekly_hours]
    else:
        salaire_hebdo = employe[hourly_rate] * employe[contract_hours]

    # Mise à jour avec les heures supplémentaires
    if employe[weekly_hours] > employe[contract_hours]:
        ecart = employe[weekly_hours] - employe[contract_hours]
        salaire_hebdo += employe[hourly_rate] * (ecart * 1.5)

    # Calcul du salaire mensuel
    salaire_mensuel: float = salaire_hebdo * 4
    return salaire_mensuel


def get_subsidiary_salaries(
        subsidiary:str,
        subsidiary_datas: dict,
        columns :list[str]
    )->tuple(list[dict],list[float]):
    """Calcule le salaire mensuel des employés d'une filiale.

    Args:
        subsidiary (str): nom de la filiale
        subsidiary_datas (dict): données de la filiale
        columns (list[str]): colonnes de données à utiliser

    Returns:
        tuple(list[dict],list[float]): un tuple conenant le 
        rapport salarial ainsi que les statistiques de la filiale
    """

    # colonnes lié au salaire
    salary_columns: list[str] = sorted(
        [key for key in set(columns) if "hour" in key]
    )
    # colonnes d'information
    data_columns: list[str] = sorted(
        [key for key in set(columns) if "hour" not in key]
    )

    salaries_report: list[dict] = []
    salaries_list: list[float] = []

    for employe in subsidiary_datas:
        # calcul des salaires pour chaque employé
        salaire = get_salary(employe, *salary_columns)
        # sauvegarde du salaire pour faire la moyenne par la suite
        salaries_list.append(salaire)
        # élaboration du rapport salarial
        salaries_report.append(
            {
                "subsidiary": subsidiary,
                data_columns[1]: employe[data_columns[1]],
                data_columns[0]: employe[data_columns[0]],
                "incomes": salaire,
            }
        )
    return salaries_report, salaries_list


def get_stats(
        salaries_list: list,
        stat_columns:list[str]
    ) -> dict:
    """retourne le salaire le plus élevé, le plus bas ainsi que 
    la moyenne.

    Args:
        salaries_list (list): liste des salaires
        stat_columns (list[str]): nom des colonnes à utiliser

    Returns:
        dict: un dictionnaire contenant le salaire le plus élevé, 
        le plus bas et le salaire moyen
    """
    max_salary: float = 0
    min_salary: float = float("inf")

    for salaire in salaries_list:
        if salaire > max_salary:
            max_salary =  salaire
        if salaire < min_salary:
            min_salary = salaire

    mean_salary = statistics.mean(salaries_list)
    
    return {
        stat_columns[0]: max_salary,
        stat_columns[1]: min_salary,
        stat_columns[2]: mean_salary,
    }

