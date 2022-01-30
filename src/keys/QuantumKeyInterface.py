from keys.Agent import Agent

from keys.CircuitExecutor import CircuitExecutor


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
        self.agent_1.generate_random_bit_sequence(length=key_length)
        self.agent_1.generate_random_gate_sequence(length=key_length)

        self.agent_2.generate_random_bit_sequence(length=key_length)
        self.agent_2.generate_random_gate_sequence(length=key_length)

        for i in range(key_length):
            string = '''version 1.0
            qubits 1'''
            if m[i] == 1: string += "\nX q[0]"
            if b1[i] == 1: string += "\nH q[0]"
            if b2[i] == 1: string += "\nH q[0]"
            string += '''
            measure_all'''

        result = CircuitExecutor().execute_qasm(qasm_string, backend='Starmon-5')
