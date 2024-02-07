import abc
from abc import abstractmethod
from src.data.position2D import Position2D
from src.data.ports.in_port import InPort
import src.data.character as CharacterUtils
from src.data.character import Character


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

    def fix_character_names(self, line: str):
        final_list = []
        for word in line.split(" "):
            # For rejoining at end
            ownership = word.endswith("'s") or word.endswith("’s")
            if ownership:
                word = word[:-2]
            # For rejoining at end
            prefix = ""
            for char in word:
                if not char.isalnum():
                    prefix += char
                else:
                    break
            suffix = ""
            for i in range(len(word) - 1, -1, -1):
                if not word[i].isalnum():
                    suffix += word[i]
                else:
                    break
            # Only include alpha characters to ensure character is found
            word_stripped = "".join([char for char in word if char.isalpha()])
            # Actually find the character
            character = None if word_stripped.islower() else CharacterUtils.get_character_from_string(word_stripped)
            # Rebuild this part of the final string
            if character is None:
                if ownership:
                    word += "’s"
                final_list.append(word)
            else:
                final_word = prefix + Character.character_to_real_name[character] + suffix
                if ownership:
                    final_word += "’s"
                final_list.append(final_word)
        return " ".join(final_list)
