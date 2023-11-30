import mysql.connector

# Establish a connection with your MySQL database
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="alejandro_1992",
    database="mydb",
)


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


print("'''DATABASE MANAGER'''\n")
print("AVAILABLE PREDEFINED QUERIES:")
print(" ")
print("1.-Insert data into tables")
print(
    "2.-Get the subject of all metabolic pathways"
    " whose description contains the following string"
)
print(
    "3.-Get all interventions applied in a clinical study"
    " where the study result contains a given tag"
)
print(
    "4.-Get all disease labels given a subject"
    " and the description of the metabolic pathway"
)
print("5.-Exit application ")
print(" ")
print("Which query do you want to execute?")
option = int(input("Enter your choice: "))

while option != 6:
    if option == 1:
        print("Query 1")
        print("Available tables:\n 1) Clinical trials \n")
        print("In which table do you want to insert data?")
        table_option = int(input("Number: "))
        if table_option == 1:
            print("Required data:")
            data1 = input("idClinicalTrials (NCTXXXXXX) : ")
            data2 = input("Title: ")
            data3 = input("Status: ")
            data4 = input("Conditions: ")
            data5 = input("Interventions: ")
            data_string = (
                f"'{data1}', '{data2}', '{data3}', '{data4}',"
                f" '{data5}'"
            )
            insert_query_with_parameters(
                connection, table_option, data_string
            )

    if option == 2:
        print("Query 3 \n")
        str_description = input("Enter the string: ")
        query3(connection, str_description)

    if option == 3:
        print("Query 4 \n")
        tag = input("Enter the tag: ")
        query4(connection, tag)

    if option == 4:
        print("Query 5 \n")
        subject = input("Enter the subject: ")
        pathway = input("Enter the metabolic pathway: ")
        query5(connection, subject, pathway)
    print("\n AVAILABLE PREDEFINED QUERIES:")
    print(" ")
    print("1.-Insert data into tables")
    print(
        "2.-Get the subject of all metabolic pathways"
        " whose description contains the following string"
    )
    print(
        "3.-Get all interventions applied in a clinical study"
        " where the study result contains a given tag"
    )
    print(
        "4.-Get all disease labels given a subject"
        " and the description of the metabolic pathway"
    )
    print("5.-Exit application ")
    print(" ")
    print("\n Which query do you want to execute?")
    option = int(input("Enter your choice: "))


connection.close()
