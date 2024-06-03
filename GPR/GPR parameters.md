# Parameters
### Kernel Parameters:
1. length_scale: Dynamic, defined by s in the loop.
2. length_scale_bounds: Fixed at (1e-4, 1e5).
3. noise_level: Fixed at 1.
4. noise_level_bounds: Fixed at (1e-10, 1e1).
### GPR Model Parameters:
1. alpha: Dynamic, defined by a in the loop.
2. normalize_y: Dynamic, defined by n in the loop.
3. n_restarts_optimizer: (Commonly set to 10 but not explicitly shown in the provided code).
