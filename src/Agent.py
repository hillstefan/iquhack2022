class Agent:

    def __init__(self):
        self._private_key = None
        self._public_key = None

    @property
    def public_key(self):
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        self._public_key = value

    def send_message(self):
        pass

    def generate_key(self):
        pass
