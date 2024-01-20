from src.data.nodes.narration_text import NarrationText
from src.data.nodes.character_text import CharacterText
import src.data.character as CharacterUtils
from src.data.character import Character


def interpret_text_file(filepath: str):
    nodes = []
    line_idx = 1
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(f"TXT INTERPRETER: Reading line {line_idx}")
            interpret_line(nodes, line, line_idx)
            line_idx += 1  # Technically this means an empty line will skip an ID, this should be fine
    forge_node_connections(nodes)
    return nodes


def interpret_line(nodes, line, node_id):
    line = line.strip()
    if line.startswith('['):
        print("TXT INTERPRETER: Making Narration Node (line is in square brackets)")
        narration_text = NarrationText(line, node_id)
        nodes.append(narration_text)
    elif len("".join(line.split())) > 0:  # The line has non-whitespace content
        node = get_character_text_node(line, node_id)
        if node is not None:
            nodes.append(node)


def get_character_text_node(line, node_id):
    colon_pos = line.find(':')
    paren_pos = line.find('(')
    colon_first = colon_pos < paren_pos or paren_pos == -1
    char_str = line[:colon_pos] if colon_first else line[:paren_pos]  # Get the character name (and nothing else)
    character = CharacterUtils.get_character_from_string(char_str)
    if character is None:
        print(f"WARNING -- TXT INTERPRETER: Failed to get character from string '{char_str}', SKIP")
        return None
    if character == Character.MC:
        print(f"TXT INTERPRETER: Making Narration Node (character string '{char_str}')")
        return NarrationText(line[colon_pos + 2:], node_id)
    print(f"TXT INTERPRETER: Making Character Dialogue Node (character string '{char_str}')")
    return CharacterText(character, line[colon_pos + 2:], node_id)  # 2 to pass both colon and space


def forge_node_connections(nodes):
    for i in range(0, len(nodes) - 1):
        nodes[i].connect_into_port(nodes[i + 1].get_in_port())
