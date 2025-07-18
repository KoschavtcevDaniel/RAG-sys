import psycopg2
from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer('paraphrase-MiniLM-L3-v2')

conn = psycopg2.connect(host='localhost', user='postgres', password='password', dbname='postgres')
cursor = conn.cursor()


def vectorize_bd():
    cursor.execute("Select * from information")
    result = cursor.fetchall()
    for numb, txt in result:
        vec = embedding_model.encode(txt).tolist()
        cursor.execute(
            "INSERT INTO vectors (id_doc, embedding) VALUES (%s, %s)",
            (numb, vec)
        )
        conn.commit()


vectorize_bd()
