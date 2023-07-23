from src.data.nodes.node import Node
from src.data.position2D import Position2D
import json
import uuid


class NarrationText(Node):

    def __init__(self, text: str, node_id: int):
        super().__init__(node_id)
        self.text = self.clean_problem_characters(text)

    def convert_to_json(self, requested_pos: Position2D):
        # Create JSON
        data = {
            "narrationTextExecutable":
                {
                    "text": self.text,
                    "voiceClip": None
                },
            "defaultValues": {},
            "position":
                {
                    "x": requested_pos.x,
                    "y": requested_pos.y
                },
            "guid": str(uuid.uuid4()),
            "$version": "A",
            "$type": "NarrationHandler",
            "$id": str(self.node_id)
        }
        return json.dumps(data)

    def get_node_width(self):
        return 200

    def get_node_height(self):
        return 100

    def __str__(self):
        return self.text

