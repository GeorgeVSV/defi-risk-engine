# MVP numerical HF prediction model

### Disclaimer: This model hasn't been checked in practice yet!
### Disclaimer: This model probably works mostly on short time spans.

This model utilizes finding derivatives through numerical methods. The derivatives can then be used in order to predict health factor of a crypto loan and possible liquidation times.

We can try to predict HF(health factor) and possible liquidation time by using basic numerical methods

First we find  the derivative of HF at current moment $t_0$:

$${dHF \over dt} = \lim_{\Delta t \to 0}{HF(t_0 + \Delta t) - {HF(t_0)} \over \Delta t}.$$

Since we are approximating we can use can use a small $\Delta t$ that is noticeably more than zero.
This can also smoothen out the random movements of the HF.
And since we do not know $HF(t_0 + \Delta t)$ we can do this:

$$HF(t_0 + \Delta t) - HF(t_0) \approx HF(t_0) - HF(t_0 - \Delta t).$$

where $HF(t_0 - \Delta t)$ is just historical data and  $HF(t_0)$ is current HF.

So let's find the derivative:

$${dHF \over dt} = \lim_{\Delta t \to 0}{HF(t_0 + \Delta t) - {HF(t_0)} \over \Delta t} \approx {{HF(t_0) - HF(t_0 - \Delta t)} \over \Delta t}.$$

Now we can try to predict the future HF linearly.
So we approximate the change speed(derivative) of HF using our methods.
Now suppose we want to approximate HF at time $\Delta \tau$ from now on:

$$HF(t_0 + \Delta \tau) \approx HF(t_0) + {dHF \over dt}*\Delta \tau \approx HF(t_0) + {{HF(t_0) - HF(t_0 - \Delta t)} \over \Delta t} * \Delta \tau.$$

This also makes finding liquidation times easy.
Liquidation happens when HF reaches one, So we assume $HF(t_0 + \Delta \tau) = 1$ and solve the equation:

$$\Delta \tau = {{\Delta t * (1 - HF(t_0))} \over {HF(t_0) - HF(t_0 - \Delta t)}}.$$

In this case $\Delta \tau$ is time until liquidation.

### It's important to point out again that this will probably only work for small $\Delta \tau$ since the derivative of HF can quickly change.
