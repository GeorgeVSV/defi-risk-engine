from scipy.stats import norm
import numpy as np

### Theoretical Formula #########################################################
def reflection_liquidation_probability(start_price, liq_price, sigma, T_days):
    T = T_days / 365  # convert days to year fraction
    a = np.log(start_price / liq_price)
    return 2 * norm.cdf(-a / (sigma * np.sqrt(T)))

# Example:
start_price = 1500
liq_price = 1212
sigma = 0.8  # annualized
T_days = 7

p_theoretical = reflection_liquidation_probability(start_price, liq_price, sigma, T_days)
print(f"Theoretical probability (Reflection Principle): {p_theoretical:.4f}")


### Monte-Carlo Simulation #########################################################
num_paths = 100_000
dt = 1/365
steps = T_days  # since 1 day = 1 step

# Simulate random walk
Z = np.random.normal(0, 1, size=(num_paths, steps))
price_paths = np.zeros_like(Z)
price_paths[:, 0] = start_price * np.exp(sigma * np.sqrt(dt) * Z[:, 0])

for t in range(1, steps):
    price_paths[:, t] = price_paths[:, t-1] * np.exp(sigma * np.sqrt(dt) * Z[:, t])

# Check for liquidation
liquidated = (price_paths <= liq_price).any(axis=1)
p_monte_carlo = liquidated.mean()

print(f"Monte Carlo estimated probability: {p_monte_carlo:.4f}")





