# Inter-Arrival Time, Clustering, and Patterns

This repository contains the Python code used to generate the charts and visualizations for the article **[Inter-arrival Time, Clustering, and Patterns](https://www.infinite-variance.com/ideas/inter-arrival-time-clustering-and-patterns)**. The article explores the human tendency to seek patterns amidst randomness, using concepts from probability theory, Poisson processes, and exponential distributions.

---

## Files in this Repository

- **`script.ipynb`**: The main Jupyter Notebook script containing the code for:
  - Visualizing the Poisson distribution's probability mass function (PMF).
  - Simulating and plotting exponential inter-arrival times.
  - Identifying and visualizing clusters of events in a simulated Poisson process.
  - Generating scatter plots with annotations for event clustering.

---

## Key Concepts and Features

1. **Poisson Distribution**:
   - Visualize the probability mass function (PMF) of a Poisson distribution.
   - Understand how random events occur at a constant average rate (\( \lambda \)).

2. **Exponential Distribution**:
   - Explore the distribution of inter-arrival times between consecutive events in a Poisson process.
   - Learn how memorylessness shapes our understanding of random processes.

3. **Clustering Analysis**:
   - Simulate a Poisson process and compute inter-arrival times.
   - Identify clusters based on thresholds for consecutive event timings.
   - Annotate visualizations to show how clusters emerge over time.

---

## Code Requirements

To run the script, you will need the following Python libraries:
- **NumPy**
- **Matplotlib**
- **SciPy**

You can install the dependencies using pip:

```bash
pip install numpy matplotlib scipy