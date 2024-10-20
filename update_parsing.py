import requests
import json

BASE_URL = "https://gis.dda.gov.ae/server/rest/services/DIS/MAIN_MAP/MapServer/13/query"
PARAMS = {
    "where": "1=1",
    "outFields": "*",
    "f": "json",
    "resultOffset": 0,
    "resultRecordCount": 2000,
    "token": "en6hvabyQHStj-y3rgnvQBLfoHxwkYp0qagJR0T2m8RWAIOfAGk9DISQc6dSX-gwk9CHqK9a2TULF5Bg_4rG76CSSWmdmJHAgWl-sK7qqGInFQ_XiS3VPDdDooovKdPCNtfEGXVGZ0CEHzQzn64CYynN79jJCskBN7i5YUsbIdT7lL1W8LUT2ft0vUC0LDb5"
}

all_features = []

while True:
    response = requests.get(BASE_URL, params=PARAMS)
    data = response.json()

    if 'features' in data:
        all_features.extend(data['features'])

        # Если количество возвращенных объектов меньше, чем `resultRecordCount`, значит мы дошли до конца
        if len(data['features']) < PARAMS["resultRecordCount"]:
            break

        # Увеличиваем смещение для следующей выборки
        PARAMS["resultOffset"] += PARAMS["resultRecordCount"]
    else:
        # Обработка ошибки, если что-то пошло не так
        print("Ошибка при запросе данных:", data)
        break

# Сохранение всех объектов в файл
with open('all_plot_data.json', 'w') as f:
    json.dump(all_features, f, indent=4)

print(f"Общее количество участков: {len(all_features)}")
