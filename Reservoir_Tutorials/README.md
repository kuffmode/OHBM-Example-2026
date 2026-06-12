# Hands-On Experiments: Memory capacity in reservoir computing models

**Course:** Promises and Perils of Connectome-Constrained Neuro-AI Models  
**Semester:** OHBM 2026 

---

## Overview

This folder contains three Jupyter notebooks designed as hands-on practical sessions accompanying a course on connectome-constrained recurrent neural networks and reservoir computing models. A fully trained vanilla RNN (tanh activation, PyTorch) is evaluated on the memory capacity task introduced in the reservoir computing tutorial. 

Two training regimes are compared:
- **Part A — Full BPTT:** gradient flows through the entire training sequence; fair comparison to the ESN.
- **Part B — Chunked BPTT:** gradients are truncated at chunk boundaries; demonstrates the effect of truncation on memory capacity as a function of chunk size.

---

## Requirements

```
numpy
scipy
scikit-learn
matplotlib
torch
```

The notebook is designed to run on **Google Colab**. 

---

## Citation

If you use these materials or build upon them, please cite the following works:


> Hadaeghi, Fatemeh, Kayson Fakhar, and Claus C. Hilgetag. "Controlling reciprocity in binary and weighted networks: A novel density-conserving approach." *Chaos: An Interdisciplinary Journal of Nonlinear Science* 36.2 (2026).

> Hadaeghi, Fatemeh, et al. "A computational perspective on the no-strong-loops principle in brain networks." *bioRxiv* (2025): 2025-09.

---

## License

These materials are shared for educational purposes. Please contact the author (f.hadaeghi@uke.de) for permissions beyond personal and classroom use.
