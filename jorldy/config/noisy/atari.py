### Noisy DQN Atari Config ###

env = {
    # "name": it should be defined in the command. ex) python main.py --config config.AGENT.atari --env.name breakout
    "render": False,
    "gray_img": True,
    "img_width": 84,
    "img_height": 84,
    "stack_frame": 4,
    "no_op": False,
    "reward_clip": True,
    "dead_penalty": False,
}

agent = {
    "name": "noisy",
    "network": "noisy",
    "head": "cnn",
    "gamma": 0.99,
    "buffer_size": 1000000,
    "batch_size": 64,
    "start_train_step": 100000,
    "target_update_period": 10000,
    # noisy
    "noise_type": "factorized",  # [independent, factorized]
}

optim = {
    "name": "adam",
    "lr": 0.0001,
}

train = {
    "training": True,
    "load_path": None,
    "run_step": 30000000,
    "print_period": 10000,
    "save_period": 100000,
    "eval_iteration": 5,
    "record": True,
    "record_period": 300000,
    # distributed setting
    "update_period": 32,
    "num_workers": 16,
}
