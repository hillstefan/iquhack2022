# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 01:11:05 2022

@author: Tobias Offermann
"""
import numpy as np

# Authentication
from getpass import getpass
from coreapi.auth import BasicAuthentication

from quantuminspire.credentials import save_account

save_account('c1fa8cbfd9b0f60668392b5fbf57d26ba4a59d95')

from quantuminspire.api import QuantumInspireAPI

qi = QuantumInspireAPI()

# Backend definieren: first qb, second qb, nr qbits
backend_starmon5 = [0, 2, 5]
backend_spin2 = [0, 1, 2]

backend = backend_spin2

qb1 = backend[0]
qb2 = backend[1]
nr_qb = backend[2]

nr_bits = 1


def random_number_generator(n_bits, n_qb, qb1):
    bitstring = np.zeros(nr_bits)

    qasm = '''version 1.0

    qubits {}

    H q[{}]

    Measure_z q[{}]
    '''.format(n_qb, qb1, qb1)

    for i in range(n_bits):
        # backend_type = qi.get_backend_type_by_name('QX single-node simulator')
        backend_type = qi.get_backend_type_by_name('Spin-2')
        result = qi.execute_qasm(qasm, backend_type=backend_type, number_of_shots=1)

        if result.get('histogram', {}):
            res_dict = result['histogram']
            res_list = list(res_dict.items())
            rand_nr = res_list[0][0]
        else:
            reason = result.get('raw_text', 'No reason in result structure.')
            print(f'Result structure does not contain proper histogram data. {reason}')

        bitstring[i] = rand_nr

    return bitstring


print(random_number_generator(nr_bits, nr_qb, qb1))
