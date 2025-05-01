import numpy as np
from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime 

# --- 1. model parameters -------------------------------------------------------
start_price = 1_500
liq_price   = 1_212
sigma       = 0.80           # annualised volatility
dt          = 1/365
num_paths   = 100_000
horizons    = [3, 7, 14, 30, 60]

# --- 2. helper functions -------------------------------------------------------
def p_theoretical(s0, s_liq, sig, t_days):
    T = t_days / 365
    a = np.log(s0 / s_liq)
    return 2 * norm.cdf(-a / (sig * np.sqrt(T)))

def p_monte_carlo_gbm(s0, s_liq, sig, t_days, paths):
    liquidated = 0
    for _ in range(paths):
        price = s0
        for _ in range(t_days):
            price *= np.exp(sig * np.sqrt(dt) * np.random.normal())
            if price <= s_liq:
                liquidated += 1
                break
    return liquidated / paths

def p_monte_carlo_euler(s0, s_liq, sig, t_days, paths):
    liquidated = 0
    for _ in range(paths):
        price = s0
        for _ in range(t_days):
            price += price * sig * np.sqrt(dt) * np.random.normal()
            if price <= s_liq:
                liquidated += 1
                break
    return liquidated / paths

# --- 3. experiment ------------------------------------------------------------
experiment_start = datetime.now()
records = []

for T in horizons:
    p_th    = p_theoretical(start_price, liq_price, sigma, T)
    p_mc_gbm   = p_monte_carlo_gbm(start_price, liq_price, sigma, T, num_paths)
    p_mc_euler = p_monte_carlo_euler(start_price, liq_price, sigma, T, num_paths)

    records.append({
        "days": T,
        "p_theoretical": p_th,
        "p_monte_carlo_gbm": p_mc_gbm,
        "p_monte_carlo_euler": p_mc_euler,
        "error_gbm": abs(p_th - p_mc_gbm),
        "error_euler": abs(p_th - p_mc_euler)
    })

df = pd.DataFrame(records)
experiment_end = datetime.now()
duration = experiment_end - experiment_start
print(f"Monte Carlo simulation completed in {duration.seconds // 60} min {duration.seconds % 60} sec")
print(df)

# --- 4. visualisation ---------------------------------------------------------
plt.figure(figsize=(6,4))
plt.plot(df["days"], df["p_theoretical"], marker="o", label="Theory")
plt.plot(df["days"], df["p_monte_carlo_gbm"], marker="x", label="MC – GBM")
plt.plot(df["days"], df["p_monte_carlo_euler"], marker="^", label="MC – Euler")
plt.plot(df["days"], abs(df["p_monte_carlo_euler"] - df["p_theoretical"]), marker="s", linestyle="--", label="Euler – Theory Δ")
plt.plot(df["days"], abs(df["p_monte_carlo_gbm"] - df["p_theoretical"]), marker="s", linestyle="--", label="GBM – Theory Δ")
plt.xlabel("time horizon (days)")
plt.ylabel("liquidation probability")
plt.title("Theoretical vs. Monte Carlo (GBM, Euler, and Δ)")
plt.legend()
plt.tight_layout()
plt.show()

# --- 5. formatted output for whitepaper -----------------------------------------------
print("\nTheoretical (Reflection Principle):")
for _, row in df.iterrows():
    print(f" ({row['days']}, {round(row['p_theoretical'], 6)})")

print("\nMonte Carlo – GBM:")
for _, row in df.iterrows():
    print(f" ({row['days']}, {round(row['p_monte_carlo_gbm'], 6)})")

print("\nMonte Carlo – Euler:")
for _, row in df.iterrows():
    print(f" ({row['days']}, {round(row['p_monte_carlo_euler'], 6)})")

print("\nAbs. Difference (GBM – Theory):")
for _, row in df.iterrows():
    diff = abs(round(row['p_monte_carlo_gbm'] - row['p_theoretical'], 6))
    print(f" ({row['days']}, {diff})")

print("\nAbs. Difference (Euler – Theory):")
for _, row in df.iterrows():
    diff = abs(round(row['p_monte_carlo_euler'] - row['p_theoretical'], 6))
    print(f" ({row['days']}, {diff})")


