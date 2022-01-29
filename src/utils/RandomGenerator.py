import random


class RandomGenerator:

    @staticmethod
    def generate_binary_random_value() -> int:
        return random.choice([0, 1])
