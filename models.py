from django.db import models
from django.utils import timezone



class names(models.Model):
    """docstring for BashT."""


    id = models.AutoField(primary_key=True)
    name = models.TextField()
    altname = models.TextField()

    def publish(self):
        pass

    def __str__(self):
        return self.name

vectors= {1:"Сверный",
2:"Южный",3:"Западный",4:"Восточный",5:"Юго-Западный",
6:"Юго-Восточный",7:"Северо-Западный",8:"Северо-Восточный",9:"Штиль"
}

class weather(models.Model):
    """docstring for BashT."""

    id=models.IntegerField(primary_key=True)
    pid = models.IntegerField(null=True)
    temperature = models.IntegerField(null=True)
    wind_deg = models.IntegerField(null=True)
    wind_name = models.TextField(null=True)
    wind_speed = models.IntegerField(null=True)
    pressure = models.IntegerField(null=True)
    humidity = models.IntegerField(null=True)
    cloud_icon = models.TextField(null=True)
    cloud_description = models.TextField(null=True)
    date = models.IntegerField(null=True)


    def publish(self):
        pass

class Hours(models.Model):
    id=models.IntegerField(primary_key=True)
    hour=models.IntegerField()

class Places():
    @staticmethod
    def shortnames():
        names =[]
        ids = []
        p=Places()
        for item in p.data.values():
            names.append(item.get("shortname"))
        names.sort()
        return names

    @staticmethod
    def sortdata():
        data = dict.fromkeys(Places.shortnames())
        for k,v in Places.data.items():
            for kk in data.keys():
                if kk==v.get("shortname"):
                    data.update([(kk,k)])
        return data

    data={
    484856:{"latin":"Agidel","name":"Агидель"},
    578120:{"latin":"Belebey","name":"Белебей"},
    577881:{"latin":"Beloretsk","name":"Белорецк"},
    576317:{"latin":"Birsk","name":"Бирск"},
    576116:{"latin":"Blagoveshchensk","name":"Благовещенск"},
    567006:{"latin":"Davlekanovo","name":"Давлеканово"},
    563719:{"latin":"Dyurtyuli","name":"Дюртюли"},
    555980:{"latin":"Ishimbay","name":"Ишимбай"},
    539283:{"latin":"Kumertau","name":"Кумертау"},
    527717:{"latin":"Meleuz","name":"Мелеуз"},
    522942:{"latin":"Neftekamsk","name":"Нефтекамск"},
    515879:{"latin":"Oktyabrskiy","name":"Октябрьский"},
    499292:{"latin":"Salavat","name":"Салават"},
    493160:{"latin":"Sibay","name":"Сибай"},
    487495:{"latin":"Sterlitamak","name":"Стерлитамак"},
    480089:{"latin":"Tuymazy","name":"Туймазы"},
    479561:{"latin":"Ufa","name":"Уфа"},
    479704:{"latin":"Uchaly","name":"Учалы"},
    569579:{"latin":"Chekmagush","name":"Чекмагуш"},
    469178:{"latin":"Yanaul","name":"Янаул"}
    }
