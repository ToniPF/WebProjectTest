#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8:

from urllib.request import urlopen
import bs4

#https://openweathermap.org/

class Client(object):

    def __init__(self, url):
        self.url = url

    def download_html(self):
        url = 'http://api.openweathermap.org/data/2.5/find?q=Lleida&units=metric&appid=870d7d010af43e7ca5ba6bb77f1328a4'
        file_source = urlopen(url)
        html = file_source.read()
        file_source.close()
        return html

    def proces_weather(self, html):
        arbre = bs4.BeautifulSoup(html, features="lxml")
        temperature = arbre.find("temperature")
        print(temperature)


    def run(self, url):
        html = self.download_html()
        print(html)
        self.proces_weather(html)
        print('I am running')


if __name__ == '__main__':
    url = 'https://www.packtpub.com/packt/offers/free-learning'
    client = Client(url)
    client.run(url)
