import typing

from quantum.EncryptionProtocol import EncryptionProtocol
from simulation.Agent import Agent
from simulation.KeyInterface import KeyInterface


class Simulation:

    def __init__(self):
        self._agents: typing.Dict[str, 'Agent'] = {}

    def add_agent(self, name):
        self._agents[name] = Agent()

    def generate_keys(self, agent_1_name, agent_2_name, protocol_name: str = 'simple'):
        agent_1 = self._agents[agent_1_name]
        agent_2 = self._agents[agent_2_name]

        agent_1.generate_raw_key()
        agent_1.generate_base()
        agent_2.generate_raw_key()
        agent_2.generate_base()

        protocol_config = getattr(EncryptionProtocol, protocol_name)
        if callable(protocol_config):
            interface = KeyInterface(protocol_config)
            interface.simulate_key_exchange(agent_1, agent_2)

    def send_message(self, sender, receiver, message):
        pass
