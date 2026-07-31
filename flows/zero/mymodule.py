import random


def load_data(n: int = 1):
    return ["US", "CA", "BR", "CN"] * n


def scoring_function(ctx):
    return random.randint(0, 10), ctx.input


def join_step(inputs):
    return max(inputs, key=lambda x: x.score).country
