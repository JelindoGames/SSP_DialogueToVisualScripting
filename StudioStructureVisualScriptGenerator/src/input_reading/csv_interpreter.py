from src.data.nodes.narration_text import NarrationText
from src.data.nodes.character_text import CharacterText
from src.data.nodes.prompt import Prompt
from src.data.character import Character
import pandas as pd


def interpret_csv_file(filepath: str):
    csv_data = pd.read_csv(filepath)
    nodes = []
    nodes_branched = []  # Same as nodes list but in a branched form
    node_id = 0
    in_branch = False
    for _, row in csv_data.iterrows():
        node_id += 1  # This may skip a few id numbers but that's okay
        if not in_branch and not pd.isnull(row[2]):
            in_branch = True
            branch_node = Prompt("...", [row[1], row[3]], node_id)
            nodes.append(branch_node)
            nodes_branched.append(branch_node)
            nodes_branched.append([[], []])
            continue
        if row[0] == "BRANCH END:":
            in_branch = False
            continue
        if in_branch:
            node1 = get_node_from_cells(row, node_id, 0, 1)
            if node1 is not None:
                nodes.append(node1)
                nodes_branched[-1][0].append(node1)
            node_id += 1
            node2 = get_node_from_cells(row, node_id, 2, 3)
            if node2 is not None:
                nodes.append(node2)
                nodes_branched[-1][1].append(node2)
        else:
            node = get_node_from_cells(row, node_id, 0, 1)
            if node is not None:
                nodes.append(node)
                nodes_branched.append(node)
    print(nodes_branched)
    forge_node_connections(nodes_branched)
    return nodes


def get_node_from_cells(row, node_id, speaker_idx, content_idx):
    row[speaker_idx] = "".join(row[speaker_idx].split())  # Remove whitespace
    row[speaker_idx] = row[speaker_idx].replace(":", "")  # Remove colon
    # Interpret Cells
    if row[speaker_idx] == "Narration":
        return NarrationText(row[content_idx], node_id)
    else:
        character = Character.string_to_character.get(row[speaker_idx])
        if character is None:
            return None
        if character == Character.MC:
            return NarrationText(row[content_idx], node_id)
        return CharacterText(character, row[content_idx], node_id)


def forge_node_connections(nodes_branched):
    for i in range(0, len(nodes_branched) - 1):
        if type(nodes_branched[i + 1]) == list:
            nodes_branched[i].connect_into_port(nodes_branched[i + 1][0][0].get_in_port())
            nodes_branched[i].connect_into_port(nodes_branched[i + 1][1][0].get_in_port())
            forge_node_connections(nodes_branched[i + 1][0])
            forge_node_connections(nodes_branched[i + 1][1])
        elif type(nodes_branched[i]) == list:
            nodes_branched[i][0][-1].connect_into_port(nodes_branched[i + 1].get_in_port())
            nodes_branched[i][1][-1].connect_into_port(nodes_branched[i + 1].get_in_port())
        else:
            nodes_branched[i].connect_into_port(nodes_branched[i + 1].get_in_port())
