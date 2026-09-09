import random

class GraphSparsifier:
    """Graph sparsification via edge sampling."""
    def sparsify(self, edges: list[tuple[int, int]], keep_prob: float = 0.5) -> dict:
        sampled = [e for e in edges if random.random() < keep_prob]
        return {
            "original_edges_count": len(edges),
            "sparsified_edges_count": len(sampled),
            "compression_ratio": round(len(sampled) / max(1, len(edges)), 4),
            "sparsified_edges": sampled
        }
