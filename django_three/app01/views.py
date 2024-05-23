from django.shortcuts import HttpResponse
from app01.static import mysql

# from rest_framework.views import APIView
# from rest_framework.response import Response
# Create your views here.

# class LoginView(APIView):
#     def post(self,request,*args,**kwargs):
#         print(request.data)
#         return Response({"status":True})

def index(request):
    db = mysql.SqLite()
    sql = 'select * from user'
    list = db.get_sqlite(sql)
    print(list)
    return HttpResponse(list)