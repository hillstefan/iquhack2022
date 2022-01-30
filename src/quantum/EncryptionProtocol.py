from simulation.Agent import Agent


class EncryptionProtocol:

    @staticmethod
    def simple(agent_1: 'Agent', agent_2: 'Agent'):
        return {
            'backend': 'Spin-2',
            'circuit': 'simple_2q',
            'circuit_parameters': [
                agent_1.__getattribute__('_raw_key'),
                agent_1.__getattribute__('_sender_base'),
                agent_2.__getattribute__('_receiver_base')
            ]
        }

    @staticmethod
    def fancy(agent_1: 'Agent', agent_2: 'Agent'):
        return {
            'backend': 'Spin-2',
            'circuit': 'simple_2q',
            'circuit_parameters': [
                agent_1.__getattribute__('_raw_key'),
                agent_1.__getattribute__('_sender_base'),
                agent_1.__getattribute__('_receiver_base'),
                agent_2.__getattribute__('_raw_key'),
                agent_2.__getattribute__('_sender_base'),
                agent_2.__getattribute__('_receiver_base')
            ]
        }
