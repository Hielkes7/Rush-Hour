# Mijn Project

in dit project berekent oplossingen voor verschillende configuraties van een puzzelspel genaamd "Rush-Hour"

Rush-Hour bestaat uit een 2D grid waarop auto's staan die ofwel op & neer ofwel links & rechts kunnen shuiven.
Het doel van Rush-hour is om de rode auto naar de exit te navigeren doormiddel van het wegschuiven van alle
andere auto's die de weg versperren.

Hoewel Rush-Hour berust op een simpel spelprincipes, kunnen bordconfiguraties al te ingewikkeld worden om gemakkelijk op te lossen.
Ook is er momenteel nog geen algemene heuristiek ontwikkeld die het oplossen van elke mogelijke individuele rush hour puzzel vergemakkelijkt.

Voor dit project zijn 7 verschillende bord configuraties verstrekt die allemaal met behulp van verscheidene algoritmes zijn opgelost.


![picture of the game Rush Hour](pic_README/rush_hour.png)

## Aan de slag


### Vereisten

Deze codebase is volledig geschreven in [Python3.6.3](https://www.python.org/downloads/). In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

### Structuur

Alle Python scripts staan in de folder Code. Deze map bestaat uit een aantal submappen: Algorithms, classes en functions. In de map algoritms staat de code voor de random algoritmes (algorithms.py), de breadthfirst search (map breadthfirst) en het backtrack algoritme (backtrack.py). De breadthfirst map bevat een eigen structure en algorithm, omdat deze afwijken van de standaard structuur. De map classes bevat de structuur van een normale game: Hier wordt een nieuwe game en de game auto's in geinitialiseerd. Daarnaast staat hier de hoofd play methode in. In de map functions staan een bestand gamefunctions.py die ondersteunend zijn voor een game, zoals het checken van een winnende conditie of het vinden van een valide zet. Het bestand functions.py bevat algemeen ondersteunende functies zoals het maken van een string van de grid.


### Test

Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:

```
python main.py
```

In main.py kunnen er een aantal aanpassingen gedaan worden om verschillende algoritmes te testen:


#### Game grids
Allereerst kan er in main.py ingesteld worden welke game van Rushhour er wordt gespeeld. Hierin moet de volgende aanpassingen gedaan worden:
* De naam van het CSV file moet veranderd worden
* De gridsize moet aangepast worden op het moment dat er een grotere grid bekeken wordt.


#### A: Random algoritmes
Bij random algoritmes wordt het gameboard door middel van random steps opgelost. Dit kan op een aantal verschillende manieren.  
* Allereerst kunnen alle auto's random een enkele stap doen ("single") of een maximale stap doen ("max").
* Ook kan de gebruiker aan of uit zetten dat een auto die net bewogen is, niet nog een keer bewogen kan worden (non recurring True of False)
* Als winconditie kan het algoritme checken of de rode auto op de juiste plek staat ("win"), maar het algoritme kan ook checken of het pad naar de uitgang voor de rode auto vrij is ("check_path_free") of zelfs het pad naar de uitgang zelfs vrijmaken als alle auto's op het pad van het pad afbewogen kunnen worden ("make_path_free").
* Ten slotte kan het random algoritme visueel gerepresenteerd worden op het moment dat visualisation True is.
Deze opties zijn allemaal individueel te veranderen in main.py.

#### B: Backtrack algoritme
Het backtrack algoritme runt een bepaald aantal games. Dit aantal is zelf aan te passen in main.py. Bij deze games worden een bepaald aantal grids (ook zelf aan te passen in main.py) opgeslagen in een dictionary. De grid is hierbij de key. De values die de key bevat zijn de stappen die nog gdeaan moeten worden om naar de endstate te komen. Vervolgens wordt er weer een bepaald aantal keer het random algoritme uitgevoerd (in te stellen in main.py). Bij het uitvoeren van deze games wordt na iedere stap gekeken of de huidige grid voorkomt in de grid dictionary. Als dit zo is, worden de moves die nog in de grid dictionary staan uitgevoerd. De volgende waardes kunnen dus aangepast worden:
* Aantal keer uitvoeren random algoritme voor het vullen van de grid dictionary.
* Aantal grids die worden toegevoegd vanaf de endstate.
* Aantal keer uitvoeren van het random algoritme voor het vergelijken met de grid dictionary.

#### C: Breadthfirst algoritme

Het breadthfirst algoritme (BFS) vind de oplossing van een puzzelconfiguratie, doormiddel van het creeeren van een complete stamboom van nodes waarin elke mogelijke move configuratie wordt
doorlopen tot de oplossing gevonden is.
Het voordeel van dit algoritme is dat de gevonden oplossing altijd de snelst mogelijke is
Het nadeel is echter dat het erg veel geheugen en rekenkracht vraagt om te runnen. Hierdoor kunnen enkel de eerste 4 puzzelconfiguraties opgelost worden, binnen een praktische tijdsduur.


Er zijn twee verschillende wincondities
  - "path_free" kijkt of het pad naar de uitgang vrij is
  - "one_blocker" komt 1 stap eerder namelijk wanneer er enkel 1 auto is die de vrije doorgang blokkeert die genoeg ruimte heeft om weggeschoven te worden.

      Ondanks dat de tweede win conditie meer rekenkracht per node vergt, vindt het de oplossing gemiddeld sneller omdat het 1 niveau eerder klaar is.

Er zijn ook twee mogelijkheden voor het aantal hokjes dat een auto verplaatst per move:
  -"max_step" hierbij beweegt een auto het maximaal aantal mogelijke stappen
  -"single_step" hierbij beweegt een auto 1 hokje

Er zijn twee prune mogelijkheden

- "pre" checkt voordat het een node toevoegd aan de wachtrij van BFS of de bordconfiguratie niet al eerder is doorlopen
- "post" voegt alle nodes toe aan de wachtrij, maar checkt voor duplicates als de node uit de wachtrij gehaald wordt, dit voorkomt dat dubbele kinderen in de wachtrij worden gezet.


#### Andere waarden


#### State space
Een NxN grid bestaat uit 2N lanen, N horizontaal en N verticaal. Elke laan heeft een eigen state space. De totale state space van de hele grid is het product van alle state spaces van de lanen. Wanneer we de state space, van een horizontale lijn, bepalen kijken we alleen naar de horizontale auto's en niet naar de verticale auto's. Visa versa voor de verticale lanen. Zodra de state spaces van deze lanen bepaald zijn hoeft er alleen nog maar geteld te worden per grid hoeveel van welke soort lanen er zijn. In het "state_space.py" bestand staat per laan vernoemd wat de bijbehorende state space is. De functie in dat bestand berekent de state space van een grid. Er moet handmatig ingevuld welke soorten lanen er aanwezig zijn in een bepaalde grid.

## Auteurs

* Liz Mooij
* Coen Prins
* Hiele Wilkes

## Dankwoord

* StackOverflow
* Minor programmeren van de UvA
* Onze supervisors Nigel van Herwijnen & Reitze Jansen
