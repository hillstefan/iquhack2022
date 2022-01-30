from quantum.CircuitExecutor import CircuitExecutor
from simulation.Agent import Agent


class QuantumKeyInterface:

    def __init__(self):
        self._agent_1 = Agent()
        self._agent_2 = Agent()

    @property
    def agent_1(self):
        return self._agent_1

    @agent_1.setter
    def agent_1(self, value):
        self._agent_1 = value

    @property
    def agent_2(self):
        return self._agent_2

    @agent_2.setter
    def agent_2(self, value):
        self._agent_2 = value

    def generate_keys(self, key_length: int = 8):
        self.agent_1.generate_raw_key(length=key_length)
        self.agent_1.generate_base(length=key_length)

        self.agent_2.generate_raw_key(length=key_length)
        self.agent_2.generate_base(length=key_length)


        result = CircuitExecutor().execute_qasm(qasm_string, backend='Starmon-5')
