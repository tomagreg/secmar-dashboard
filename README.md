# Secours en mer : ce qui occupe les CROSS n'est pas ce qui tue

Dashboard Streamlit de data storytelling sur les opérations de secours en mer coordonnées par les CROSS.

**Question centrale** : où, quand et dans quelles situations les opérations de secours deviennent-elles mortelles, et en quoi cela diffère-t-il de ce qui occupe le plus les CROSS ?

**Public visé** : pratiquants et encadrants de loisirs nautiques, acteurs de la prévention.

## Données

- Jeu de données : « Opérations coordonnées par les CROSS » (SECMAR) — https://www.data.gouv.fr/datasets/operations-coordonnees-par-les-cross
- Producteur : Direction des Affaires maritimes, ministère de la Transition écologique.
- Licence : Licence Ouverte / Open Licence 2.0.
- Documentation : https://mtes-mct.github.io/secmar-documentation/
- Fichiers utilisés : `operations.csv` et `operations_stats.csv` (jointure 1-1 sur `operation_id`). Ils ne sont pas embarqués : ils sont téléchargés dans `data/` au premier lancement, puis réutilisés.

## Lancer l'application

Python 3.13.

```bash
python -m venv .venv
.venv/Scripts/activate        # Windows ; sous Linux/macOS : source .venv/bin/activate
pip install -r requirements.txt
python -m utils.io            # télécharge les données dans data/ (optionnel, fait aussi au lancement)
streamlit run app.py
```

## Structure

```
app.py                  # cache, barre latérale, enchaînement des sections
sections/
  intro.py              # accroche, contexte, public, limites
  overview.py           # KPI liés aux filtres, évolution annuelle, saisonnalité
  deep_dives.py         # fréquence contre gravité, météo et distance, carte
  conclusions.py        # qualité des données, enseignements, suites
utils/
  io.py                 # téléchargement avec cache, chargement, licence
  prep.py               # nettoyage, contrôles qualité, filtres, tables agrégées
  viz.py                # fonctions de graphiques Plotly
  i18n.py               # textes de l'interface en français et en anglais
data/                   # CSV téléchargés (ignorés par git)
assets/logo.png         # logo affiché dans « About me »
```

L'interface est disponible en français et en anglais (choix en haut de la barre latérale). Les libellés issus des données (CROSS, catégories, motifs) restent en français.

## Méthode

- **Opération mortelle** : au moins une personne décédée ou disparue (`nombre_personnes_tous_deces_ou_disparues > 0`).
- **Découvertes de corps** : mortelles par définition, exclues des calculs de part d'opérations mortelles.
- **Durées** : de la réception de l'alerte à la fin de l'opération ; les durées négatives sont mises à manquantes.
- **Carte** : opérations regroupées par maille de 0,05°, environ 5 km (constante `MAP_GRID_DEG` dans `utils/prep.py`).
- **Classement des motifs** : seuls les motifs d'au moins 200 opérations sont classés (`MIN_OPS_MOTIF`).
- Aucun échantillonnage aléatoire : les résultats sont déterministes.
- Performance : données chargées une fois (`st.cache_resource`), tables filtrées et agrégées mises en cache par combinaison de filtres (`st.cache_data`).