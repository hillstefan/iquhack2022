import abc
import typing
from hashlib import sha3_512

from utils.RandomGenerator import RandomGenerator


class Agent(abc.ABC):

    def __init__(self):
        self._private_key = None
        self._public_key = None

        self._sender_base: typing.List[int] = []
        self._receiver_base: typing.List[int] = []
        self._raw_key: typing.List[int] = []

    @property
    def public_key(self):
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        self._public_key = value

    def get_private_key_hash(self) -> str:
        return sha3_512(repr(self._private_key).encode('utf-8')).hexdigest()

    def generate_raw_key(self, length: int = 8):
        self._raw_key = [RandomGenerator.bit_value() for _ in range(length)]

    def generate_base(self, length: int = 8):
        self._sender_base = [RandomGenerator.bit_value() for _ in range(length)]
        self._receiver_base = [RandomGenerator.bit_value() for _ in range(length)]
