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
        file_source = urlopen(self.url)
        html = file_source.read()
        file_source.close()
        return html

    def find_information(self, html):
        arbre = bs4.BeautifulSoup(html, features="lxml")
        print(arbre)
        info = arbre.find_all("div", "free-learning-dropin")
        print(info)
        pass

    def run(self, url):
        html = self.download_html()
        #print(html)
        self.find_information(html)
        print('I am running')


if __name__ == '__main__':
    url = 'https://www.packtpub.com/packt/offers/free-learning'
    client = Client(url)
    client.run(url)
