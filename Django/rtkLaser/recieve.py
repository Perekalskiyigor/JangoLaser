import requests

import requests

def get_data_from_api(url, params=None):
    try:
        # Отправляем GET-запрос
        response = requests.get(url, params=params)
        
        # Проверяем статус ответа
        response.raise_for_status()
        
        # Возвращаем JSON-данные
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе данных: {e}")
        return None
    


'''
# Вызов функции и вывод результата в консоль
if __name__ == "__main__":
    api_url = "https://swapi.dev/api/starships/9/"  # Пример API (замените на ваше)
    params = {"userId": 1}  # Пример параметров (если они есть)

    data = get_data_from_api(api_url, params)
    
    # Печать результата
    if data:
        print("Полученные данные:")
        for item in data:
            print(item)  # Печать каждого элемента (например, словаря)
    else:
        print("Не удалось получить данные.")
'''
