import abc
import typing
from hashlib import sha3_512

from utils.RandomGenerator import RandomGenerator


class Agent(abc.ABC):

    def __init__(self):
        self._private_key = None
        self._public_key = None

        self._gate_sequence: typing.List[int] = []
        self._bit_sequence: typing.List[int] = []
        self._result_sequence: typing.List[int] = []

    @property
    def public_key(self):
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        self._public_key = value

    def get_private_key_hash(self) -> str:
        return sha3_512(repr(self._private_key).encode('utf-8')).hexdigest()

    def generate_random_bit_sequence(self, length: int = 8):
        self._bit_sequence = [RandomGenerator.generate_binary_random_value() for _ in range(length)]

    def generate_random_gate_sequence(self, length: int = 8):
        self._gate_sequence = [RandomGenerator.generate_binary_random_value() for _ in range(length)]