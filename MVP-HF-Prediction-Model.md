# MVP HF Calculation model for crypto lending

### Disclaimer: This is a very rough approximation, but it is suitable for an MVP. All the terms in the HF equations are known at the current moment.

This Basic Health Factor(HF) Calculation model predicts possible HF sometime $\Delta t$ in the future.

HF can be found using this formula:

$$HF = {Collateral Value*Liquidation Threshold \over Loan Value}.$$


In our MVP(Minimal Value Product) we will be considering a stablecoin, e.g., USDC, as a loan currency, so we can take its exchange rate as a constant relative to time.
We chose Aave as our protocol.

In Aave loan amount increases with time because of interest rate.

So, the loan value from time of $\Delta t$ from now, assuming that loan currency exchange rate is constant, is:

$$Loan Value(t_{0} + \Delta t) = (1 + n)^{\Delta t \over \tau} * Loan Amount(t_{0}) * Loan Currency Exchange Rate = (1 + n)^{\Delta t \over \tau} * Loan Value(t_{0}).$$

where $n$ is interest rate, $t_{0}$ is the current moment of time and $\tau$ is the interest rate period, e.g., a year for annual interest rate.

So, let's predict collateral value at time $\Delta t$ from now on:

$$Collateral Value(t_{0} + \Delta t) = Collateral Amount * Predicted Collateral Exchange Rate (t_{0} + \Delta t).$$


After we put it all together, we get:

$$HF(\Delta t, t_{0}) = {Collateral Amount * Predicted Collateral Exchange Rate (t_{0} + \Delta t) * Liquidation Threshold \over (1 + n)^{\Delta t \over \tau} * Loan Value(t_{0})}.$$


For our exchange rate prediction function we will utilize the simplest approach.
We will assume that the exchange rate will continue to follow current trade linearly.

![Trendlinearapproximation](https://github.com/user-attachments/assets/f6f185b7-4420-4849-a34d-c58472d8ea8a)

So, we can find the simplest price prediction function:

$$Predicted Collateral Exchange Rate (t_{0} + \Delta t) = k*\Delta t + Collateral Exchange Rate (t_{0}).$$

where $k$ is the trend's slope.

So, we can put this together again:

$$HF(\Delta t, t_{0}) = {Collateral Amount * (k*\Delta t + Collateral Exchange Rate (t_{0})) * Liquidation Threshold \over (1 + n)^{\Delta t \over \tau} * Loan Value(t_{0})}.$$


### The accurancy of this method mostly depends on collateral exchange rate prediction, so this method can be drastically improved with a better exchange rate prediction function. Interest rates may also change, but this doesn't affect this method as much as the exchange rate prediction.
