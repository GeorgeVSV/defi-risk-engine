from scipy.stats import norm
import numpy as np

### Theoretical Formula #########################################################
def reflection_liquidation_probability(start_price, liq_price, sigma, T_days):
    T = T_days / 365  # convert days to year fraction
    a = np.log(start_price / liq_price)
    return 2 * norm.cdf(-a / (sigma * np.sqrt(T)))

# Parameters
start_price = 1500
liq_price = 1212
sigma = 0.8  # annualized volatility
T_days = 7
dt = 1 / 365
num_paths = 100_000

# Theoretical result
p_theoretical = reflection_liquidation_probability(start_price, liq_price, sigma, T_days)
print(f"Theoretical probability (Reflection Principle): {p_theoretical:.4f}")

### Optimized Monte Carlo Simulation with Early Stopping #########################
liquidated_count = 0

for _ in range(num_paths):
    price = start_price
    for _ in range(T_days):
        Z = np.random.normal()
        price *= np.exp(sigma * np.sqrt(dt) * Z)
        if price <= liq_price:
            liquidated_count += 1
            break  # stop early if liquidation occurs

p_monte_carlo_fast = liquidated_count / num_paths
print(f"Monte Carlo estimated probability (early stopping): {p_monte_carlo_fast:.4f}")
