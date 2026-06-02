<div align="center">

# 🧪 Causal A/B-Testing Framework

[![Python](https://img.shields.io/badge/Language-Python_3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SciPy](https://img.shields.io/badge/Stats-SciPy_%7C_Statsmodels-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org/)
[![DoWhy](https://img.shields.io/badge/Causal-DoWhy-0194E2?style=for-the-badge)](#)
[![Pytest](https://img.shields.io/badge/Testing-Pytest_%7C_TDD-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/en/latest/)
[![Business Value](https://img.shields.io/badge/Focus-Decision_Safety-emerald?style=for-the-badge)](#)

**Ein automatisiertes Sicherheitsnetz und "Bodyguard" für datengetriebene Business-Entscheidungen.**

*Falsche Daten in A/B-Tests führen zu extrem teuren Fehlentscheidungen. Dieses System prüft Rohdaten vollautomatisch auf versteckte technische Anomalien, bevor das Management auf dieser Basis strategische Entscheidungen trifft.*

---
</div>

## 💼 Business Value & Executive Summary

Die meisten Standard-Tools berechnen am Ende eines Tests blind einen p-Wert, egal wie kaputt die zugrunde liegenden Daten sind. Dieses Framework agiert präventiv und defensiv:

<table>
  <tr>
    <td><strong>⏱️ Effizienz & Budget-Schutz</strong></td>
    <td>Berechnet vorab exakt, wie lange ein Test laufen muss (Power Analysis & Sample Size). Verhindert Geldverbrennung durch viel zu lange oder statistisch sinnlose Tests.</td>
  </tr>
  <tr>
    <td><strong>🚨 Sample Ratio Mismatch (SRM)</strong></td>
    <td>Erkennt sofort, wenn Website-Traffic durch Tracking-Bugs falsch verteilt wurde (z.B. 60/40 statt 50/50). Das System stoppt die Analyse automatisch, um fatale Trugschlüsse zu verhindern.</td>
  </tr>
  <tr>
    <td><strong>🛡️ Spillover-Guard (Daten-Reinheit)</strong></td>
    <td>Filtert vollautomatisch Nutzer heraus, die durch technische Fehler (z.B. Cookie-Resets oder Cross-Device-Nutzung) kontaminiert wurden und in mehreren Testgruppen gleichzeitig gelandet sind.</td>
  </tr>
</table>

---

## 🏗️ Architektur & Tech-Stack

Das System verbindet klassische frequentistische Statistik mit modernen Kausal-Modellen und strengem Software-Engineering:

| Komponente | Eingesetzte Technologie & Logik |
| :--- | :--- |
| **🧮 Data Science Core** | `Pandas`, `SciPy`, `Statsmodels` für die hochperformante Berechnung von Konfidenzintervallen, Varianzen und statistischer Signifikanz. |
| **🧠 Causal Inference** | `DoWhy` zur Modellierung kausaler Graphen. Stellt sicher, dass gemessene Effekte tatsächlich durch das Feature (Treatment) und nicht durch versteckte Störvariablen (Confounder) verursacht wurden. |
| **✅ Qualitätssicherung** | **Test-Driven Development (TDD)** via `Pytest`. Das Framework testet sich selbst und stellt sicher, dass die SRM- und Spillover-Guards auch bei Edge-Cases nicht brechen. |

---

## 🚀 Quick Start (Lokales Setup)

<details>
<summary><b>🛠️ Installation & Ausführung (Hier klicken zum Aufklappen)</b></summary>

### 1. Umgebung aufsetzen
```bash
# Virtuelles Environment erstellen und aktivieren
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.txt
