import pandas as pd
import scipy.stats as stats

def assert_ab_integrity(df, user_col='user_id', variant_col='group'):
    print("🛡️ Starte Causal Guards: Prüfe auf Kontamination und SRM...")
    
    # Fault 2: Spillover Check - User in beiden Gruppen?
    cross_pollinated = df.groupby(user_col)[variant_col].nunique()
    invalid_users = cross_pollinated[cross_pollinated > 1].index
    
    if len(invalid_users) > 0:
        print(f"⚠️ WARNUNG: {len(invalid_users)} User kontaminiert. Werden gedroppt.")
        df = df[~df[user_col].isin(invalid_users)]
    else:
        print("✅ Kein Spillover erkannt. User sind sauber getrennt.")
        
    # Fault 1: Sample Ratio Mismatch (SRM) Chi-Square Test
    counts = df[variant_col].value_counts()
    expected = [len(df)/2, len(df)/2] # Annahme 50/50 Split
    chi2, p_value = stats.chisquare(counts, f_exp=expected)
    
    if p_value < 0.001:
        raise ValueError(f"🚨 SRM DETECTED! P-Value: {p_value:.4f}. Routing-Logik im Frontend prüfen!")
    else:
        print(f"✅ Kein SRM erkannt (p-value: {p_value:.4f}). 50/50 Split ist valide.")
        
    return df