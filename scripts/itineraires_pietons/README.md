# Itinéraires piétons — Architecture modulaire

Ce package génère des itinéraires piétons entre arrêts de transport (rail/metro/tram) et points d'intérêt (POI) proches.

## Architecture

Le code suit une **architecture en couches (Layered Architecture)** qui sépare clairement les responsabilités :

```
itineraires_pietons/
├── __init__.py          # Package root
├── __main__.py          # Point d'entrée module
├── cli.py               # Interface CLI (Presentation Layer)
├── orchestrator.py      # Orchestration (Application Layer)
├── config.py            # Configuration et constantes
├── data_loader.py       # Chargement données (Data Layer)
├── spatial_service.py   # Recherche spatiale (Business Logic)
├── routing_service.py   # Calcul itinéraires (Business Logic)
└── export_service.py    # Export GeoJSON (Business Logic)
```

### Couches

1. **Presentation Layer** (`cli.py`)
   - Interface en ligne de commande
   - Parsing des arguments
   - Configuration du logging

2. **Application Layer** (`orchestrator.py`)
   - Orchestre le workflow complet
   - Coordonne les services métier
   - Gère les erreurs et le logging

3. **Business Logic Layer**
   - `spatial_service.py`: recherche spatiale (KDTree, haversine)
   - `routing_service.py`: calcul d'itinéraires via Valhalla
   - `export_service.py`: création et export de GeoJSON

4. **Data Layer** (`data_loader.py`)
   - Chargement des fichiers POI et arrêts
   - Nettoyage et filtrage des données
   - Validation des colonnes

5. **Configuration** (`config.py`)
   - Constantes et paramètres
   - Chemins de fichiers
   - Types de POI pertinents

## Utilisation

### Installation des dépendances

```powershell
pip install pandas numpy scipy routingpy tqdm
```

### Exécution basique

```powershell
# Depuis le dossier 'autres'
python -m itineraires_pietons

# Ou avec options
python -m itineraires_pietons --limit 10 --verbose
```

### Options CLI

```powershell
python -m itineraires_pietons --help

Options:
  --poi PATH              Fichier CSV des POI
  --arrets PATH           Fichier parquet des arrêts
  --output PATH           Dossier de sortie
  --distance METERS       Rayon de recherche (défaut: 500m)
  --limit N               Limiter à N itinéraires (tests)
  --valhalla-url URL      URL serveur Valhalla
  -v, --verbose           Mode debug
```

### Utilisation programmatique

```python
from itineraires_pietons import ItineraryOrchestrator

orchestrator = ItineraryOrchestrator()
count = orchestrator.generate_itineraries(
    limit=50,  # Test sur 50 itinéraires
    max_distance=750  # Rayon de 750m
)
print(f"{count} itinéraires générés")
```

## Avantages de cette architecture

1. **Séparation des responsabilités** : chaque module a un rôle clair
2. **Testabilité** : chaque service peut être testé indépendamment
3. **Maintenabilité** : modifications localisées sans impact sur les autres couches
4. **Réutilisabilité** : les services peuvent être utilisés dans d'autres contextes
5. **Extensibilité** : facile d'ajouter de nouveaux services (ex: manifest CSV, validation)

## Tests rapides

```powershell
# Test avec 10 itinéraires seulement
python -m itineraires_pietons --limit 10 -v

# Test avec rayon différent
python -m itineraires_pietons --distance 300 --limit 5
```

## Prochaines évolutions

- Tests unitaires (pytest) pour chaque service
- Projection EPSG:2154 pour distances métriques exactes
- Parallélisation des calculs Valhalla
