# Mijn Project

Hier staat een korte beschrijving van het probleem evt. met plaatje.
![picture of the game Rush Hour](rush_hour.png)

## Aan de slag (Getting Started)

### Vereisten (Prerequisites)

Deze codebase is volledig geschreven in [Python3.6.3](https://www.python.org/downloads/). In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

### Structuur (Structure)


### Test (Testing)

Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:

```
python main.py
```

In main.py kunnen er een aantal aanpassingen gedaan worden om verschillende algoritmes te testen:

#### State space
Een NxN grid bestaat uit 2N lanen, N horizontaal en N verticaal. Elke laan heeft een eigen state space. De totale state space van de hele grid is het product van alle state spaces van de lanen. Wanneer we de state space, van een horizontale lijn, bepalen kijken we alleen naar de horizontale auto's en niet naar de verticale auto's. Visa versa voor de verticale lanen. Zodra de state spaces van deze lanen bepaald zijn hoeft er alleen nog maar geteld te worden per grid hoeveel van welke soort lanen er zijn. In het "state_space.py" bestand staat per laan vernoemd wat de bijbehorende state space is. De functie in dat bestand berekent de state space van een grid. Er moet handmatig ingevuld welke soorten lanen er aanwezig zijn in een bepaalde grid.

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

#### Andere waarden

## Auteurs (Authors)

* Liz Mooij
* Coen Prins
* Hiele Wilkes

## Dankwoord (Acknowledgments)

* StackOverflow
* minor programmeren van de UvA
