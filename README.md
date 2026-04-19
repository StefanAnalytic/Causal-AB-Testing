🧪 Causal A/B-Testing Framework
Ein automatisiertes Sicherheitsnetz für verlässliche Produktentscheidungen.

🎯 Der Elevator Pitch (Warum dieses Projekt existiert)
Unternehmen treffen täglich teure Entscheidungen basierend auf A/B-Tests. Das Problem: Wenn die zugrundeliegenden Daten fehlerhaft sind, sind es auch die Entscheidungen. Oft laufen Tests zu kurz, Traffic wird falsch geroutet oder User landen versehentlich in mehreren Testgruppen.

Dieses Projekt ist eine automatisierte Pipeline (ein "Bodyguard"), die Rohdaten von A/B-Tests auf kritische Fehler prüft, bevor falsche Schlüsse gezogen werden. Das Ziel: Vermeidung von Fehlentscheidungen, die das Unternehmen Geld kosten.

💡 Der Business Value (Was das Tool leistet)
💰 Budget-Sicherheit (Pre-Analysis): Berechnet vorab mathematisch präzise, wie viele User ein Test braucht und wie viele Tage er laufen muss, um statistisch belastbar zu sein. (Vermeidet zu frühes Abbrechen).

🛡️ Schutz vor Bugs (SRM Kill-Switch): Erkennt sofort, wenn das Frontend den Traffic nicht richtig aufteilt (z.B. 80% Variante A, 20% Variante B statt 50/50) und stoppt die Analyse.

🧹 Datenreinheit (Spillover-Guard): Filtert automatisiert User heraus, die durch technische Fehler in beiden Testgruppen gelandet sind.

🛠️ Technische Umsetzung (Für Entwickler & Data Scientists)
Das Framework lässt sich nahtlos in bestehende Python-Pipelines integrieren und ist vollständig testgetrieben (TDD) entwickelt.

1. Pre-Analysis (Test-Planung)
Generiert automatisch PDF-Reports mit den benötigten Metriken (Minimum Detectable Effect, Sample Size, Testdauer) basierend auf historischem Traffic.

Bash
python src/power_analysis.py
2. Causal Guards (Daten-Bereinigung)
Eine Funktion, die am Anfang jedes Analyse-Notebooks steht und kaputte Daten abfängt:

Python
import pandas as pd
from src.causal_guards import assert_ab_integrity

df = pd.read_csv('ab_data.csv')
# Bricht bei fehlerhaftem Routing ab, bereinigt kontaminierte User
df_clean = assert_ab_integrity(df) 
3. Automatisierte Tests
Die Logik ist durch Pytest abgesichert. Die Tests simulieren defekte Datensätze, um sicherzustellen, dass die Guards im Ernstfall auslösen.

Bash
pytest tests/
⚙️ Tech Stack
Sprache: Python 3.8+

Data Science: Pandas, NumPy, SciPy, Statsmodels

Testing: Pytest

Causal Inference Vorbereitung: DoWhy
