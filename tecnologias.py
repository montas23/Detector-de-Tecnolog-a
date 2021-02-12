#!/usr/bin/env python
#_*_coding: utf8_*_


from Wappalyzer import WebPage, Wappalyzer
import argparse

parser = argparse.ArgumentParser(description='Obtener Tecnologia')
parser.add_argument('-p','--page',help='Ingrese Página WEB')
parser = parser.parse_args()


URL = parser.page
def main():
    if parser.page:
        wap = Wappalyzer.latest()
        try:
            web = WebPage.new_from_url(URL)
            tecnologias = wap.analyze(web)
            for t in tecnologias:
                print('Tecnologia detectada: {}'.format(t))

        except:
            print('Ha ocurrido un error')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
            