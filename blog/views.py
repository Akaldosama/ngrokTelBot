# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from num2words import num2words
#
# @api_view(['POST'])
# def num_to_words(request):
#     try:
#         num = request.data.get('number', None)
#
#         if num is None:
#             return Response({'error': 'son kiritilmagan'}, status=400)
#         if not isinstance(num, int):
#             return Response({'error': 'Butun son kiritilmagan.'}, status=400)
#
#         txt = num2words(num, lang='en')
#         return Response({'number_in_words': txt}, status=200)
#     except Exception as e:
#         return Response({'error': str(e)}, status=400)

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from num2words import num2words

@api_view(['POST'])
def num_to_words(request):
    try:
        num = request.data.get('number', None)

        if num is None:
            return Response({'error': 'son kiritilmagan'}, status=400)
        if not isinstance(num, int):
            return Response({'error': 'Butun son kiritilmagan.'}, status=400)

        txt = num2words(num, lang='en')
        return Response({'number_in_words': txt}, status=200)
    except Exception as e:
        print(f"An error occurred: {e}")  # Log the error for debugging
        return Response({'error': str(e)}, status=400)
