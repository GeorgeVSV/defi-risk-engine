import numpy as np
from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. model parameters -------------------------------------------------------
start_price = 1_500
liq_price   = 1_212
sigma       = 0.80           # annualised volatility
dt          = 1/365
num_paths   = 100_000        # raise to e.g. 1_000_000 for final run
horizons    = [3, 7, 14, 30, 60]

# --- 2. helper ---------------------------------------------------------------
def p_theoretical(s0, s_liq, sig, t_days):
    T = t_days / 365
    a = np.log(s0 / s_liq)
    return 2 * norm.cdf(-a / (sig * np.sqrt(T)))

def p_monte_carlo(s0, s_liq, sig, t_days, paths):
    liquidated = 0
    for _ in range(paths):
        price = s0
        for _ in range(t_days):
            price *= np.exp(sig * np.sqrt(dt) * np.random.normal())
            if price <= s_liq:
                liquidated += 1
                break
    return liquidated / paths

# --- 3. experiment ------------------------------------------------------------
records = []
for T in horizons:
    p_th = p_theoretical(start_price, liq_price, sigma, T)
    p_mc = p_monte_carlo(start_price, liq_price, sigma, T, num_paths)
    records.append({
        "days": T,
        "p_theoretical": p_th,
        "p_monte_carlo": p_mc,
        "abs_error": abs(p_th - p_mc)
    })

df = pd.DataFrame(records)
print(df)

# --- 4. visualisation ---------------------------------------------------------
plt.figure(figsize=(6,4))
plt.plot(df["days"], df["p_theoretical"], marker="o", label="Theory")
plt.plot(df["days"], df["p_monte_carlo"], marker="x", label="Monte-Carlo")
plt.xlabel("time horizon (days)")
plt.ylabel("liquidation probability")
plt.title("Reflection Principle vs. Monte-Carlo")
plt.legend()
plt.tight_layout()
plt.show()
