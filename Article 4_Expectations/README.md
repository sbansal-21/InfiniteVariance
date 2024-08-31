# Expectations, Tails, and Poisson-Gamma

## Overview

This repository contains the Jupyter Notebook (`Expectations, Tails, and Poisson-Gamma.ipynb`) that accompanies the article **"[Expectations, Tails, and Poisson-Gamma](https://www.infinite-variance.com/ideas/updating-expectations-poisson-gamma-and-capturing-tails)."** The article explores the Poisson-Gamma model as a tool for updating assumptions in dynamic environments, highlighting the importance of balancing flexibility in variable settings with stability in predictable ones to enhance decision-making processes.

## Contents

- **Data Generation:** The notebook simulates synthetic data with extreme outcomes using Poisson-Gamma distributions. This is aimed at illustrating the model's capability to capture tail events and rare occurrences effectively.
  
- **Model Fitting:**
  - **Simple Poisson Model:** A basic Poisson model is fitted to the generated data, providing a baseline for comparison.
  - **Poisson-Gamma Model:** An updated model is then fitted, which accounts for the dynamic nature of the environment by integrating a gamma-distributed rate parameter, thereby offering a more flexible and robust approach.

- **Prediction and Comparison:**
  - The notebook predicts future defaults using both the simple Poisson and the Poisson-Gamma models.
  - It then compares the predicted defaults against actual data generated under extreme conditions, emphasizing how the Poisson-Gamma model better captures the variability and tail risks.

- **Application in Stable Environments:** The notebook also demonstrates the application of the Poisson-Gamma model in a stable environment, where the variance is low, to show how the model adapts to different conditions.

## Code Structure

The notebook is divided into the following key sections:

1. **Synthetic Data Generation:** 
   - Creates data using Gamma-distributed rates and Poisson-distributed defaults.
   - Visualizes the distribution of extreme outcomes.
   
2. **Simple Poisson Model Fitting:**
   - Fits a Poisson model to the generated data.
   - Predicts future outcomes using this model.

3. **Poisson-Gamma Model Fitting and Prediction:**
   - Updates the Gamma parameters based on observed data.
   - Predicts future outcomes using the updated Poisson-Gamma model.
   - Compares the results of the simple Poisson model with the Poisson-Gamma model.

4. **Comparison of Models in Stable Environments:**
   - Demonstrates how the Poisson-Gamma model performs in an environment with low variance.
   - Simulates future defaults and compares the results.

## Key Concepts

- **Poisson Distribution:** Often used to model the number of events happening within a fixed interval of time or space.
  
- **Gamma Distribution:** A continuous probability distribution used to model the time between events in a Poisson process.

- **Poisson-Gamma Model:** A Bayesian approach that combines the Poisson distribution with a gamma prior to create a more flexible model that can better account for variability and rare events.

## Usage

To use the notebook:

1. **Clone the repository** to your local machine:
   ```sh
   git clone https://github.com/yourusername/yourrepository.git
   ```

2. **Install the required Python libraries** if not already installed:
   ```sh
   pip install numpy matplotlib scipy
   ```

3. **Open the notebook** in Jupyter:
   ```sh
   jupyter notebook "Expectations, Tails, and Poisson-Gamma.ipynb"
   ```

4. **Run the cells** sequentially to reproduce the analysis and visualizations.

## Conclusion

This notebook serves as a practical guide to understanding and applying Poisson-Gamma models in environments with varying levels of uncertainty and stability. By following the steps outlined, you will gain insights into how these models can be used to improve decision-making processes in both stable and volatile conditions.

---

Feel free to modify the README to better fit your repository's specific needs!