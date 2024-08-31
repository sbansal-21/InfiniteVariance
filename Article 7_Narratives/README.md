# Narratives, Chekhov’s Gun, and Agency

## Article Overview

**Article Name:** Narratives, Chekhov’s Gun, and Agency

**Description:**  
This article explores the nature of cinematic heroism and character transformation through the lens of mathematical concepts, particularly normal distributions and weighting functions. By modeling how characters' choices and paths evolve over time, the article provides a unique perspective on storytelling and character development.

**Article Link:**  
[Read the article here](https://www.infinite-variance.com/ideas/narratives-chekhovs-gun-and-agency)

## Code Overview

**Code File Name:** Narratives, Chekhov’s Gun, and Agency.ipynb

### Code Description

The provided code supports the article's exploration of character evolution in narratives by utilizing mathematical functions. It specifically uses normal distributions to represent character traits and decisions, and different types of weighting functions to simulate how these characteristics might shift over time. The code is organized into the following key sections:

1. **Normal Distributions Visualization:**
   - Generates and plots normal distributions with different means and variances to model character traits.
   - Highlights how these traits can be represented in a probabilistic framework.

2. **Converging Weights Function:**
   - Implements a function that models the convergence of a character's traits over time.
   - Demonstrates how certain characteristics may dominate as the story progresses.

3. **Random Weights Function:**
   - Uses a Dirichlet distribution to introduce randomness in the evolution of character traits.
   - This models scenarios where a character’s path is unpredictable, reflecting chaotic or non-linear narratives.

4. **Cyclical, Accelerative/Decelerative, and Linear Perception:**
   - Simulates how a character's perception or decision-making process can change over time using different weighting schemes.
   - Three models are used: Cyclical (periodic change), Accelerative/Decelerative (growth that slows or speeds up), and Linear (steady change).

### Visualizations

The code generates several visualizations to aid in understanding the evolution of character traits and decisions:

- **Probability Density Functions:** Shows how different normal distributions (representing traits) evolve.
- **Time-based Mixture Models:** Displays how the mixture of traits changes over time based on the chosen weighting function.
- **Weighting Function Plots:** Visualizes how different perception models affect the weight of a character's traits or decisions over time.

These visualizations are crucial for comprehending how mathematical models can be applied to narrative structures, offering insights into character development and story arcs.

## How to Use

1. **Clone or download the repository containing the `.ipynb` file.**
2. **Open the `Narratives, Chekhov’s Gun, and Agency.ipynb` file in Jupyter Notebook or any compatible environment.**
3. **Run the code cells sequentially to generate the plots and observe the behavior of the models.**
4. **Refer to the article for a detailed explanation of how these models relate to narrative theory.**

## Requirements

- **Python 3.x**
- **Jupyter Notebook**
- **Libraries:**  
  - `numpy`
  - `matplotlib`
  - `scipy`

To install the required libraries, you can use the following command:

```bash
pip install numpy matplotlib scipy
```

## Conclusion

The code complements the article by providing a mathematical framework to analyze and visualize the evolution of characters in narratives. By running this code, readers can gain a deeper understanding of how narrative elements like agency and transformation can be modeled and explored using mathematical functions.