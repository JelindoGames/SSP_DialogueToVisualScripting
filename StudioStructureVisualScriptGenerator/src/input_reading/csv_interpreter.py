from src.data.nodes.narration_text import NarrationText
from src.data.nodes.character_text import CharacterText
from src.data.character import Character
import pandas as pd


def interpret_csv_file(filepath: str):
    csv_data = pd.read_csv(filepath)
    nodes = []
    node_id = 1
    in_branch = False
    for _, row in csv_data.iterrows():
        if not in_branch and not pd.isnull(row[2]):
            in_branch = True
        if row[0] == "BRANCH END:":
            in_branch = False
            continue
        if in_branch:
            get_node_from_cells(row, node_id, nodes, 0, 1)
            get_node_from_cells(row, node_id, nodes, 2, 3)
        else:
            get_node_from_cells(row, node_id, nodes, 0, 1)
    return nodes


def get_node_from_cells(row, node_id, nodes, speaker_idx, content_idx):
    node = interpret_cells(row, node_id, speaker_idx, content_idx)
    if node is not None:
        nodes.append(node)
        node_id += 1


def interpret_cells(row, node_id, speaker_idx, content_idx):
    row[speaker_idx] = "".join(row[speaker_idx].split())  # Remove whitespace
    row[speaker_idx] = row[speaker_idx].replace(":", "")  # Remove colon
    # Interpret Cells
    if row[speaker_idx] == "Narration":
        return NarrationText(row[content_idx], node_id)
    else:
        character = Character.string_to_character.get(row[speaker_idx])
        if character is None:
            return None
        return CharacterText(character, row[content_idx], node_id)
