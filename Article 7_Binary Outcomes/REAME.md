# Binary Outcomes, Risk Aversion, and Sorites Paradox (Part I)

### Article Overview

This repository contains the code used in the article **[Binary Outcomes, Risk Aversion, and Sorites Paradox (Part I)](https://www.infinite-variance.com/ideas/binary-outcomes-risk-aversion-sorites-paradox-part-one)**. The article delves into how increasing probabilities of success in a fixed number of trials can lead to negatively skewed distributions. It explores the paradoxical scenario where higher success rates may inadvertently increase risk aversion due to heightened sensitivity to potential losses.

### Code Summary

The code provided in this repository includes functions to plot the Probability Mass Function (PMF) of a binomial distribution for various numbers of trials and probabilities of success. These visualizations are crucial in illustrating the distribution's behavior as discussed in the article.

### Files

- **`plot_binomial_pmf.py`**: This script contains functions to generate and plot the PMF of a binomial distribution for given parameters.

### Usage

1. **Plotting a Single Binomial PMF**:
   ```python
   plot_binomial_pmf(n=10, p=0.50)
   ```
   This will generate a plot of the binomial distribution's PMF with 10 trials and a 50% probability of success.

2. **Plotting Multiple Binomial PMFs**:
   ```python
   plot_binomial_pmf(n=50, probabilities=[0.50, 0.90])
   ```
   This will generate plots of the PMF for 50 trials across different probabilities of success (50% and 90%).

### Dependencies

Ensure you have the following Python packages installed to run the code:

- `numpy`
- `matplotlib`
- `scipy`

You can install these dependencies via pip:

```bash
pip install numpy matplotlib scipy
```

### Visualization Examples

The code will generate bar charts that visualize the probability of achieving a certain number of successes in a binomial experiment, given the specified number of trials and success probabilities. These charts are central to understanding the discussed paradox in the article.

### License

This code is provided under the MIT License. Feel free to use, modify, and distribute it as needed.

---

Feel free to modify or expand upon this README as necessary!