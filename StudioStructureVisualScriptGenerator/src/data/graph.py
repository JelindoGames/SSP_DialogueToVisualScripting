import json
import uuid

from src.data.character import Character
from src.data.position2D import Position2D
from src.data.nodes.node import Node


class Graph:

    def __init__(self, nodes, graph_name):
        self.nodes = nodes
        self.name = graph_name

    def convert_to_text(self):
        text = self.handle_boilerplate()
        return text

    def handle_boilerplate(self):
        text = ("%YAML 1.1\n"
                "%TAG !u! tag:unity3d.com,2011:\n"
                "--- !u!114 &11400000\n"
                "MonoBehaviour:\n"
                "  m_ObjectHideFlags: 0\n"
                "  m_CorrespondingSourceObject: {fileID: 0}\n"
                "  m_PrefabInstance: {fileID: 0}\n"
                "  m_PrefabAsset: {fileID: 0}\n"
                "  m_GameObject: {fileID: 0}\n"
                "  m_Enabled: 1\n"
                "  m_EditorHideFlags: 0\n"
                "  m_Script: {fileID: 11500000, guid: 95e66c6366d904e98bc83428217d4fd7, type: 3}\n"
                f"  m_Name: {self.name}\n"
                "  m_EditorClassIdentifier: \n"
                "  _data:\n"
                "    _json: '{\"graph\":{\"variables\":{\"Kind\":\"Flow\",\"collection\":{\"$content\":[],\"$version\":\"A\"},\"$version\":\"A\"},\"controlInputDefinitions\":[],\"controlOutputDefinitions\":[],\"valueInputDefinitions\":[],\"valueOutputDefinitions\":[],\"title\":null,\"summary\":null,\"pan\":{\"x\":0.0,\"y\":0.0},\"zoom\":1.0,\"elements\":"
                            f"[{self.get_nodes_in_json_form()},"
                            f"{self.get_unit_connections_json()}],"
                            "\"$version\":\"A\"}}'\n"
                "    _objectReferences:\n"
                f"{self.get_characters_as_object_references()}")
        return text

    def get_nodes_in_json_form(self):
        json = ""
        current_pos = Position2D()
        for node in self.nodes:
            json += node.convert_to_json(current_pos)
            json += ","
            current_pos.x += node.get_node_width()
        json = json[:-1]  # Remove last comma
        return json

    def get_characters_as_object_references(self):
        text = ""
        for i in range(Character.max_character_value):
            text += "    - {fileID: 11400000, guid: " + Character.character_to_guid[i] + ", type: 2}\n"
        return text

    def get_unit_connections_json(self):
        json = ""
        for i in range(1, len(self.nodes)):
            json += self.get_unit_connection_json(self.nodes[i - 1], self.nodes[i]) + ","
        json = json[:-1]
        return json

    def get_unit_connection_json(self, first: Node, second: Node):
        json_dict = {
            "sourceUnit": {
                "$ref": str(first.node_id)
            },
            "sourceKey": "Output",
            "destinationUnit": {
                "$ref": str(second.node_id)
            },
            "destinationKey": "Input",
            "guid": str(uuid.uuid4()),
            "$type": "Unity.VisualScripting.ControlConnection"
        }
        return json.dumps(json_dict)
