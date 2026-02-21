import numpy as np
import statsmodels.stats.api as sms
import math
import matplotlib.pyplot as plt
import os

print("📊 Starte Power-Analyse (Pre-Analysis Plan)...")

baseline_conversion = 0.119  
uplift_relative = 0.015      
alpha = 0.05                 
power = 0.80                 

treatment_conversion = baseline_conversion * (1 + uplift_relative)
effect_size = sms.proportion_effectsize(baseline_conversion, treatment_conversion)

# ... [Restlicher Code davor bleibt gleich]
sample_size = sms.NormalIndPower().solve_power(effect_size, power=power, alpha=alpha, ratio=1.0)
sample_size = math.ceil(sample_size)
total_sample = sample_size * 2
traffic_per_day = 75000  # <--- HIER AUF 75000 ÄNDERN!
days_required = math.ceil(total_sample / traffic_per_day)
# ... [Restlicher Code danach bleibt gleich]

plan_text = f"""
PRE-ANALYSIS PLAN (CAUSAL INFERENCE)
=========================================
Minimum Detectable Effect (MDE): {uplift_relative*100:.1f}%
Signifikanzniveau (Alpha):       {alpha}
Statistische Power:              {power}
-----------------------------------------
Benötigte Sample Size pro Gruppe:{sample_size:,}
Total Traffic benötigt:          {total_sample:,}
Testdauer (@{traffic_per_day:,} User/Tag): {days_required} Tage
=========================================
Fazit: Test kann innerhalb von 14 Tagen 
signifikant abgeschlossen werden.
"""

print(plan_text)

# Ordner 'reports' erstellen, falls er nicht existiert
os.makedirs('reports', exist_ok=True)

# Als PDF speichern (Das Deliverable)
fig = plt.figure(figsize=(8, 4))
plt.text(0.05, 0.5, plan_text, family='monospace', fontsize=12, va='center')
plt.axis('off')
plt.savefig('reports/pre_analysis_plan.pdf', bbox_inches='tight')
print("💾 PDF erfolgreich generiert: reports/pre_analysis_plan.pdf")