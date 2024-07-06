# DSA

## Installation
mit Conda:
```
conda create --prefix ./env python=3.10
```
```
conda activate ./env
```
```
pip install -r requirements.txt
```
## Benutzung
In ```aufbereitung.ipynb``` wurden alle Daten in ein gemeinsames ```data/combined.csv``` umgewandelt. Die Policy Daten wurden in ```data/Policy_Weekly_Extended.csv``` aggregiert. Für die Deskriptive Analyse wird ```exploration.ipynb``` verwendet. 

Um das Corona Dashboard zu verwenden muss ```corona_dashboard_skript.py``` ausgeführt werden.

Die statistischen Modelle wurden in ```models.ipynb``` implementiert.

Der ChatBot wurde in ```chat_bot.ipynb``` implementiert.


## Links zu Covid Maßnahmen
https://www.bundesgesundheitsministerium.de/coronavirus/chronik-coronavirus

### Infos nach Bundesländer
https://www.bundesregierung.de/breg-de/themen/coronavirus/corona-bundeslaender-1745198

## Quellen
### Tote allgemein
https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Sterbefaelle-Lebenserwartung/Publikationen/Downloads-Sterbefaelle/statistischer-bericht-sterbefaelle-tage-wochen-monate-aktuell-5126109.html

https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Sterbefaelle-Lebenserwartung/Publikationen/Downloads-Sterbefaelle/statistischer-bericht-sterbefaelle-tage-wochen-monate-endg-5126108.html?nn=209016

### Corona Tote
https://github.com/robert-koch-institut/COVID-19-Todesfaelle_in_Deutschland

### Infektionen
https://github.com/robert-koch-institut/COVID-19_7-Tage-Inzidenz_in_Deutschland

### Hospitalisierungen
https://github.com/robert-koch-institut/COVID-19-Hospitalisierungen_in_Deutschland

### Impfungen
https://github.com/robert-koch-institut/COVID-19-Impfungen_in_Deutschland

### Maßnahmen
https://github.com/OxCGRT/covid-policy-tracker
