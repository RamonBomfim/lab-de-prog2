# selecionando todos os registros
import psycopg2
connection = ""
try:
    conn = psycopg2.connect(database='empresa',
                            user='postgres',
                            password='941215',
                            host='localhost',
                            port='5433')

    cursor = conn.cursor()
    postgreSQL_select_Query = "select nome, sexo, municipio from empregado"
    cursor.execute(postgreSQL_select_Query)
    print("Selecionando os registros")
    empregado_records = cursor.fetchall()

    print("Imprimindo cada linha e coluna")
    for row in empregado_records:
        print("Nome = ", row[0])
        print("Sexo  = ", row[1])
        print("Município  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error:
    print(f"Ocorreu uma falha, informe o erro {error}​​​​ ao suporte")

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        conn.close()
        print("PostgreSQL conexão encerrada")
