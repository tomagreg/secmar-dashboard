"""UI texts in French and English."""

import streamlit as st

TEXTS = {
    "fr": {
        "title": "Secours en mer : ce qui occupe les CROSS n'est pas ce qui tue",
        "license": "Source : « Opérations coordonnées par les CROSS » (SECMAR), Direction des "
                   "Affaires maritimes, data.gouv.fr — Licence Ouverte / Open Licence 2.0.",
        "dataset": "Jeu de données",
        "doc": "Documentation",
        "filters": "Filtres",
        "period": "Période (années)",
        "period_help": "{year} est incomplet et exclu par défaut.",
        "zone": "Zone",
        "zone_all": "Toutes",
        "zone_metro": "Métropole",
        "zone_overseas": "Outre-mer",
        "cross": "CROSS",
        "all_m": "Tous",
        "category": "Catégorie d'évènement",
        "all_f": "Toutes",
        "map_var": "Variable de la carte",
        "var_operations": "Nombre d'opérations",
        "var_letalite": "Part d'opérations mortelles (%)",
        "no_data": "Aucune opération ne correspond aux filtres.",
        "about": "À propos",
        "about_course": "Analyse et visualisation de données",
        "about_prof": "Projet proposé par : Prof. Mano Mathew",
        # Intro
        "intro_header": "Ce qui occupe les CROSS n'est pas ce qui tue",
        "intro_hook": "Sur 100 opérations de secours en mer, environ 97 se terminent sans mort ni "
                      "disparu. Pourtant, plus de 13 600 personnes sont mortes ou ont disparu depuis "
                      "1984. **Où, quand et dans quelles situations les opérations deviennent-elles "
                      "mortelles ?**",
        "intro_context": "**Contexte.** Les CROSS (Centres régionaux opérationnels de surveillance et "
                         "de sauvetage) coordonnent les secours en mer sur les côtes françaises et "
                         "outre-mer. La base SECMAR recense chaque opération depuis 1984 : motif, "
                         "lieu, météo, bilan humain.\n\n"
                         "**Public visé.** Pratiquants et encadrants de loisirs nautiques, acteurs "
                         "de la prévention.\n\n"
                         "**Ce que l'on mesure.** Des opérations de secours déclenchées par une "
                         "alerte, pas des accidents ni un risque par pratique.",
        "intro_limits": "**Limites à garder en tête.** Aucun nombre de pratiquants : on parle de "
                        "part des opérations, jamais de risque par activité. 14 % des opérations "
                        "n'ont pas de coordonnées, 27 à 29 % n'ont pas de météo. L'année en cours "
                        "est incomplète. Les données ne montrent que des corrélations, pas des causes.",
        # Overview
        "overview_header": "Une activité massive, saisonnière et en forte hausse",
        "kpi_ops": "Opérations",
        "kpi_people": "Personnes impliquées",
        "kpi_deaths": "Morts et disparus",
        "kpi_lethal": "Opérations mortelles",
        "kpi_lethal_help": "Part des opérations avec au moins une personne décédée ou disparue.",
        "kpi_duration": "Durée médiane",
        "kpi_duration_help": "Entre la réception de l'alerte et la fin de l'opération.",
        "ops_year": "Opérations par année",
        "axis_year": "Année",
        "axis_ops": "Nombre d'opérations",
        "incomplete": "{year} incomplet",
        "read_note": "Les commentaires sous les graphiques portent sur l'ensemble des données "
                     "1984-2025 ; les graphiques et les indicateurs, eux, suivent les filtres.",
        "read_year": "#### Quatre fois plus\n\n"
                     "Le nombre d'opérations a **presque quadruplé** : environ 4 200 en 1985, 9 "
                     "800 en 2010, **16 300 en 2025**. Cette hausse **ne signifie pas** que la "
                     "mer est devenue plus dangereuse : elle reflète probablement à la fois "
                     "**plus de pratiquants** et une **meilleure remontée des alertes**. C'est un "
                     "constat, pas une explication.",
        "ops_month": "Opérations par mois",
        "axis_month": "Mois",
        "months": ["janv.", "févr.", "mars", "avr.", "mai", "juin",
                   "juil.", "août", "sept.", "oct.", "nov.", "déc."],
        "read_month": "#### Un pic estival\n\n"
                      "L'activité suit le **calendrier des loisirs** : **juillet et août** "
                      "concentrent à eux seuls **34 % des opérations**, contre moins de 5 % pour "
                      "chaque mois d'hiver. **L'été** est la période où la prévention touche le "
                      "plus de monde.",
        # Deep dives
        "dd_header": "Fréquence, gravité, conditions, lieux",
        "a_sub": "A. Les situations les plus fréquentes ne sont pas les plus graves",
        "share_ops": "Part des opérations (%)",
        "share_deaths": "Part des morts et disparus (%)",
        "axis_share": "Part du total (%)",
        "axis_category": "Catégorie d'évènement",
        "read_a1": "#### Fréquence contre gravité\n\n"
                   "Les deux barres ne racontent pas la même histoire. **Avaries et fausses "
                   "alertes** représentent **39 % des opérations** mais **moins de 2 % des "
                   "morts** et disparus. À l'inverse, les trois catégories d'**accidents "
                   "individuels** ne pèsent que 14 % des opérations mais **52 % des décès**. Ce "
                   "qui occupe les CROSS au quotidien **n'est donc pas ce qui tue**.",
        "axis_lethal": "Opérations mortelles (%)",
        "axis_motif": "Motif",
        "mean": "Moyenne {v:.1f} %",
        "read_a2": "#### Seul dans l'eau\n\n"
                   "Rapportés à leur nombre d'opérations, certains motifs sont **bien plus graves "
                   "que la moyenne** (environ 2,3 %) : **disparu en mer (59 %)**, chute de "
                   "falaise ou personne emportée par une lame (49 %), **homme à la mer (31 %)**, "
                   "plongée en apnée (28 %), **baignade (18 %)**. Ce sont presque tous des "
                   "situations où **une personne se retrouve seule dans l'eau**. Seuls les motifs "
                   "d'au moins {n} opérations sont classés ; les découvertes de corps sont "
                   "exclues.",
        "b_sub": "B. La gravité ne se lit pas dans le vent seul",
        "axis_force": "Force (échelle de Beaufort pour le vent, de Douglas pour la mer)",
        "axis_wind": "Vent",
        "axis_sea": "État de la mer",
        "read_b1": "#### La mer compte\n\n"
                   "Les deux courbes partagent la même échelle de force. Par vent calme à frais "
                   "(force 0 à 6), la part d'opérations mortelles reste collée à la moyenne, "
                   "entre 2,2 et 2,5 % : **le vent distingue à peine** les opérations graves. "
                   "**L'état de la mer est plus parlant** : 1,7 % par mer calme, 2,9 % à force 4, "
                   "4,8 % à force 6 et **environ 8 % au-delà**. Les forces extrêmes sont rares "
                   "(quelques centaines d'opérations), leurs valeurs sont donc **plus "
                   "incertaines**.",
        "axis_distance": "Distance à la côte (milles nautiques)",
        "read_b2": "#### Deux extrémités dangereuses\n\n"
                   "La **bande côtière** concentre l'essentiel : **54 % des opérations** et **46 "
                   "% des morts** et disparus ont lieu à moins d'un demi-mille du bord. **Au "
                   "large** (plus de 50 milles), les opérations sont moins nombreuses (14 %) mais "
                   "pèsent **25 % des décès**. La gravité se joue aux deux extrémités : **près du "
                   "bord par le volume**, **loin au large par l'isolement**.",
        "c_sub": "C. Où se concentrent les opérations",
        "read_map": "#### Côtes très fréquentées\n\n"
                    "Les opérations suivent le **trait de côte** et se concentrent sur les "
                    "littoraux les plus fréquentés : **Bretagne, Méditerranée, Manche**. Chaque "
                    "point regroupe une maille d'environ 5 km ; sa **taille** indique le nombre "
                    "d'opérations, sa **couleur** la variable choisie dans la barre latérale. En "
                    "mode « part d'opérations mortelles », une maille avec très peu d'opérations "
                    "peut afficher 0 % ou 100 % : **à lire avec la taille du point**. Découvertes "
                    "de corps exclues.\n\n"
                    "**Critique.** Les coordonnées saisies sont parfois **imprécises** : certains "
                    "points **tombent à terre**, parfois loin du rivage. La position d'une maille "
                    "est indicative, pas exacte (voir la section qualité des données).",
        "axis_cross": "CROSS",
        "read_cross": "#### Deux CROSS dominent\n\n"
                      "Deux CROSS assurent **près de la moitié de l'activité** : **Étel** "
                      "(Atlantique, 25 %) et **La Garde** (Méditerranée, 24 %), loin devant "
                      "Corsen (11 %). Ce sont les façades où la **plaisance et les loisirs "
                      "nautiques** sont les plus denses.",
        # Quality and conclusions
        "q_header": "Qualité des données et limites",
        "q_dup_ids": "Identifiants en double",
        "q_dup_rows": "Lignes dupliquées",
        "q_neg": "Durées négatives",
        "q_neg_help": "Fin d'opération avant la réception de l'alerte : durée mise à manquante.",
        "q_coords": "Coordonnées invalides",
        "q_coords_help": "Hors bornes ou valeurs factices (0, 0), -90 ou -180 : mises à manquantes.",
        "q_period": "Période couverte : {start} – {end}, {rows} opérations. {bodies} découvertes "
                    "de corps, mortelles par définition, sont exclues des calculs de part "
                    "d'opérations mortelles.",
        "q_land": "**Coordonnées imprécises.** {pct:.0f} % des opérations localisées ont une "
                  "distance à la côte de 0. Selon la documentation SECMAR, cela correspond à une "
                  "opération très près du bord ou à l'intérieur des terres (fausse alerte). "
                  "S'y ajoutent des positions approximatives, probablement dues à la saisie ou à "
                  "la position de l'alerte plutôt que de l'incident, qui placent des points à "
                  "terre sur la carte. Les analyses par lieu et par distance à la côte sont donc à lire comme "
                  "des ordres de grandeur.",
        "q_missing": "Valeurs manquantes par colonne",
        "q_missing_col": "Valeurs manquantes (%)",
        "q_bias": "**Biais connus.** Les données ne recensent que les alertes reçues par les CROSS, "
                  "pas tous les incidents. Il n'existe pas de nombre de pratiquants : on ne peut "
                  "pas calculer de risque par activité. La façon de déclarer a pu évoluer depuis "
                  "1984. Les données de personnes ne sont présentées qu'agrégées.",
        "c_header": "Enseignements et suites",
        "c_messages": "1. **Le quotidien n'est pas le drame** : avaries et fausses alertes occupent "
                      "les CROSS mais causent peu de décès.\n"
                      "2. **La gravité vient des accidents individuels** (homme à la mer, baignade).\n"
                      "3. **La météo seule ne l'explique pas** : le vent distingue peu les "
                      "opérations mortelles.",
        "c_next": "**Implications.** Cibler la prévention estivale sur la bande côtière et les "
                  "accidents individuels. Ce sont des pistes suggérées par les données, pas des "
                  "preuves causales.\n\n"
                  "**Suites possibles.** Croiser avec des données de fréquentation pour obtenir un "
                  "vrai taux de risque ; ajouter le fichier des moyens engagés (SNSM, hélicoptères).",
    },
    "en": {
        "title": "Sea rescue: what keeps the CROSS busy is not what kills",
        "license": "Source: “Opérations coordonnées par les CROSS” (SECMAR), French Directorate of "
                   "Maritime Affairs, data.gouv.fr — Licence Ouverte / Open Licence 2.0.",
        "dataset": "Dataset",
        "doc": "Documentation",
        "filters": "Filters",
        "period": "Period (years)",
        "period_help": "{year} is incomplete and excluded by default.",
        "zone": "Area",
        "zone_all": "All",
        "zone_metro": "Mainland France",
        "zone_overseas": "Overseas",
        "cross": "CROSS",
        "all_m": "All",
        "category": "Event category",
        "all_f": "All",
        "map_var": "Map variable",
        "var_operations": "Number of operations",
        "var_letalite": "Share of fatal operations (%)",
        "no_data": "No operation matches the filters.",
        "about": "About me",
        "about_course": "Data analysis and visualisation",
        "about_prof": "Project proposed by: Prof. Mano Mathew",
        # Intro
        "intro_header": "What keeps the CROSS busy is not what kills",
        "intro_hook": "Out of 100 sea rescue operations, about 97 end with no one dead or missing. "
                      "Yet more than 13,600 people have died or gone missing since 1984. **Where, "
                      "when and in which situations do operations become fatal?**",
        "intro_context": "**Context.** The CROSS (Regional Operational Surveillance and Rescue "
                         "Centres) coordinate sea rescue along the French coasts and overseas. "
                         "The SECMAR database records every operation since 1984: reason, "
                         "location, weather, human toll.\n\n"
                         "**Audience.** Water sports practitioners and instructors, prevention "
                         "stakeholders.\n\n"
                         "**What is measured.** Rescue operations triggered by an alert, not "
                         "accidents nor a risk per activity.",
        "intro_limits": "**Limits to keep in mind.** No number of practitioners: we talk about "
                        "share of operations, never risk per activity. 14% of operations have no "
                        "coordinates, 27 to 29% have no weather data. The current year is "
                        "incomplete. The data only show correlations, not causes.",
        # Overview
        "overview_header": "A massive, seasonal and fast-growing activity",
        "kpi_ops": "Operations",
        "kpi_people": "People involved",
        "kpi_deaths": "Dead and missing",
        "kpi_lethal": "Fatal operations",
        "kpi_lethal_help": "Share of operations with at least one person dead or missing.",
        "kpi_duration": "Median duration",
        "kpi_duration_help": "From alert reception to the end of the operation.",
        "ops_year": "Operations per year",
        "axis_year": "Year",
        "axis_ops": "Number of operations",
        "incomplete": "{year} incomplete",
        "read_note": "The comments below the charts describe the whole 1984-2025 dataset; the "
                     "charts and KPIs follow the filters.",
        "read_year": "#### Four times more\n\n"
                     "The number of operations has **almost quadrupled**: about 4,200 in 1985, "
                     "9,800 in 2010, **16,300 in 2025**. This rise **does not mean** the sea "
                     "became more dangerous: it probably reflects both **more people at sea** and "
                     "**better alert reporting**. It is an observation, not an explanation.",
        "ops_month": "Operations per month",
        "axis_month": "Month",
        "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "read_month": "#### A summer peak\n\n"
                      "Activity follows the **leisure calendar**: **July and August** alone "
                      "account for **34% of operations**, against less than 5% for each winter "
                      "month. **Summer** is when prevention reaches the most people.",
        # Deep dives
        "dd_header": "Frequency, severity, conditions, places",
        "a_sub": "A. The most frequent situations are not the most severe",
        "share_ops": "Share of operations (%)",
        "share_deaths": "Share of dead and missing (%)",
        "axis_share": "Share of total (%)",
        "axis_category": "Event category",
        "read_a1": "#### Frequency versus severity\n\n"
                   "The two bars tell different stories. **Breakdowns and false alarms** make up "
                   "**39% of operations** but **less than 2% of dead** and missing. Conversely, "
                   "the three **individual accident** categories account for only 14% of "
                   "operations but **52% of deaths**. What keeps the CROSS busy every day **is "
                   "not what kills**.",
        "axis_lethal": "Fatal operations (%)",
        "axis_motif": "Reason",
        "mean": "Average {v:.1f}%",
        "read_a2": "#### Alone in water\n\n"
                   "Relative to their number of operations, some reasons are **far more severe "
                   "than the average** (about 2.3%): **missing at sea (59%)**, cliff fall or "
                   "swept away by a wave (49%), **man overboard (31%)**, freediving (28%), "
                   "**swimming (18%)**. Almost all are situations where **a person ends up alone "
                   "in the water**. Only reasons with at least {n} operations are ranked; body "
                   "discoveries are excluded.",
        "b_sub": "B. Severity cannot be read from the wind alone",
        "axis_force": "Force (Beaufort scale for wind, Douglas scale for sea)",
        "axis_wind": "Wind",
        "axis_sea": "Sea state",
        "read_b1": "#### Sea state matters\n\n"
                   "Both curves share the same force scale. From calm to fresh wind (force 0 to "
                   "6), the share of fatal operations stays close to the average, between 2.2 and "
                   "2.5%: **wind barely separates** severe operations. **Sea state says more**: "
                   "1.7% in calm sea, 2.9% at force 4, 4.8% at force 6 and **about 8% beyond**. "
                   "Extreme forces are rare (a few hundred operations), so their values are "
                   "**less certain**.",
        "axis_distance": "Distance from the coast (nautical miles)",
        "read_b2": "#### Two dangerous extremes\n\n"
                   "The **coastal strip** concentrates most of it: **54% of operations** and "
                   "**46% of dead** and missing occur less than half a mile from shore. **Far "
                   "offshore** (over 50 miles), operations are fewer (14%) but account for **25% "
                   "of deaths**. Severity plays out at both ends: **near shore through volume**, "
                   "**far offshore through isolation**.",
        "c_sub": "C. Where operations are concentrated",
        "read_map": "#### Crowded coastlines dominate\n\n"
                    "Operations follow the **coastline** and cluster on the busiest shores: "
                    "**Brittany, the Mediterranean, the Channel**. Each point is a cell of about "
                    "5 km; its **size** shows the number of operations, its **colour** the "
                    "variable chosen in the sidebar. In “share of fatal operations” mode, a cell "
                    "with very few operations can show 0% or 100%: **read it together with the "
                    "point size**. Body discoveries excluded.\n\n"
                    "**Caveat.** Recorded coordinates are sometimes **imprecise**: some points "
                    "**fall on land**, sometimes far from the shore. A cell's position is "
                    "indicative, not exact (see the data quality section).",
        "axis_cross": "CROSS",
        "read_cross": "#### Two CROSS dominate\n\n"
                      "Two CROSS handle **almost half of the activity**: **Étel** (Atlantic, 25%) "
                      "and **La Garde** (Mediterranean, 24%), far ahead of Corsen (11%). These "
                      "are the coasts where **yachting and water sports** are densest.",
        # Quality and conclusions
        "q_header": "Data quality and limitations",
        "q_dup_ids": "Duplicate IDs",
        "q_dup_rows": "Duplicate rows",
        "q_neg": "Negative durations",
        "q_neg_help": "Operation ends before the alert is received: duration set to missing.",
        "q_coords": "Invalid coordinates",
        "q_coords_help": "Out of bounds or placeholder values (0, 0), -90 or -180: set to missing.",
        "q_period": "Period covered: {start} – {end}, {rows} operations. {bodies} body "
                    "discoveries, fatal by definition, are excluded from the share of fatal "
                    "operations.",
        "q_land": "**Imprecise coordinates.** {pct:.0f}% of located operations have a distance "
                  "from the coast of 0. According to the SECMAR documentation, this means an "
                  "operation very close to shore or inland (false alarm). On top of that, "
                  "approximate positions, probably due to data entry or to the position of the "
                  "alert rather than of the incident, put some points on land on the map. Analyses by place "
                  "and by distance from the coast should be read as orders of magnitude.",
        "q_missing": "Missing values by column",
        "q_missing_col": "Missing values (%)",
        "q_bias": "**Known biases.** The data only record alerts received by the CROSS, not all "
                  "incidents. There is no number of practitioners: no risk per activity can be "
                  "computed. Reporting practices may have changed since 1984. People-related "
                  "data are shown aggregated only.",
        "c_header": "Takeaways and next steps",
        "c_messages": "1. **Everyday work is not the tragedy**: breakdowns and false alarms keep "
                      "the CROSS busy but cause few deaths.\n"
                      "2. **Severity comes from individual accidents** (man overboard, swimming).\n"
                      "3. **Weather alone does not explain it**: wind barely separates fatal "
                      "operations from the others.",
        "c_next": "**Implications.** Focus summer prevention on the coastal strip and individual "
                  "accidents. These are leads suggested by the data, not causal evidence.\n\n"
                  "**Possible next steps.** Cross with attendance data to get a true risk rate; "
                  "add the file of deployed resources (SNSM lifeboats, helicopters).",
    },
}


def lang() -> str:
    """Return the current language code."""
    return st.session_state.get("lang", "fr")


def t(key: str, **kwargs):
    """Return the UI text for a key in the current language."""
    text = TEXTS[lang()][key]
    return text.format(**kwargs) if kwargs else text


def fmt_int(n: int) -> str:
    """Format an integer with the current language's thousands separator."""
    return f"{n:,}".replace(",", " " if lang() == "fr" else ",")
