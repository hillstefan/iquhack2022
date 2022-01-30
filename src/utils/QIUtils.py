class QIUtils:

    @staticmethod
    def _circuit_to_qobj(circuit):
        run_config_dict = {'shots': 25, 'memory': True}
        backend = QuantumInspireBackend(Mock(), Mock())
        qobj = assemble(circuit, backend, **run_config_dict)
        return qobj

    @staticmethod
    def _circuit_to_experiment(circuit):
        qobj = QIUtils._circuit_to_qobj(circuit)
        return qobj.experiments[0]
