import psycopg2

conn = psycopg2.connect(database='empresa',
                        user='postgres',
                        password='941215',
                        host='localhost',
                        port='5433')

print("Sucesso na conexão ao Banco")

cursor = conn.cursor()
cursor.execute("SELECT * FROM empregado")
conn.commit()

rows = cursor.fetchall()

for row in rows:
    print(row[1])

cursor.close()
conn.close()
