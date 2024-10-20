from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def hello_world(request):
    people = Person.objects.all() # вывод всех объектов (записей) модели Person
    #print(people)
    # TODO: рассмотреть понятие ORM

    data = {'marks': [4, 5, 5, 4, 3], 'people': people}

    return render(
        request,
        'index.html',
        data  # context - информация которая передается с функции
        # в шаблон
    )
