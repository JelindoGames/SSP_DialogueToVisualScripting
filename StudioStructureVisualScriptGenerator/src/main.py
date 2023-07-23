from src.input_reading.text_interpreter import interpret_text_file
from src.input_reading.csv_interpreter import interpret_csv_file
import src.data.graph as graph_code

# Predefined
input_file = "../input/Wednesday - Slice of Life (Week 1).txt"

if __name__ == "__main__":
    input_is_csv = input_file.endswith(".csv")
    nodes = interpret_csv_file(input_file) if input_is_csv else interpret_text_file(input_file)
    graph_name = "TestGeneratedScriptMachineD"
    graph = graph_code.Graph(nodes, graph_name)
    with open(f"../output/{graph_name}.asset", 'w') as f:
        f.write(graph.convert_to_text())
