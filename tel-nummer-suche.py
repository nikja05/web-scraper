"""
Dieses Programm nimmt user input und sucht auf
search.ch nach den entsprechenden Telefonnummern
"""
from urllib import request, parse
from re import findall

print("Bitte verwende keine umlaute, sondern schreibe sie als (ü -> ue)")
user_was = input("Was suchst du? ")
user_wo = input("Wo suchst du es? ")

url = "https://search.ch/tel/?was=" + user_was + "&wo=" + user_wo

uf = request.urlopen(url)
html = str(uf.read())
print(html)

liste = findall('<ul class="tel-result-actions sl-screenonly sl-floatlist"><li><a class="tel-result-action sl-icon-call" href="tel:+[\d]', html)

print(liste)