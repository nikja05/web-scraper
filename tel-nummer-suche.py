"""
Dieses Programm nimmt user input und sucht auf
search.ch nach den entsprechenden Telefonnummern
"""
from urllib import request, parse
from re import findall

def suche(was, wo):
    uf = request.urlopen(url)
    html = str(uf.read())
    resultat = findall(pattern, html)
    return resultat[0]
    
print("Bitte verwende keine umlaute, sondern schreibe sie als (ü -> ue)")
user_was = input("Was suchst du? ")
user_wo = input("Wo suchst du es? ")

url = "https://search.ch/tel/?was=" + user_was + "&wo=" + user_wo
pattern = "title=\"Anrufen\">([0-9]{3} [0-9]{3} [0-9]{2} [0-9]{2})"
telefon_nummer = suche(user_was, user_wo)

print(f"Du kannst hier anrufen: {telefon_nummer}")