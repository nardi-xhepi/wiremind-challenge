# Documentation pour ExpediaSpider

Le script `ExpediaSpider` est une araignée Scrapy pour scraper les données de vol du site Expedia.fr.

## Pré-requis
- Python 3.7+
- Scrapy (Installez avec `pip install scrapy`)

## Utilisation

Cette araignée Scrapy a besoin de quatre arguments lors de l'exécution : `origin`, `destination`, `departure_date`, `return_date`.

L'araignée peut être exécutée avec la commande suivante :
```bash
scrapy crawl expedia -a origin="Paris" -a destination="Munich" -a departure_date="01/07/2023" -a return_date="15/07/2023" -O expedia.json
```
Cette commande lancera le Spider qui va scraper les informations de vol entre Paris et Munich, en partant le 1er juillet 2023 et en revenant le 15 juillet 2023.

Notez que la date doit être formatée en `"DD/MM/YYYY"`.

## Output
L'araignée retournera une liste de vols disponibles avec les détails suivants : numéro de vol, origine, destination, heure de départ, heure d'arrivée, classe et prix.

## Notes

Ce script utilise le contenu de l'appel API étudié sur le site de expedia.fr



# Documentation pour TransaviaSpider

Le script `TransaviaSpider` est une araignée Scrapy pour scraper les données de vol du site transavia.com.

## Pré-requis
- Python 3.7+
- Scrapy (Installez avec `pip install scrapy`)

## Utilisation

Cette araignée Scrapy a besoin de quatre arguments lors de l'exécution : `origin`, `destination`, `departure_date`, `return_date`.

L'araignée peut être exécutée avec la commande suivante :
```bash
scrapy crawl transavia -a origin="ORY" -a destination="FCO" -a departure_date="01/07/2023" -a return_date="15/07/2023" -O transavia.json
```
Cette commande lancera le Spider qui va scraper les informations de vol entre Paris et Rome, en partant le 1er juillet 2023 et en revenant le 15 juillet 2023.

Notez que la date doit être formatée en `"DD/MM/YYYY"`. Egalement, vous devez insérer comme nom d'aéroport les identifiants fournis par transavia pour chaque aéroport. Il n'est malheuresement pas possible de mettre directement le nom de la ville de destination.

## Output
L'araignée retournera une liste de vols disponibles avec les détails suivants : numéro de vol, origine, destination, heure de départ, heure d'arrivée, classe et prix.

## Notes

Ce script utilise le contenu de l'appel API étudié sur le site de transavia.fr