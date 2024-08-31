# Gradient Ascent, Global Maximum, and Complexity

### Article Overview

This repository contains the code used in the article **[Gradient Ascent, Global Maximum, and Complexity](https://www.infinite-variance.com/ideas/games-gradient-ascent-and-complexity)**. The article explores the challenges of progressing from one level of achievement to another using the gradient ascent algorithm. By comparing simple and complex game scenarios, it highlights the difficulties in reaching higher levels of accomplishment.

### Code Summary

The code provided in this repository includes functions to:

- **Visualize 3D surfaces** for functions used in the analysis.
- **Run the gradient ascent algorithm** to identify the maximum points on these surfaces.
- **Simulate and analyze** the convergence behavior of the algorithm across multiple runs.
- **Generate histograms** to observe the distribution of vertical distances traveled during gradient ascent.

### Files

- **`Gradient Ascent, Global Maximum, and Complexity.py`**: This script includes all the functions for visualizing surfaces, running gradient ascent, and analyzing the algorithm's behavior.

### Usage

1. **Visualizing the Function Surface**:
   ```python
   # Define the range of x and y values
   x = np.linspace(-10, 10, 100)
   y = np.linspace(-10, 10, 100)
   x, y = np.meshgrid(x, y)

   # Define the function and plot
   z = np.sin(x/3) * np.cos(y/3)
   ax.plot_surface(x, y, z, cmap='viridis', alpha=0.9)
   ```

2. **Running the Gradient Ascent Algorithm**:
   ```python
   x_start = np.random.normal(0,1)
   y_start = np.random.normal(0,1)
   x_max, y_max = gradient_ascent(x_start, y_start, learning_rate=0.01, epochs=1000, grad=grad_f1)
   ```

3. **Analyzing Convergence**:
   ```python
   simulation_data = pd.DataFrame(columns=['z_start','z_max', 'z_diff'])
   for _ in range(1000):
       # Run gradient ascent for each simulation
       x_max, y_max = gradient_ascent(np.random.normal(0, 1), np.random.normal(0, 1), learning_rate=0.01, epochs=1000, grad=grad_f1)
       # Store the results
       simulation_data = pd.concat([simulation_data, pd.DataFrame([{'z_start': f1(x_start, y_start), 'z_max': f1(x_max, y_max), 'z_diff': f1(x_max, y_max) - f1(x_start, y_start)}])], ignore_index=True)
   ```

4. **Visualizing the Convergence with Histograms**:
   ```python
   data = (simulation_data["z_diff"] - simulation_data["z_diff"].min()) / (simulation_data["z_diff"].max() - simulation_data["z_diff"].min())
   ax.hist(data, bins=50, color='viridis')
   ```

### Dependencies

Ensure you have the following Python packages installed to run the code:

- `numpy`
- `matplotlib`
- `pandas`
- `sympy`
- `scipy`

You can install these dependencies via pip:

```bash
pip install numpy matplotlib pandas sympy scipy
```

### Visualization Examples

The code generates 3D plots of the surfaces for the functions under analysis, overlaid with points indicating the starting positions and maximum points found by the gradient ascent algorithm. Histograms are also generated to display the distribution of vertical distances traveled during the simulations.

### License

This code is provided under the MIT License. Feel free to use, modify, and distribute it as needed.

---

Feel free to customize this README further to better fit your needs!