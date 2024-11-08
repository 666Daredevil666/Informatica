def parse_json_to_xml(json_data):
    xml_content = "<schedule>\n"

    for lesson in json_data["schedule"]:
        xml_content += "    <lesson>\n"
        xml_content += f"        <time>{lesson['time']}</time>\n"
        xml_content += f"        <subject>{lesson['subject']}</subject>\n"
        xml_content += f"        <lecturer>{lesson['lecturer']}</lecturer>\n"
        xml_content += f"        <audience>{lesson['audience']}</audience>\n"
        xml_content += f"        <address>{lesson['address']}</address>\n"
        xml_content += "    </lesson>\n"

    xml_content += "</schedule>"

    return xml_content


# Пример использования
import json

# Исходный JSON с расписанием
schedule_json = {
    "schedule": [
        {
            "time": "17:00",
            "subject": "Теория функций комплексного переменного",
            "lecturer": "Бойцев Антон Александрович",
            "audience": "1405",
            "address": "Кронверкский пр., д.49, лит.А"
        },
        {
            "time": "18:40",
            "subject": "Теория функций комплексного переменного",
            "lecturer": "Бойцев Антон Александрович",
            "audience": "1405",
            "address": "Кронверкский пр., д.49, лит.А"
        }
    ]
}

# Преобразование JSON в XML
xml_output = parse_json_to_xml(schedule_json)

# Сохранение XML в файл
with open("schedule.xml", "w", encoding="utf-8") as file:
    file.write(xml_output)
