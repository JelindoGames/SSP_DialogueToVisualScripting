import abc
from abc import abstractmethod
from src.data.position2D import Position2D

class Node(abc.ABC):

    def __init__(self, node_id: int):
        self.node_id = node_id

    @abstractmethod
    def convert_to_json(self, latest_node_pos: Position2D):
        pass

    @abstractmethod
    def get_node_width(self):
        pass

    @abstractmethod
    def get_node_height(self):
        pass

    def clean_problem_characters(self, text: str):
        return text.replace('\'', '’')
