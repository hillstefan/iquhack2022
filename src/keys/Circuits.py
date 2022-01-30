from numpy import pi
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit


class Circuits:

    @staticmethod
    def key_generation_circuit(control_bit_agent_1: int, control_bit_agent_2):
        qreg_q = QuantumRegister(2, 'q')
        creg_c = ClassicalRegister(2, 'c')
        circuit = QuantumCircuit(qreg_q, creg_c)

        circuit.rx(control_bit_agent_1 * pi, qreg_q[0])
        circuit.rx(control_bit_agent_2 * pi, qreg_q[1])
        circuit.h(qreg_q[0])
        circuit.h(qreg_q[1])
        circuit.cx(qreg_q[0], qreg_q[1])
        circuit.h(qreg_q[0])
        circuit.h(qreg_q[1])
        circuit.measure(qreg_q[0], creg_c[0])
        circuit.measure(qreg_q[1], creg_c[1])
