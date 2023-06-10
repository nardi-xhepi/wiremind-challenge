# Documentation succincte pour ExpediaSpider

Le script `ExpediaSpider` est une araignée Scrapy pour scraper les données de vol du site Expedia.fr.

## Pré-requis
- Python 3.7+
- Scrapy (Installez avec `pip install scrapy`)

## Utilisation

Cette araignée Scrapy a besoin de quatre arguments lors de l'exécution : `origin`, `destination`, `departure_date`, `return_date`.

L'araignée peut être exécutée avec la commande suivante :
```bash
scrapy crawl expedia -a origin="Paris" -a destination="New York" -a departure_date="01/07/2023" -a return_date="15/07/2023 -O output.json"
```
Cette commande lancera le Spider qui va scraper les informations de vol entre Paris et New York, en partant le 1er juillet 2023 et en revenant le 15 juillet 2023.

Notez que la date doit être formatée en `"DD/MM/YYYY"`.

## Output
L'araignée retournera une liste de vols disponibles avec les détails suivants : numéro de vol, origine, destination, heure de départ, heure d'arrivée, classe et prix.

## Notes

Ce script utilise le contenu de l'appel API étudié sur le site de expedia.fr