from quantum.CircuitExecutor import CircuitExecutor
from quantum.ExecutionPipeline import ExecutionPipeline


class KeyInterface:

    def __init__(self, protocol_config):
        self._protocol_config = protocol_config

    def simulate_key_exchange(self, agent_1, agent_2):
        protocol = self._protocol_config(agent_1, agent_2)

        executor = CircuitExecutor(backend=protocol['backend'])
        pipeline = ExecutionPipeline(executor, protocol['circuit'])
        result = list(pipeline.apply_on(*protocol['circuit_parameters']))
