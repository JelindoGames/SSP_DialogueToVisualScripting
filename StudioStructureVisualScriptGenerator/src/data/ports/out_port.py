import uuid
import json


class OutPort:

    def __init__(self, node, key: str):
        self.key = key
        self.node = node
        self.in_port = None

    def connect_into(self, in_port):
        if self.in_port is not None:
            raise Exception("Error: OutPort is already filled")
        self.in_port = in_port
        self.in_port.out_port = self

    def get_json_representation(self):
        json_dict = {
            "sourceUnit": {
                "$ref": str(self.node.node_id)
            },
            "sourceKey": self.key,
            "destinationUnit": {
                "$ref": str(self.in_port.node.node_id)
            },
            "destinationKey": self.in_port.key,
            "guid": str(uuid.uuid4()),
            "$type": "Unity.VisualScripting.ControlConnection"
        }
        return json.dumps(json_dict)
