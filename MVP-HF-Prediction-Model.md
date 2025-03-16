#MVP HF Calculation model for crypto lending

This Basic Health Factor(HF) Calculation model predicts possible HF sometime $\Delta t$ in the future.

HF can be found using this formula:

$$HF = {Collateral Value*Liquidation Threshold \over Loan Value}.$$

In MVP we will be considering a stablecoin, e.g., USDC, as a loan currency. So we can take its exchange rate as a constant relative to time.
We chose Aave as a protocol.

In Aave loan amount increases with time because of interest rate.

So the loan value from time of $\Delta t$ from now is, assuming that loan currency exchange rate is constant:

$$Loan Value = (1 + n)^{\Delta t \over \tau} * Current Loan Amount * Loan Currency Exchange Rate = (1 + n)^{\Delta t \over \tau} * Loan Value $$

n is interest rate.
$\tau$ is the interest rate period, e.g., a year for anuall interest rate.

So let's predict collateral value at time $\Delta t$ from now on:

$$Collateral Value = Collateral Amount * Predicted Collateral Exchange Rate (t_{0} + \Delta t)$$

where $t_{0}$ is the current moment of time.

After we put it all together, we get:

$$HF(\Delta t, t_{0}) = {Collateral Amount * Predicted Collateral Exchange Rate (t_{0} + \Delta t) * Liquidation Threshold \over (1 + n)^{\Delta t \over \tau} * Loan Value}.$$

For our exchange rate prediction function we will take the simplest approach.
We will assume the exchange rate will continue to follow curent trade linearly.
So we can find the simplest price prediction function:

$$Predicted Collateral Exchange Rate (t_{0} + \Delta t) = k*\Delta t + Collateral Exchange Rate (t_{0})$$

k is the trend's slope.
$Collateral Exchange Rate (t_{0})$ is the exchange rate at this moment.

So we can put this together again:

$$HF(\Delta t, t_{0}) = {Collateral Amount * (k*\Delta t + Collateral Exchange Rate (t_{0})) * Liquidation Threshold \over (1 + n)^{\Delta t \over \tau} * Loan Value}.$$

This is a very rough approximation, but it is suitable for a MVP(Minimal Value Product). All the terms in the HF equations are known at the current moment.