# BeterSN
Waarom je BSN op straat als dat niet hoeft?

## Installatie
Clone dit repository naar je eigen laptop/ computer met het commando:
```ps
git clone https://www.github.com/donkere-vader/betersn.git
```

Heb je geen git geinstalleerd?
Download de code dan door te klikken op de groene knop "Code" en selecteer "Download Zip".

## Uitvoeren
Voor het uivoeren van de code is de python interperter nodig. Deze is te downloaden op de officiele python website. [python.org](https://www.python.org)
Dit programma werkt inniedergeval met python 3.8.5 of hoger.

### Afhankelijkheden (dependencies)
Mijn software maakt gebruik van modules van andere mensen. Als je python hebt geinstalleerd is als het goed is ook de python package manager geinstalleerd (beter bekend als "pip").

Om alle afhankelijkheden te downloaden moet je ervoor zorgen dat je de gedownloade zip hebt uitgepakt en zorg dat je met een commandprompt/ terminal in deze map zit. (Zie punt een op deze website voor een uitleg hoe dat moet: [digitalcitizen.life](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/))

Als je dan in die map zit met je commandprompt/ terminal moet je het commando
```ps
pip install -r requirements.txt
```
runnen. Dit installeert de modules die ik heb gebruikt.

### Start de webserver
Het is een kleine website die je lokaal opstart.
Dit opstarten is zo gepiept.

Zorg ervoor dat je nogsteeds in dezelfde map zit met je commandoprompt (Zoals beschreven in Het kopje Afhankelijkheden).

run dan het commando:
```ps
python run.py
```

Dit start de webserver op. Open dan je browser naar keuze en type in de adres balk: [localhost:5000](http://localhost:5000)
Dit opent de webpagina.

## De website
Gebruik van de website. Volg deze kopjes voor het stappenplan.

### Burger toevoegen
Voordat je echt aan de slag kunt moet je even op de pagina "Nieuwe burger toevoegen" een nieuwe burger toevoegen aan de database. Normaal gesproken zou dit al in het systeem van DigiD staan, maar dit is maar een proof of concept.

Dan kan je deze gebruiker en zijn/ haar id zien op de pagina "Burger overzicht" Dit is natuurlijk ook alleen maar omdat het een proof of concept is. In het echt wil je natuurlijk niet zo'n "export knop" ;). We weten allemaal hoe dat wel eens fout kan gaan.

### Tijdelijk BSN
Om een tijdelijk bsn aan te maken moet je naar de pagina "Genereer BSN" vul hierin het id van de aangemaakt burger in (dit kan je terugvinden op de "Burger overzicht" pagina.) Normaal zou iemand natuurlijk ingelogd zijn op de pagina van DigiD, maar voor nu moet je de webserver even laten weten wie je bent door je id in te vullen.

In het veld "Gebruiken voor" kan je opschrijven waar je dit BSN voor wilt gebruiken. Bijv: "GGD afspraak Provincie, stad"

In het veld "Afloop datum" kan je invullen tot wanneer je dit tijdelijke BSN wilt laten gelden. (In het echt moet er natuurlijk ook een optie zijn om er geen afloop datum aan te hangen, maar dit is maar een proof of concept.)

Klik dan op genereer bsn en kopieer dan de tijdelijke bsn die getoont word op de volgende pagina. Dit is je tijdelijke BSN.

### Gebruik tijdelijke BSN
(We houden even het voorbeeld van de GGD afspraak aan.)
Als je dan bij de GGD aankomt dan kan je je tijdelijke BSN laten zien.
De medewerker opent dan ook de website en gaat naar de pagina "Valideer BSN".
Hierop kunnen zij uw BSN nummer invullen en als dit klopt krijgen ze persoonlijke informatie over je terug die ze kunnen vergelijken met je ID kaart. (Bijv: foto, naam, geboortedag etc.).

Ook krijgen ze dan te zien waar de BSN voor is bedoeld in het veld "usecase" en zien ze de afloop datum in het veld "expiry_date".

## Op grote schaal
Dit is natuurlijk maar een proof of concept. Als dit verder uitgewerkt zou worden dan zou het natuurlijk veel handiger moeten. Bijvoorbeeld een QR code of Bar code als tijdelijk BSN, zodat dit makkelijk gescanned kan worden bij een balie/ GGD testcentrum.

En dan zou het natuurlijk geintegreed moeten worden met de systemen van DigiD. Met een login en mooi dashboard van je tijdelijke BSN nummers en dat je die dan ook kut verwijderen etc.