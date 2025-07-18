import model_init
from sentence_transformers import SentenceTransformer
import psycopg2
import torch


device = "cuda" if torch.cuda.is_available() else "cpu"

embedding_model = SentenceTransformer('paraphrase-MiniLM-L3-v2')

model = model_init.get_model()
tokenizer = model_init.get_tokenizer()

conn = psycopg2.connect(host='localhost', user='postgres', password='29062003', dbname='postgres')
cursor = conn.cursor()


def answer_question(text):
    context = search_in_bd(text)

    prompt = f"""
    На основе следующего контекста ответь на вопрос. 
    Если во всём контексте нет информации для ответа — скажи: Извините, я не знаю ответа на этот вопрос.
    Используй только информацию из контекста. 
    Не добавляй знания, полученные из других источников.  
    
    Контекст:
    {context}
    
    Вопрос:
    {text}
    
    Ответ должен быть без спец слов и похожим на человеческий. Ответы должны быть достаточно информативными.
    
    Ответ:
    """

    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=200, do_sample=True, temperature=0.5)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    answer = response[len(prompt):].strip()

    return answer



def search_in_bd(txt):
    query_vec = embedding_model.encode(txt).tolist()

    try:
        cursor.execute("""
                SELECT information.doc 
                FROM vectors
                JOIN information ON vectors.id_doc = information.id_doc
                ORDER BY vectors.embedding <-> %s::vector
                LIMIT 3
            """, (query_vec,))

        # 3. Извлекаем результаты
        results = cursor.fetchall()

        # 4. Объединяем найденные документы в один контекст
        context = " ".join([row[0] for row in results if row[0]])

        return context

    except Exception as e:
        print("Ошибка при поиске в БД:", e)
        return ""


def take_sum():
    pass




