import logging
import time
import http.client
import json
import sqlite3
from datetime import datetime

def init():
    """init() - setup config for logging"""
    logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s %(filename)s %(message)s",
                        filename="~/app.log",
                        level=logging.INFO,
                        )


def connect():
    cities = {
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
    ids = ",".join(str(i) for i in cities.keys())
    print(ids)
    key = "xxx"
    domain = "api.openweathermap.org"
    url = "/data/2.5/group?id=%s&lang=ru&units=metric&appid=%s"%(ids,key)
    conn = None
    while True:
        try:
            conn = http.client.HTTPConnection(domain)
            conn.request("GET",url=url)
        except Exception as e:
            logging.error(e)
        else:
            break
        time.sleep(10)
    result = conn.getresponse()
    logging.info("get site status:%d"%result.status)
    data = result.read().decode()
    conn.close()
    return data

def get_last_item(cur):
    """[item, ...] get_last_item(sqlite3.connect.cursor) - Retrieve from a table the last written value
    func:get_last_item(sqlite3.connect.cursor)
    return:[item, ...]
    """
    sql = "SELECT get_date FROM basht_weather ORDER BY id DESC LIMIT 1"
    ex= cur.execute(sql)
    res = cur.fetchone()
    if res:
        return res
    else:
        return None

def setWeather(data):
    """The entry in the database of the obtained values
    func:setWeather(return buildData)
    """
    db = "~/mysite/db.sqlite3"
    columns = ["pid",
      "temperature",
      "wind_deg" ,
      "wind_name" ,
      "wind_speed" ,
      "pressure" ,
      "humidity" ,
      "cloud_icon" ,
      "cloud_description" ,
      "date"]
    con =sqlite3.connect(db)
    cur =con.cursor()
    sql = "INSERT INTO basht_weather(%s) VALUES (%s?)"%(",".join(columns),"?,"*(len(columns)-1))
    for row in data:
        values = []
        values.append(row["id"])
        values.append(int(row["main"]["temp"]))
        values.append(int(row["wind"]["deg"]))
        values.append(setWind(row["wind"]["deg"]))
        values.append(int(row["wind"]["speed"]))
        values.append(int(row["main"]["pressure"]/1.333))
        values.append(int(row["main"]["humidity"]))
        values.append(row["weather"][0]["icon"])
        values.append(row["weather"][0]["description"])
        values.append(row["dt"])
        try:
            cur.execute(sql,tuple(values))
        except sqlite3.DatabaseError as er:
            logging.error(er)
        else:
            con.commit()
    logging.info("add to db!")
    data.clear()
    cur.close()
    con.close()

def readJsonFile():
    path = "data/weather.json"
    result = []
    with  open(path,"r") as f:
        return f.read()


def setWind(deg=0.0):
    if deg>337.5 or deg<=22.5:
        return "N"
    elif deg>22.5 and deg<=67.5:
        return "NE"
    elif deg>67.5 and deg<=112.5:
        return "E"
    elif deg>112.5 and deg<=157.5:
        return "SE"
    elif deg>157.5 and deg<=202.5:
        return "S"
    elif deg>202.5 and deg<=247.5:
        return "SW"
    elif deg>247.5 and deg<=292.5:
        return "W"
    elif deg>292.5 and deg<=337.5:
        return "NW"

def run():
    init()
    rawobj = connect()
    try:
        obj = json.loads(rawobj)
    except Exception as err:
        logging.error(err)
    else:
        setWeather(obj["list"])

if __name__ == '__main__':
    run()
