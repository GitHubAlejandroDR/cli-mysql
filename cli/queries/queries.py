# QUERIES


def insert_query_with_parameters(connection, table_number, values):
    if table_number == 1:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO clinicaltrials (idClinicalTrials, Title,"
            " Status, Conditions, Interventions) VALUES ("
            + values
            + ")"
        )
        cursor.execute("commit")
        cursor.close()


def insert_relation_query(connection, table_number, values):
    if table_number == 1:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO atiende (paciente_nss, consulta_nconsulta)"
            " VALUES ("
            + values
            + ")"
        )
        cursor.execute("commit")
        cursor.close()


def query3(connection, str_description):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT Subject FROM pathways WHERE Description LIKE"
        f" '%{str_description}%'"
    )
    results = cursor.fetchall()

    max_length = max(len(str(row[0])) for row in results)

    table = f" {'-' * (max_length + 2)} \n"

    for row in results:
        table += f"| {row[0]}{' ' * (max_length - len(row[0]))} |\n"

    table += f" {'-' * (max_length + 2)} "

    cursor.close()

    print(table)


def query4(connection, str_tag):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT Interventions FROM clinicaltrials WHERE EXISTS"
        " (SELECT Study FROM resultsclinicaltrials WHERE"
        " resultsclinicaltrials.clinicaltrials_idClinicalTrials ="
        " clinicaltrials.idClinicalTrials AND Study LIKE"
        f" '%{str_tag}%')"
    )
    results = cursor.fetchall()

    table = " "

    for row in results:
        table += f"{row[0]}\n"
        table += f"{'-' *len(row[0])}\n"

    cursor.close()

    print(table)


def query5(connection, str_subject, str_pathway):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT DiseaseLabel FROM clingene WHERE"
        " Pathways_idPathways1 IN (   SELECT idPathways FROM"
        f" pathways  WHERE Subject = '{str_subject}' AND Description"
        f" LIKE '%{str_pathway}%')"
    )
    results = cursor.fetchall()

    table = " "

    for row in results:
        table += f"{row[0]}\n"
        table += f"{'-' *len(row[0])}\n"

    print(table)
