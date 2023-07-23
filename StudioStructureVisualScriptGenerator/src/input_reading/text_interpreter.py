from src.data.nodes.narration_text import NarrationText
from src.data.nodes.character_text import CharacterText
from src.data.character import Character


def interpret_text_file(filepath: str):
    nodes = []
    node_id = 1
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('['):
                narration_text = NarrationText(line, node_id)
                nodes.append(narration_text)
            elif len("".join(line.split())) > 0:  # The line has non-whitespace content
                nodes.append(get_character_text_node(line, node_id))
            node_id += 1  # Technically this means an empty line will skip an ID, this should be fine
    return nodes


def get_character_text_node(line, node_id):
    colon_pos = line.find(':')
    paren_pos = line.find('(')
    colon_first = colon_pos < paren_pos or paren_pos == -1
    char_str = line[:colon_pos] if colon_first else line[:paren_pos]
    char_str = "".join(char_str.split())  # Get rid of whitespace
    character = Character.string_to_character[char_str]
    return CharacterText(character, line[colon_pos + 2:], node_id)  # 2 to pass both colon and space

