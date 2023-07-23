from src.data.ports.out_port import OutPort


class InPort:

    def __init__(self, node, key: str):
        self.key = key
        self.node = node
        self.out_port = None
