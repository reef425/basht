from django.shortcuts import render, get_object_or_404
from . models import weather,Places,Hours
import logging
from django.utils import timezone
import threading
# Create your views here.

def initlog():
    """init() - setup config for logging"""
    logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s %(filename)s %(message)s",
                        filename="/home/reef/app.log",
                        level=logging.INFO,
                        )

def tempfunc():
    pass

def sort_key_weather(weather):
    return weather.shortname

def about(request):
    return render(request, "about.html")

def curent_hour():
    hour = timezone.now().hour
    if hour<=18:
        return hour+5
    else:
        return (hour+5)-24

def myruner():
    cdt = timezone.now()
    db_dt = timezone.datetime.fromtimestamp(Hours.objects.filter(id=1)[0].hour)
    if cdt.year!=db_dt.year or cdt.month!=db_dt.month or cdt.hour!=db_dt.hour:
        cdt=cdt-timezone.timedelta(minutes=cdt.minute,seconds=cdt.second)
        Hours.objects.filter(id=1).update(hour=int(cdt.timestamp()))
        from . import openweathermap
        th = threading.Thread(target = openweathermap.run())
        th.start()

def basht_list(request):
    myruner()
    last_item = weather.objects.last()
    weathers = weather.objects.filter(date=last_item.date)
    dt = timezone.datetime.fromtimestamp(last_item.date)
    dt = dt+timezone.timedelta(hours=5)
    update_date = str(dt)
    for wth in weathers:
        wth.shortname=Places.data.setdefault(wth.pid,{"name":"None city"}).get("name")
    weathers=list(weathers)
    weathers.sort(key=sort_key_weather)
    return  render(request, 'basht_list.html',{"weathers":weathers,"whr":weathers,"update_date":update_date})

def get404(request):
    return render(request, '404.html')
