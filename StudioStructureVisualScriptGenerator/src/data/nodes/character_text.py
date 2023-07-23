from src.data.character import Character
from src.data.nodes.node import Node
from src.data.position2D import Position2D
import json
import uuid


class CharacterText(Node):

    def __init__(self, character: Character, text: str, node_id: int):
        super().__init__(node_id)
        self.character = character
        self.text = self.clean_problem_characters(text)

    def convert_to_json(self, requested_pos: Position2D):
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

    def get_node_width(self):
        return 300

    def get_node_height(self):
        return 200
