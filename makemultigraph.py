import pandas as pd
import networkx as nx
import itertools
from tqdm import tqdm  # Import tqdm for progress tracking

# Load the dataset
file_path = "personal_list_filtered.xlsx"
df = pd.read_excel(file_path, usecols=["gname", "country_txt", "weapsubtype1_txt", "target1"])

# Create an empty list for edges
edges = []

###Processing Country-Based Connections
print("\n Step 1: Processing by Country...")
grouped_country = df.groupby("country_txt")["gname"]
total_groups = len(grouped_country)

for i, (_, group) in enumerate(tqdm(grouped_country, total=total_groups, desc="Country Groups")):
    group = group.unique()
    if len(group) > 1:
        edges.extend([(a, b, "operates_in_same_country") for a, b in itertools.combinations(group, 2)])

print(f"Country-based edges added: {len(edges)}\n")

### Processing Weapon-Based Connections
print("\n Step 2: Processing by Weapon Type...")
valid_weapons = df[~df["weapsubtype1_txt"].isin(["Unknown", "Other", None, ""])]  # Filter out invalid values
grouped_weapon = valid_weapons.groupby("weapsubtype1_txt")["gname"]

weapon_edges = []
for _, group in tqdm(grouped_weapon, total=len(grouped_weapon), desc="Weapon Groups"):
    group = group.unique()
    if len(group) > 1:
        weapon_edges.extend([(a, b, "uses_similar_weapon") for a, b in itertools.combinations(group, 2)])

edges.extend(weapon_edges)
print(f"Weapon-based edges added: {len(weapon_edges)} (Total: {len(edges)})\n")

### 3️Processing Target-Based Connections
print("\n Step 3: Processing by Target Type...")
# valid_targets = df[df["target1"].notna()]  # Remove empty targets
grouped_target = df.groupby("target1")["gname"]

target_edges = []
for _, group in tqdm(grouped_target, total=len(grouped_target), desc="Target Groups"):
    group = group.unique()
    if len(group) > 1:
        target_edges.extend([(a, b, "targets_similar_entities") for a, b in itertools.combinations(group, 2)])

edges.extend(target_edges)
print(f"Target-based edges added: {len(target_edges)} (Total: {len(edges)})\n")

### Saving & Loading the Graph
print("\n Step 4: Saving and Loading into NetworkX...")

# Convert edges into DataFrame
edges_df = pd.DataFrame(edges, columns=["start_node", "end_node", "edge_type"])
edges_df.to_csv("gtd_multigraph_edges.csv", index=False)

# Load into a MultiGraph in NetworkX
G = nx.MultiGraph()
for _, row in tqdm(edges_df.iterrows(), total=len(edges_df), desc="Loading into Graph"):
    G.add_edge(row["start_node"], row["end_node"], edge_type=row["edge_type"])

print(f"\nGraph Loaded!")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

# Example: Get all edges for a specific node
example_node = "Black December"
if example_node in G:
    print(f" Edges for '{example_node}': {list(G.edges(example_node, data=True))}")
else:
    print(f"'{example_node}' not found in graph.")
