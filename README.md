# SpamDetectorAI 🛡️

## Contexte du Projet

Ce projet vise à concevoir un système intelligent de détection de spams à partir d’emails. Cette initiative s'inscrit dans le cadre du renforcement de la sécurité des communications et servira de base à une solution évolutive destinée à être intégrée aux plateformes de messagerie des clients.

## Objectif

L’objectif principal est de développer un modèle de classification performant, capable de distinguer automatiquement les emails malveillants (Spam) des messages légitimes (Ham). La solution combine des techniques avancées de **Traitement du Langage Naturel (NLP)** et d’**Apprentissage Supervisé**.

## Fonctionnalités et Étapes du Projet

### 1. Analyse des Données 📊
-   **Exploration du Dataset** : Examen de la structure, des types de colonnes et du format des emails.
-   **Nettoyage** : Détection et traitement des valeurs manquantes et des doublons.
-   **Analyse de Distribution** : Étude de l'équilibre entre les classes (Spam vs Ham).
-   **Visualisation** : Génération de **WordClouds** pour identifier les termes fréquents dans chaque catégorie.

### 2. Prétraitement du Texte (NLP) 📝
Le pipeline de prétraitement inclut les étapes suivantes :
-   **Normalisation** : Conversion du texte en minuscules.
-   **Nettoyage** : Suppression des doublons et des entrées vides.
-   **Tokenisation** : Découpage des emails en mots individuels.
-   **Stopwords** : Suppression des mots vides (mots de liaison sans valeur sémantique forte).
-   **Nettoyage Avancé** : Suppression de la ponctuation et des caractères spéciaux.
-   **Stemming** : Réduction des mots à leur racine (via `PorterStemmer`).
-   **Vectorisation** : Transformation du texte en vecteurs numériques (TF-IDF ou CountVectorizer).

### 3. Modélisation et Entraînement 🤖
-   Entraînement de plusieurs modèles de classification.
-   Comparaison et analyse des performances.
-   Optimisation des hyperparamètres.
-   Sauvegarde du meilleur modèle (`best_text_classifier.pkl`).

### 4. Application Utilisateur 💻
Une interface utilisateur interactive a été développée avec **Streamlit** pour permettre la détection en temps réel.
-   **Dashboard** : Vue d'ensemble du projet.
-   **Page de Prédiction** : Zone de saisie pour tester des emails et obtenir un verdict instantané.

## Installation et Lancement

### Prérequis
-   Python 3.8+
-   Les dépendances listées dans `requirements.txt`

### Installation
```bash
git clone https://github.com/bouchramilo/SpamDetectorAI
cd SpamDetectorAI
pip install -r requirements.txt
```

### Lancement de l'application
```bash
streamlit run app/main.py
```

## Structure du Projet

```
SpamDetectorAI/
├── app/
│   ├── main.py              # Page d'accueil de l'application Streamlit
│   └── pages/
│       └── prediction.py    # Page de prédiction
├── data/                    # Données brutes et traitées
├── models/                  # Modèles entraînés (.pkl)
├── notebooks/               # Notebooks Jupyter d'analyse et d'entraînement
├── src/                     # Scripts sources (fonctions utilitaires)
├── requirements.txt         # Liste des dépendances
└── README.md                # Documentation du projet
```
