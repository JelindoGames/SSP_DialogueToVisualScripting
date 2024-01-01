from src.data.nodes.narration_text import NarrationText
from src.data.nodes.character_text import CharacterText
from src.data.nodes.prompt import Prompt
from src.data.character import Character
import src.data.character as CharacterUtils
import pandas as pd
import numpy as np


def interpret_csv_file(filepath: str):
    csv_data = pd.read_csv(filepath)
    csv_data = csv_data.replace('', np.nan)
    nodes = []
    nodes_branched = []  # Same as nodes list but in a branched form
    node_id = 0
    in_branch = False
    for idx, row in csv_data.iterrows():
        print(f"CSV INTERPRETER: Handling Row {idx}")
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
    if pd.isna(row[speaker_idx]) or pd.isna(row[content_idx]):
        return None
    speaker_str = row[speaker_idx]
    stripped_speaker_str = "".join(speaker_str.split()).replace(":", "") # Remove whitespace and colon
    # Interpret Cells
    if stripped_speaker_str == "Narration":
        print(f"CSV INTERPRETER: Created Narration Node (speaker string: '{speaker_str}')")
        return NarrationText(row[content_idx], node_id)
    else:
        character = CharacterUtils.get_character_from_string(speaker_str)  # Don't use stripped version, spaces matter
        if character is None:
            print(f"WARNING -- CSV INTERPRETER: Failed to find speaker character from string '{speaker_str}', SKIP")
            return None
        if character == Character.MC:
            print(f"CSV INTERPRETER: Created Narration Node (speaker string: '{speaker_str}')")
            return NarrationText(row[content_idx], node_id)
        print(f"CSV INTERPRETER: Created Character Dialogue Node (speaker string: '{speaker_str}')")
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
