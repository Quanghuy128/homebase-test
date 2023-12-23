import time

class NestedSetModel:
    def __init__(self):
        self.nodes = []
        self.left_counter = 1
        self.right_counter = 2

    def add_node(self, name, parent=None):
        node = {'name': name, 'left': self.left_counter, 'right': self.right_counter, 'children': []}
        self.left_counter += 2
        self.right_counter += 2

        if parent is None:
            self.nodes.append(node)
        else:
            parent_node = self.find_node(parent)
            if parent_node:
                parent_node['children'].append(node)

    def find_node(self, name, node_list=None):
        if node_list is None:
            node_list = self.nodes

        for node in node_list:
            if node['name'] == name:
                return node
            elif node['children']:
                found_node = self.find_node(name, node['children'])
                if found_node:
                    return found_node

    def retrieve_parent_child_relationships(self, node_list=None):
        if node_list is None:
            node_list = self.nodes

        relationships = []

        for node in node_list:
            for child in node['children']:
                relationships.append({'parent': node['name'], 'child': child['name']})
                relationships.extend(self.retrieve_parent_child_relationships(child['children']))

        return relationships

def measure_performance():
    nested_set_model = NestedSetModel()

    # Create a hierarchical structure
    nested_set_model.add_node('Root')
    nested_set_model.add_node('Child1', 'Root')
    nested_set_model.add_node('Child2', 'Root')
    nested_set_model.add_node('Grandchild1', 'Child1')
    nested_set_model.add_node('Grandchild2', 'Child1')
    nested_set_model.add_node('Grandchild3', 'Child2')

    # Measure performance for a larger dataset
    start_time = time.time()

    for i in range(1000):
        nested_set_model.add_node(f'Node{i}', 'Root')

    relationships = nested_set_model.retrieve_parent_child_relationships()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Elapsed Time for 1000 Nodes: {elapsed_time:.6f} seconds")
    print("Parent-Child Relationships:")
    for rel in relationships[:10]:  # Print the first 10 relationships for brevity
        print(rel)

if __name__ == "__main__":
    # Test the Nested Set Model
    nested_set_model = NestedSetModel()

    # Create a hierarchical structure
    nested_set_model.add_node('Root')
    nested_set_model.add_node('Child1', 'Root')
    nested_set_model.add_node('Child2', 'Root')
    nested_set_model.add_node('Grandchild1', 'Child1')
    nested_set_model.add_node('Grandchild2', 'Child1')
    nested_set_model.add_node('Grandchild3', 'Child2')

    # Retrieve and print parent-child relationships
    relationships = nested_set_model.retrieve_parent_child_relationships()
    print("Parent-Child Relationships:")
    for rel in relationships:
        print(rel)

    # Measure and print performance for a larger dataset
    measure_performance()
