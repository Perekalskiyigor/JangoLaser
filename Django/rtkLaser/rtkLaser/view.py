from django.http import JsonResponse
from django.shortcuts import render

# Подключаем функцию для получения данных
from .utils import get_data_from_api  # Убедитесь, что путь правильный

def my_view(request):
    api_url = "https://api.example.com/data"  # Замените на URL вашего API
    params = {
        'param1': 'value1',
        'param2': 'value2'
    }
    
    api_url = "https://swapi.dev/api/starships/9/"
    # Получаем данные
    data = get_data_from_api(api_url, params)
    
    if data:
        # Рендерим данные в шаблон (HTML)
        return render(request, 'my_template.html', {'data': data})
    else:
        # Возвращаем ошибку в случае неудачи
        return JsonResponse({'error': 'Не удалось получить данные с API'}, status=500)