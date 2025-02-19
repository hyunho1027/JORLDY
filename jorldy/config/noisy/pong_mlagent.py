### Noisy DQN Pong_ML-Agents Config ###

env = {"name": "pong_mlagent", "train_mode": True}

agent = {
    "name": "noisy",
    "network": "noisy",
    "gamma": 0.99,
    "buffer_size": 50000,
    "batch_size": 32,
    "start_train_step": 25000,
    "target_update_period": 1000,
    # noisy
    "noise_type": "factorized",  # [independent, factorized]
}

optim = {
    "name": "adam",
    "lr": 2.5e-4,
}

train = {
    "training": True,
    "load_path": None,
    "run_step": 200000,
    "print_period": 5000,
    "save_period": 50000,
    "eval_iteration": 10,
    # distributed setting
    "update_period": 8,
    "num_workers": 16,
}
