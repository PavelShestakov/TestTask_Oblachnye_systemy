# Create your views here.
from django.shortcuts import render, redirect
from tz_app.models import Account
from tz_app.forms import StartForm
from Auto_browser import Auto_browser
from config import url_main

# Create your views here.
def start(request):
    """Представление стартовой страницы"""
    if request.method != 'POST':
        #создается пустая форма, с полем для ввода и кнопкой "Начать".
        form = StartForm()
    else:
        #Отправлены данные POST; происходит получение данных из бд, открытие браузера и выполнение авторизации
        form = StartForm(data=request.POST)
        try:
            if form.is_valid():
                username = form.data.get('username')
                #получение данных username из бд
                userdata: dict = list(Account.objects.filter(username=username).values())[0] #.values_list('username', 'email','password'))
                #Запуск функции автоматизации браузера
                Auto_browser.run_main(url=url_main, username=userdata.get('username'), password=userdata.get('password'))
                #Возвращаем стартовую страницу
                return redirect('tz_app:start')
        except:
            #возвращает стартовую страницу в случае возниктновения ошибки
            return redirect('tz_app:start')

    #Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'tz_app/index.html', context)
