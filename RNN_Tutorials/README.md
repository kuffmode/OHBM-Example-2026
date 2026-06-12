# Hands-On Experiments: Memory capacity in vanilla RNNs compared to reservoir computing

**Course:** Promises and Perils of Connectome-Constrained Neuro-AI Models  
**Semester:** OHBM 2026 

## Overview

This folder contains one Jupyter notebook designed as hands-on practical sessions accompanying a course on recurrent neural networks. The experiments are built around the **Memory Capacity (MC) task**, a standard benchmark in the reservoir computing community that measures how well a recurrent network can reconstruct delayed versions of a past input signal.

---

### `MC_vanilla_rnn.ipynb` — Vanilla RNN trained with BPTT (PyTorch)
A fully trained vanilla RNN (tanh activation, PyTorch) is evaluated on the same task. Two training regimes are compared:
- **Part A — Full BPTT:** gradient flows through the entire training sequence; fair comparison to the ESN.
- **Part B — Chunked BPTT:** gradients are truncated at chunk boundaries; demonstrates the effect of truncation on memory capacity as a function of chunk size.

---

## Requirements

```
numpy
scipy
scikit-learn
matplotlib
echoes
torch
```

All notebooks are designed to run on **Google Colab**. PyTorch is pre-installed on Colab.

---

## Citation

If you use these materials or build upon them, please cite the following works:

> Hadaeghi, Fatemeh, Kayson Fakhar, and Claus C. Hilgetag. "Controlling reciprocity in binary and weighted networks: A novel density-conserving approach." *Chaos: An Interdisciplinary Journal of Nonlinear Science* 36.2 (2026).

> Hadaeghi, Fatemeh, et al. "A computational perspective on the no-strong-loops principle in brain networks." *bioRxiv* (2025): 2025-09.

---

## License

These materials are shared for educational purposes. Please contact the author for permissions beyond personal and classroom use.
