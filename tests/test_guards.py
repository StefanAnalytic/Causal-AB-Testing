import pandas as pd
import pytest
import sys
import os

# Damit Python unseren src-Ordner findet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.causal_guards import assert_ab_integrity

def test_spillover_guard():
    """Testet, ob User gelöscht werden, die in BEIDEN Gruppen auftauchen."""
    # Wir bauen künstliche (kaputte) Daten: User 'A' ist in Control UND Treatment
    data = {
        'user_id': ['A', 'B', 'C', 'D', 'A'], 
        'group': ['control', 'control', 'treatment', 'treatment', 'treatment']
    }
    df_dirty = pd.DataFrame(data)
    
    # Jagen sie durch unseren Bodyguard
    df_clean = assert_ab_integrity(df_dirty)
    
    # Assertions (Behauptungen): User A muss komplett verschwunden sein!
    assert 'A' not in df_clean['user_id'].values, "Fail: Kontaminierter User A wurde nicht gelöscht!"
    assert len(df_clean) == 3, "Fail: Es sollten nur noch 3 saubere User übrig sein."
    print("\n✅ Spillover-Test bestanden: Kontaminierte User werden gnadenlos gelöscht.")


def test_srm_guard():
    """Testet, ob der Kill-Switch auslöst, wenn der Traffic nicht 50/50 ist."""
    # Wir bauen Daten mit einem massiven Fehler: 800 Control vs. 200 Treatment
    data = {
        'user_id': range(1000),
        'group': ['control'] * 800 + ['treatment'] * 200
    }
    df_srm = pd.DataFrame(data)
    
    # Assertion: Die Funktion MUSS mit einem ValueError ("SRM DETECTED") abstürzen
    with pytest.raises(ValueError, match="SRM DETECTED"):
        assert_ab_integrity(df_srm)
        
    print("\n✅ SRM-Test bestanden: Kill-Switch löst bei kaputtem Traffic-Routing erfolgreich aus!")

if __name__ == "__main__":
    test_spillover_guard()
    test_srm_guard()