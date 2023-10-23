from src.data.character import Character
from src.data.nodes.node import Node
from src.data.position2D import Position2D
from src.data.ports.out_port import OutPort
from src.data.ports.in_port import InPort
import json
import uuid


class CharacterText(Node):

    def __init__(self, character: Character, text: str, node_id: int):
        super().__init__(node_id)
        self.character = character
        self.text = self.fix_character_names(self.clean_problem_characters(text))
        self.out_port = OutPort(self, "Output")
        self.in_port = InPort(self, "Input")

    def convert_to_json(self, requested_pos: Position2D) -> str:
        data = {
            "characterCutoutTextExecutable":
                {
                    "character": self.character,  # gives object reference id, which should be same as actual character int value
                    "text": self.text,
                    "characterSprite": None,
                    "voiceClip": None,
                    "textBoxPos": "TOP",
                    "hideTextBoxOnEnd": False
                },
            "defaultValues": {},
            "position":
                {
                    "x": requested_pos.x,
                    "y": requested_pos.y
                },
            "guid": str(uuid.uuid4()),
            "$version": "A",
            "$type": "CharacterCutoutTextHandler",
            "$id": str(self.node_id)
        }
        return json.dumps(data)

    def get_node_width(self) -> int:
        return 300

    def get_node_height(self) -> int:
        return 200

    def connect_into_port(self, in_port: InPort):
        self.out_port.connect_into(in_port)

    def get_filled_out_ports(self) -> list:
        if self.out_port.in_port is not None:
            return [self.out_port]
        return []

    def get_in_port(self) -> InPort:
        return self.in_port
