from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Student


# def hello_world(request):
    # print('hello world')
    # return HttpResponse('<h1> Главная страница приложения App <h1>')
    # return render(request, "index.html")
# Create your views here.
# def h2(request):
#     print('h2')
#     return HttpResponse('<h2> Заголовок второго уровня <h2>')

def hello_world(request):
    people = Person.objects.all() #вывод всех объектов модели (записей)
    print(people)

    # TODO: рассмотреть понятие ORM

    data = {'people' : people}

    return render(
        request, 
        'person.html',
        data # context - информация, которая передается с функции в шаблон
    )

def students(request):
    students_not_same_as_function = Student.objects.all() #вывод всех объектов модели (записей)

    return render(
        request, 'student.html', {'students' : students_not_same_as_function}
    )

