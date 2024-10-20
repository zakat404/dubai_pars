import requests
import json

# URL для запроса данных с сервиса. Используйте URL слоя, в котором находятся полигоны участков.
url = "https://gis.dda.gov.ae/server/rest/services/DIS/MAIN_MAP/MapServer/13/query"

# Параметры для запроса всех объектов
params = {
    "f": "json",  # Формат ответа
    "where": "1=1",  # Условие для выборки всех объектов
    "outFields": "*",  # Получаем все поля для каждого объекта
    "returnGeometry": "true",  # Возвращаем геометрию (например, чтобы получить границы участков)
    "geometryType": "esriGeometryEnvelope",  # Тип геометрии
    "inSR": "102100",  # Система координат
    "token": "CzxDZ8zpPAOlc6u0fo9Rpphw_N5Elhvlyx1NxMH11TEIh1bSMljbmVgZt6L9XzddcqtQZI5QZd3OigAB8oVQmdE6XCD30juCI3yukTmfzRRfP7PbCH5iBUF8LxiSU0SpyKBkAWp1YoN-EZnRQtVBB64bTyUDOnYjPuRNLJA3Hrusz49b7vR5Fg-XuXfBrJZm"
    # Токен для доступа
}

# Отправляем запрос
response = requests.get(url, params=params)

# Проверяем, успешен ли запрос
if response.status_code == 200:
    # Получаем ответ в формате JSON
    data = response.json()

    # Сохраняем данные в JSON-файл
    with open('all_plot_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
        print("Данные успешно сохранены в файл all_plot_data.json")
else:
    print("Ошибка при запросе данных: ", response.status_code)
