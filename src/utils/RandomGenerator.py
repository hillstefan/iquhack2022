import random


class RandomGenerator:

    @staticmethod
    def generate_binary_random_value(self) -> int:
        return random.choice([0, 1])
