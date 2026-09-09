from client import GraphSparsifier

def main():
    print("=== Graph Sparsifier Edge Sampling ===")
    sparsifier = GraphSparsifier()
    edges = [(i, i+1) for i in range(20)]
    res = sparsifier.sparsify(edges, keep_prob=0.5)
    print("Sparsification Result:", res)
    assert res["sparsified_edges_count"] < 20

    print("Graph Sparsifier verified successfully!")

if __name__ == "__main__":
    main()
