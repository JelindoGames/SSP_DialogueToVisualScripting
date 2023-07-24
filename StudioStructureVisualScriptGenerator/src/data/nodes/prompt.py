import json
import uuid

from src.data.nodes.node import Node
from src.data.position2D import Position2D
from src.data.ports.in_port import InPort
from src.data.ports.out_port import OutPort


class Prompt(Node):

    def __init__(self, prompt_text: str, response_list: list, node_id: int):
        super().__init__(node_id)
        self.prompt_text = prompt_text
        self.response_list = response_list
        self.in_port = InPort(self, "Input")
        self.out_ports = []
        self.num_ports_filled = 0
        for i in range(len(response_list)):
            self.out_ports.append(OutPort(self, f"Choice {i}"))

    def convert_to_json(self, latest_node_pos: Position2D) -> str:
        json_dict = {
            "promptExecutable": {
                "prompt": self.prompt_text,
                "voiceClip": None,
                "responses": self.response_list
            },
            "defaultValues": {},
            "position": {
                "x": latest_node_pos.x,
                "y": latest_node_pos.y
            },
            "guid": str(uuid.uuid4()),
            "$version": "A",
            "$type": "PromptHandler",
            "$id": str(self.node_id)
        }
        return json.dumps(json_dict)

    def get_node_width(self) -> int:
        return 300

    def get_node_height(self) -> int:
        return 150

    def connect_into_port(self, in_port: InPort):
        self.out_ports[self.num_ports_filled].connect_into(in_port)
        self.num_ports_filled += 1

    def get_filled_out_ports(self) -> list:
        filled = []
        for out_port in self.out_ports:
            if out_port.in_port is not None:
                filled.append(out_port)
        return filled

    def get_in_port(self) -> InPort:
        return self.in_port
