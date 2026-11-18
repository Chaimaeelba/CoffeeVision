
# CoffeeVision

### Système intelligent de comptage automatique des boissons servies par vision par ordinateur

## 1. Présentation du projet

CoffeeVision est une solution de vision par ordinateur destinée à automatiser le comptage des boissons servies dans un café.

Une caméra fixe observe le comptoir. Le système analyse le flux vidéo, détecte les contenants (tasses, verres et gobelets), suit leurs déplacements et identifie les événements de service.

L'objectif est de fournir un comptage fiable, des statistiques exploitables et une interface de suivi de l'activité.

## 2. Problématique

Le comptage manuel des boissons servies est répétitif et peut entraîner des erreurs.

La principale difficulté consiste à distinguer la présence d'un contenant d'un véritable événement de service.

Une tasse visible sur plusieurs images ne doit pas être comptée plusieurs fois.

CoffeeVision répond à cette problématique grâce à la détection d'objets, au suivi multi-objets et à une logique de comptage basée sur le franchissement d'une zone de retrait.

## 3. Objectifs

- Détecter automatiquement les tasses, verres et gobelets.
- Attribuer un identifiant unique à chaque contenant suivi.
- Identifier les franchissements de la zone de retrait dans le sens attendu.
- Éviter les doubles comptages.
- Enregistrer les événements avec leur date, heure et session.
- Fournir des statistiques journalières et horaires.
- Permettre l'export des résultats au format CSV.
- Évaluer les performances du modèle.
- Assurer la reproductibilité et le déploiement de l'application.

## 4. Fonctionnalités principales

| Fonctionnalité | Description |
|---|---|
| Acquisition vidéo | Lecture d'une vidéo enregistrée ou d'une caméra fixe |
| Détection | Identification des contenants avec YOLO |
| Suivi | Maintien de l'identité des objets dans le temps |
| Comptage | Détection des franchissements valides |
| Anti-doublon | Un seul événement par service |
| Stockage | Enregistrement des sessions et événements |
| Statistiques | Totaux journaliers et horaires |
| Export | Génération de rapports CSV |
| Correction | Signalement et correction des événements |
| MLOps | Suivi des expérimentations et des modèles |

## 5. Architecture du système

Le traitement repose sur une chaîne composée de plusieurs étapes :

```text
Caméra / Vidéo
      |
      v
Acquisition et traitement vidéo
      |
      v
Détection des contenants (YOLO)
      |
      v
Suivi multi-objets (Tracking)
      |
      v
Détection du franchissement
      |
      v
Validation et comptage
      |
      v
Stockage des événements (SQLite)
      |
      v
API REST (FastAPI)
      |
      v
Dashboard / Statistiques / Export CSV
```

Le comptage est déclenché lorsqu'un contenant suivi traverse la zone de retrait dans la direction attendue.

## 6. Technologies envisagées

| Domaine | Technologies |
|---|---|
| Langage principal | Python |
| Traitement vidéo | OpenCV |
| Détection d'objets | YOLO |
| Suivi multi-objets | ByteTrack / BoT-SORT |
| Backend | FastAPI |
| Base de données | SQLite |
| Frontend | HTML, CSS, JavaScript ou React |
| Machine Learning Operations | MLflow |
| Tests | Pytest |
| Conteneurisation | Docker |
| Intégration continue | GitHub Actions |
| Gestion de versions | Git / GitHub |
| Gestion de projet | Jira |

## 7. Structure du projet

```text
CoffeeVision/
|
|-- src/            # Code source
|-- data/           # Vidéos, images et annotations
|-- models/         # Modèles entraînés
|-- notebooks/      # Expérimentations ML/DL
|-- tests/          # Tests unitaires et d'intégration
|-- docs/           # Documentation
|
|-- README.md
|-- .gitignore
```

Cette structure sera enrichie progressivement au cours du développement.

## 8. Données et intelligence artificielle

Le projet repose sur des vidéos de comptoir représentant différents scénarios :

- Conditions d'éclairage variées.
- Différents types de contenants.
- Objets partiellement masqués.
- Plusieurs contenants simultanés.
- Déplacements et retours de contenants.
- Scènes sans événement de service.

Les données seront annotées pour entraîner et évaluer le modèle de détection.

Les ensembles d'entraînement, de validation et de test seront séparés par session vidéo afin d'éviter les fuites de données.

## 9. Évaluation et performances

Les performances seront évaluées à l'aide de plusieurs indicateurs :

- Précision et rappel de détection.
- mAP pour la détection d'objets.
- Erreur de comptage.
- Nombre de faux événements.
- Débit de traitement en images par seconde (FPS).
- Absence de doublons après relancement d'une session.

## 10. DevOps et MLOps

Le projet adopte une démarche DevOps et MLOps comprenant :

- Git et GitHub pour le versionnement collaboratif.
- Branches dédiées au développement des fonctionnalités.
- Pull Requests et revues de code.
- Tests automatisés.
- GitHub Actions pour l'intégration continue.
- MLflow pour le suivi des expériences.
- Docker pour le déploiement reproductible.

## 11. Organisation du projet

Le développement est organisé en six axes :

1. Gestion de projet et collaboration.
2. Collecte et préparation des données.
3. Détection, suivi et comptage.
4. API, stockage et tableau de bord.
5. Tests, intégration continue et déploiement.
6. Suivi des expériences et pipelines MLOps.

Les tâches sont organisées et suivies dans Jira.

## 12. Équipe du projet

| Membre | Établissement |
|---|---|
| Omar Afidi | ENSA Khouribga |
| Chaimae Elbahchoumi | ENSA Khouribga |
| Mohammed Agoulzi | ENSA Khouribga |



