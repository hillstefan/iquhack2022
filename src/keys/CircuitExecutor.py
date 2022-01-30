import typing

from quantuminspire.api import QuantumInspireAPI
from quantuminspire.credentials import save_account


class CircuitExecutor:

    def __init__(self):
        save_account('c1fa8cbfd9b0f60668392b5fbf57d26ba4a59d95')
        self._qi = QuantumInspireAPI()

    def execute_qiskit(self, circuit: 'QuantumCircuit') -> typing.List[int]:
        pass

    def execute_qasm(self, qasm: str, backend:str='Spin-2') -> typing.List[int]:
        backend_type = self._qi.get_backend_type_by_name(backend)
        result = self._qi.execute_qasm(qasm, backend_type=backend_type, number_of_shots=1)

        if result.get('histogram', {}):
            return [int(x) for x in result['histogram'].keys()]

        else:
            reason = result.get('raw_text', 'No reason in result structure.')
            print(f'Result structure does not contain proper histogram data. {reason}')
            return []
