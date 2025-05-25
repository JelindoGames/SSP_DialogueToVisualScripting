from src.input_reading.text_interpreter import interpret_text_file
from src.input_reading.csv_interpreter import interpret_csv_file
import src.data.graph as graph_code

# Predefined
input_file = "../input/sidestory/YonakaXDaniel/SideStory_YonakaXDaniel - Day 5 - Section 3.txt"
graph_name = "YxD - Day 5 - Section 3(New)"

diff_char_pov = True
diff_char_name = ["Yonaka", "Amber"]


if __name__ == "__main__":
    input_is_csv = input_file.endswith(".csv")
    nodes = interpret_csv_file(input_file, diff_char_pov, diff_char_name) if input_is_csv else interpret_text_file(input_file, diff_char_pov, diff_char_name)
    graph = graph_code.Graph(nodes, graph_name)
    with open(f"../output/sidestory/{graph_name}.asset", 'w') as f:
        f.write(graph.convert_to_text())
