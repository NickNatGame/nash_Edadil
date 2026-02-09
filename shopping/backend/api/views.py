from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .analyze import analyze
from .sample_data import load_sample_data
from .main import parsing
from .json_utils import save_file, clear_file

# Загрузите данные из JSON файла
def get_products(request):
    #parsing()
    data = load_sample_data()
    return JsonResponse(data, safe=False)
   

# Анализ корзины
@csrf_exempt
def analyze_cart(request):
    if request.method == 'POST':
        cart_data = request.body
        '''with open('cart_data.json', 'w', encoding='utf-8') as file:
            json.dump(cart_data, file)'''

        result = str(analyze(cart_data))

        return JsonResponse(result, safe=False)
