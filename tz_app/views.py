from django.shortcuts import render, redirect
from tz_app.models import Account
from tz_app.forms import StartForm
from Auto_browser import Auto_browser
from config import url_main

def start(request):
    """Представление стартовой страницы"""
    if request.method != 'POST':
        form = StartForm()
    else:
        form = StartForm(data=request.POST)
        try:
            if form.is_valid():
                username = form.data.get('username')
                userdata: dict = list(Account.objects.filter(username=username).values())[0]
                #Запуск функции автоматизации браузера
                Auto_browser.run_main(url=url_main, username=userdata.get('username'), password=userdata.get('password'))
                return redirect('tz_app:start')
        except:
            return redirect('tz_app:start')
            
    context = {'form': form}
    return render(request, 'tz_app/index.html', context)
