from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .ai_engine import analyze_code

def index(request):
    """
    Render the home page.
    """
    return render(request, 'review/index.html')


class CodeReviewAPIView(APIView):
    """
    API view for code review operations.
    """

    def post(self, request):
        """
        Handle POST requests for code review.
        """
        code = request.data.get('code')
        language = request.data.get('language', 'python')

        if not code:
            return Response({"error": "Code is required."},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            analysis =  analyze_code(code, language)
            return  Response({"analysis": analysis}, status= status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

       