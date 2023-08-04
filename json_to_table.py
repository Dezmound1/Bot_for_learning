import json
import psycopg2

json_file_path = 'C:\\code\\Bot\\data.json'

def insert_subjects_from_json(json_file_path):
    with open(json_file_path, "r", encoding='utf-8') as file:
        data = json.load(file)

    connection = psycopg2.connect(database="Dolg_bot_bd", user="postgres", password="denchik2557204", host="localhost")
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO subject (title, status, cost, schedule, room, teacher, comment)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    default_cost = 0.0
    for key, subject_data in data.items():
        title = subject_data["title"]
        status = subject_data.get("status", False)
        cost = subject_data.get("cost", default_cost)
        schedule = subject_data.get("schedule", None)
        room = subject_data.get("room", None)
        teacher = subject_data.get("teacher", None)
        comment = subject_data.get("comment", None)
        values = (title, status, cost, schedule, room, teacher, comment)

        try:
            cursor.execute(insert_query, values)
        except Exception as e:
            print(f"Error occurred for values: {values}")
            raise e

    connection.commit()
    cursor.close()
    connection.close()

insert_subjects_from_json(json_file_path)
