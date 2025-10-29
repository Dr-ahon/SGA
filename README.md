# Evolutionary Algorithm (EA) Implementation

This project contains a simple implementation of a **binary Genetic Algorithm (GA)** written in Python.  
It was developed as a homework assignment for the course **Evolutionary Algorithms** at Charles University.

---

## 🧠 Overview

The algorithm evolves a population of binary individuals (`0`/`1` sequences) toward maximizing the sum of bits —  
a standard *OneMax* optimization problem.

### Implemented components
- **Population initialization**
- **Roulette wheel selection**
- **Tournament selection (optional)**
- **One-point crossover**
- **Bit-flip mutation**
- **Logging and convergence visualization**

---

## ⚙️ Parameters

| Parameter | Meaning | Default |
|------------|----------|----------|
| `POP_SIZE` | Population size | 100 |
| `IND_LEN` | Length of each individual | 25 |
| `CX_PROB` | Probability of crossover | 0.8 |
| `MUT_PROB` | Probability of mutation | 0.05 |
| `MUT_FLIP_PROB` | Probability of flipping each bit during mutation | 0.1 |

---

## 📈 Output

The script runs the algorithm 10 times and plots:
- Median of best fitness over generations
- 25–75% percentile interval (shown as a shaded area)

Example convergence plot:

