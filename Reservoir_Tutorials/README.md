# Hands-On Experiments: Memory capacity in reservoir computing models 

**Course:** Promises and Perils of Connectome-Constrained Neuro-AI Models 
**Semester:** OHBM 2026  

---

## Overview

This folder contains three Jupyter notebooks designed as hands-on practical sessions accompanying a course on reservoir computing and connectome-constrained recurrent neural networks. The experiments are built around the **Memory Capacity (MC) task**, a standard benchmark in the reservoir computing community that measures how well a recurrent network can reconstruct delayed versions of a past input signal.

---

## Notebooks

### `experiment_1_rc_random_mc.ipynb` — Reservoir Computing with Random Parameters
An Echo State Network (ESN) is evaluated on the MC task without any parameter tuning. Five independent trials are run and averaged. Diagnostic plots include signal reconstruction, reservoir neuron traces, input and output weight distributions, and the memory profile (r² per lag).

### `experiment_2_rc_tuned_mc.ipynb` — Reservoir Computing with Hyperparameter Tuning
A grid search is performed over spectral radius, sparsity, and input scaling. The best configuration is identified by mean test MC over multiple random seeds and visualised with the same diagnostic plots as Experiment 1.

### `experiment_3_rc_connectome_mc.ipynb` — Memory Capacity of Empirical Connectomes
In Experiments 1 and 2, we used randomly generated reservoir weight matrices. Here we ask: **what happens when the reservoir is an empirical brain connectome?**

We evaluate the Memory Capacity (MC) of four network variants derived from a chosen connectome:

1. **Structured** — the original empirical connectome as loaded
2. **Symmetrized structured** — $(W + W^T)/2$, eliminating all asymmetry
3. **Shuffled (null)** — degree-preserving rewired network via `bct.randmio_dir_connected`
4. **Symmetrized shuffled** — the same symmetrization applied to the null network
---

## Requirements

```
numpy
scipy
scikit-learn
matplotlib
echoes
```

All notebooks are designed to run on **Google Colab**. The `echoes` library is installed via `pip` at the top of Experiments 1 and 2. 

---

## Citation

If you use these materials or build upon them, please cite the following works:

> Damicelli, Fabrizio, Claus C. Hilgetag, and Alexandros Goulas. "Brain connectivity meets reservoir computing." PLoS Computational Biology 18.11 (2022): e1010639.

> Hadaeghi, Fatemeh, Kayson Fakhar, and Claus C. Hilgetag. "Controlling reciprocity in binary and weighted networks: A novel density-conserving approach." *Chaos: An Interdisciplinary Journal of Nonlinear Science* 36.2 (2026).

> Hadaeghi, Fatemeh, et al. "A computational perspective on the no-strong-loops principle in brain networks." *bioRxiv* (2025): 2025-09.

---

## License

These materials are shared for educational purposes. Please contact the author for permissions beyond personal and classroom use.
