import pandas as pd
import numpy as np
from itertools import product

# Simulated DataFrame with ETH price delta column (replace with actual DataFrame)
# Example: df['delta'] contains open-close daily changes in USD
np.random.seed(42)
df = eth_historical_df.copy()
# Step 1: Bin the deltas into discrete buckets
bin_width = 50
bins = np.arange(-400, 401, bin_width)
df['binned'] = pd.cut(df['price_open_close_delta'], bins=bins, labels=(bins[:-1] + bin_width // 2))

# Step 2: Compute frequency and normalize to PMF
pmf = df['binned'].value_counts(normalize=True).sort_index()
price_deltas = pmf.index.astype(int).to_numpy()
probabilities = pmf.to_numpy()

# Step 3: Brute-force simulation setup
starting_price = 1500
liq_price = 1212
steps = 3  # keep small for brute-force

paths = list(product(price_deltas, repeat=steps))
liq_prob = 0
total_prob = 0

for path in paths:
    price = starting_price
    prob = 1.0
    for delta in path:
        price += delta
        prob *= probabilities[np.where(price_deltas == delta)[0][0]]
    total_prob += prob
    if price <= liq_price:
        liq_prob += prob

# Normalize
final_liquidation_probability = liq_prob / total_prob
print(final_liquidation_probability)
