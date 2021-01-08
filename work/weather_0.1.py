# -*- coding: utf-8 -*-
import sys, os, ftplib, socket, json, urllib.request, xml.etree.ElementTree as ET, time

log = open("log.txt", "w+")
fo = open("temp", "w+")
citypy = ["heilongjiang", "jilin", "liaoning", "neimenggu", "hebei"]

for py in citypy:
    with urllib.request.urlopen("http://flash.weather.com.cn/wmaps/xml/" + py + ".xml") as response:
        html = response.read()
        # print(html.decode("utf-8"))
        tree = ET.fromstring(html.decode("utf-8"))
        xianpy = []
        for c in tree.iter("city"):
            data = {};
            data["city"] = c.get('cityname')
            data["type"] = c.get('stateDetailed')
            data["low"] = c.get('tem2')
            data["high"] = c.get('tem1')
            data["wind_dir"] = c.get('windState')
            data["wind_power"] = ""
            fo.write(json.dumps(data) + "\n")
            xianpy.append(c.get('pyName'))
            print(data)
        for xpy in xianpy:
            with urllib.request.urlopen("http://flash.weather.com.cn/wmaps/xml/" + xpy + ".xml") as response:
                html = response.read()
                # print(html.decode("utf-8"))
                xtree = ET.fromstring(html.decode("utf-8"))
                for c in xtree.iter("city"):
                    xdata = {};
                    xdata["city"] = c.get('cityname')
                    xdata["type"] = c.get('stateDetailed')
                    xdata["low"] = c.get('tem2')
                    xdata["high"] = c.get('tem1')
                    xdata["wind_dir"] = c.get('windState')
                    xdata["wind_power"] = ""
                    print(xdata)
                    fo.write(json.dumps(xdata) + "\n")

fo.close();
log.write(str(time.asctime(time.localtime(time.time()))) + "天气数据获取成功\n");
log.close();
fo = open("temp", "rb")
ftp = ftplib.FTP("223.100.28.117")
ftp.login("fzweatherftp", "fz_weather_ftp")
ftp.storbinary("STOR weather.txt", fo, 1024)
ftp.quit()
fo.close()
os.remove("temp")
