# [Projet REG'INNA]

## Présentation du projet

Ce projet a été développé dans le cadre du Hackathon Mobilités 2025, organisé par Île-de-France Mobilités les 13 et 14 novembre 2025. Pour en savoir plus, voici le [Guide des participants et participantes](https://github.com/hackathons-mobilites/hackathon_mobilites_2025/).


### Le problème et la proposition de valeur 

En fauteuil roulant depuis l’adolescence, Ilseem Jung, n’habite qu’à quelques minutes de Denfert-Rochereau et la ligne 6 du métro à Paris (XIVe). 
Pourtant, voilà plus d’un an qu’elle n’y a pas mis les pieds. 

Rendre accessible le réseau de transport en île de France est un vrai défi et va durer plusieurs années. La priorisation des actions est essentielle pour les personnes en charge de la maintenance des équipements et des de celles en charge des programmes de mécanisation des stations, de rénovation des stations et des gares ou bien du programme "Métro pour tous".

**Nos usagers cibles** sont  : 
- les mainteneurs sur le réseau
- les décideurs des projets de rénovation et de mise en accessibilité du réseau 

Dans un second temps, en pouvant coupler cet outil à une recherche d'itinéraire, nos usagers cibles pourraient aussi être des personnes en situation de handicap (mental, moteur, visuel, auditif, dû à l'âge) pour leur permettre de trouver des **itinéraires accessibles**.


### La solution
Il s'agit d'un démonstrateur représentant sur une même carte  : 
* la facilité d'accès des gares et stations, 
* les lieux générateurs de flux PMR, 
* les stations et gares sur lesquelles les validations de personnes âgées sont les plus importantes
* l'état des ascenseurs et escaliers mécaniques des espaces.

Un indicateur de type **score d'accessibilité** sera proposé pour chaque station du réseau afin d'aider les mainteneurs et les décideurs à prioriser les chantiers de rénovation et de mise en accessibilité du réseau.

## Les données mobilisées :

### Données des niveaux d'accessibilité des stations extraites du [Plan PMR](https://eu.ftp.opendatasoft.com/stif/PlansRegion/Plans/Paris_PMR.pdf)

### Données open sources utilisées
    - Référentiel IDFM des stations : 
    - Correspondances entre noms de station :
        https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/zones-de-correspondance
        https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/arrets
    - Metro Connexion 
    - Données de validation  
    - Lieux générateurs de flux PMR :
            - Hôpitaux
            - Etablissements d'accueil d'adultes en situation de handicap
            - Etablissements d'accueil d'enfants en situation de handicap

### Les problèmes surmontés et les enjeux en matière de données
- Extraire les données d'accessibilité d'une correspondance depuis la description textuelle de métro connexion
- Jointure entre les données des différentes sources au niveau de l'identifiant station


### Et la suite ? 
> [!TIP]
> Ici vous vous projetez sur comment vous auriez aimé développer votre projet si vous aviez eu plus de temps ! (Quel cas d'usage pour la suite ? Quelles ressources à mobiliser ?)


## Installation et utilisation
> [!TIP]
> Si vous avez le temps, vous pouvez décrire les étapes d'installation de votre projet (commandes à lancer, ...) et son fonctionnement.
`git clone https://github.com/hackathons-mobilites/hackathon_mobilites_2025.git`
`pip install -r requirements.txt`

Carte

## La licence
> Ici, il faut décrire la ou les licences du projet. Vous pouvez utiliser la licence [MIT](LICENSE), qui est très permissive. Si on souhaite s'assurer que les dérivés du projet restent Open-Source, vous pouvez utiliser la licence [GPLv3](https://github.com/Illumina/licenses/blob/master/gpl-3.0.txt).

Le code et la documentation de ce projet sont sous licence [MIT](LICENSE).
