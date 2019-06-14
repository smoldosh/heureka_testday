from django.shortcuts import render, render_to_response
from django.http import HttpRequest
import requests
import json


# Vrátí json strukturu na základě zadaného url
def getrequest(url):
    r = requests.get(url)
    return r.json()


def getimg(offerlist, product):
    for offer in offers:
        if offer['img_url'] != None:
            product['img_url'] = offer['img_url']
            continue
    
        product['img_url'] = None


# JSON pro výpis kategorií
categories = getrequest("http://python-servers-vtnovk529892.codeanyapp.com:5000/categories/")


def homepage(request):
    return render(request, "index.html", dict(jsondict=categories))


def productlist(request, id):
    #categoryid = 3
    
    # JSON se seznamem produktů na zákadě URL a id kategorie
    prodlist = getrequest("http://private-anon-ef66a8d825-catalogue9.apiary-proxy.com/products/"+str(id)+"///")

    for product in prodlist:
        offers = getrequest("http://private-anon-ef66a8d825-catalogue9.apiary-proxy.com/offers/"+str(product['productId'])+"///")

    # Zjištění zda-li se v nabídkách vyskytuje obrázek k produktu
        for offer in offers:
            if offer['img_url'] != None:
                product['img_url'] = offer['img_url']
                continue
        
            product['img_url'] = None

        prices = []
        for offer in offers:
            prices.append(offer['price'])

        prices.sort()

        product['min_price'] = prices[0]
        product['max_price'] = prices[len(prices)-1]
            

    return render(request, "section.html", dict(jsondict=categories, jsondictp=prodlist))
