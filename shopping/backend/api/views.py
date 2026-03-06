from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .analyze import analyze
from .test import test_json

# Загрузите данные из JSON файла
def get_products(request):
    data = test_json()
    return JsonResponse(data, safe=False)
   

# Анализ корзины
@csrf_exempt
def analyze_cart(request):
    if request.method != 'POST':
        return JsonResponse({'detail': 'Method not allowed'}, status=405)

    try:
        result = analize(request.body)
    except Exception as exc:
        return JsonResponse({'detail': f'Invalid cart payload: {exc}'}, status=400)

    return JsonResponse(result)
