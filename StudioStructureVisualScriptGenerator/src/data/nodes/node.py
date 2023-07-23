import abc
from abc import abstractmethod
from src.data.position2D import Position2D
from src.data.ports.in_port import InPort


class Node(abc.ABC):

    def __init__(self, node_id: int):
        self.node_id = node_id

    @abstractmethod
    def convert_to_json(self, latest_node_pos: Position2D) -> str:
        pass

    @abstractmethod
    def get_node_width(self) -> int:
        pass

    @abstractmethod
    def get_node_height(self) -> int:
        pass

    @abstractmethod
    def connect_into_port(self, in_port: InPort):
        pass

    @abstractmethod
    def get_filled_out_ports(self) -> list:
        pass

    @abstractmethod
    def get_in_port(self) -> InPort:
        pass

    def clean_problem_characters(self, text: str):
        return text.replace('\'', '’')
