from .views import *
from django.urls import path
# список доступных страниц для чтения 
# После запроса пользователя
# браузер будет искать
# соответсвующий путь в этом массиве

urlpatterns = [
    # path(route, view_func, name="")
    path('hello_world/', hello_world),
    path('students/', students)
]