from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .analize import analize
from .test import test_json
from .main import parsing
from .work_with_json import save_file,clear_file

# Загрузите данные из JSON файла
def get_products(request):
    #parsing()
    data = test_json()
    return JsonResponse(data, safe=False)
   

# Анализ корзины
@csrf_exempt
def analyze_cart(request):
    if request.method == 'POST':
        cart_data = request.body
        '''with open('cart_data.json', 'w', encoding='utf-8') as file:
            json.dump(cart_data, file)'''

        result = str(analize(cart_data))

        return JsonResponse(result, safe=False)