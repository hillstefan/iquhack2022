from keys.CircuitExecutor import CircuitExecutor


class RandomGenerator:

    @staticmethod
    def generate_binary_random_value() -> int:
        qasm = f'''version 1.0

            qubits 2

            H q[0]

            Measure_z q[0]
            '''
        return CircuitExecutor().execute_qasm(qasm)[0]
