# Local Resolving Neighborhoods of Consecutive Circulant Graphs

A small, dependency-free Python module for computing distances, edges, and
local resolving neighborhoods `L(i,j)` in the consecutive circulant graph
`C_n(1,2,...,t)`.

The goal is simple: **test conjectures on small graphs before committing to
a proof.** This is meant as a complement to paper-and-pencil pattern-seeking,
not a replacement for it.

## Why this exists

Most conjectures about resolving sets in circulant graphs are tested by hand
on a handful of small cases before a proof is attempted. That works, but
hand-computation is slow and error-prone past `n ≈ 10`, and it is easy to
mistake a small-`n` artifact for a general pattern.

This module lets you check a conjecture on many `(t, n)` pairs in seconds.
It cannot prove anything — but it can save weeks by killing a false
conjecture before you invest in proving it.

## Requirements

- Python 3.8 or later
- **No external packages** — standard library only (`math`)

## Quick start

```python
from circulant import circ_dist, circ_edge_test, circ_luv_one, circ_luv_all

# Distance between two vertices in C_11(1,2,3)
circ_dist(3, 11, 1, 6)          # -> 2

# Is 1-8 an edge in C_12(1,2,3)?
circ_edge_test(3, 12, 1, 8)     # -> True

# Local resolving neighborhood of the edge (0,2) in C_11(1,2,3)
L, size = circ_luv_one(3, 11, 0, 2)

# Print L(i,j) for every edge of C_7(1,2)
circ_luv_all(2, 7)

```

## Notes and Limitations
+ The distance formula is exact for consecutive circulants `C_n(1,2,...,t)`.
For general connection sets, no closed form is used — see the general
version of this workflow.
+ The module computes `L(i,j)` for edges only when called via
`circ_luv_all`. The underlying function `circ_luv_one` works for any
pair `(i,j)`.
+ Computation is `O(n²)` per call to `circ_luv_one`, and `O(n³)` for
`circ_luv_all` on a graph with n vertices. Fine for small `n`;
not intended for large-scale enumeration.


## References 
The distance formula and edge test follow:
+ T. BC, S. Dueck, The metric dimension of circulant graphs,
Opuscula Math. 45 (2025) 1, 39–51.
+ A. Borchert, S. Gosselin, The metric dimension of circulant graphs
and Cayley hypergraphs, Util. Math. 106 (2018), 125–147.

The enumeration of local resolving neighborhoods follows:
+ I. Javaid, H. Benish, M. Murtaza, The fractional local metric
dimension of graphs, Contrib. Discrete Math. 19 (2024), no. 3, 163–177.


## Citing
If you use this in your own work, I'd love to hear about it.

Vidal, C.N. (2026). Local Resolving Neighborhoods of Consecutive Circulant Graphs (v1.0). Zenodo.

## License
MIT --- see License.

## Contact
Cristover N. Vidal

cristovervidal@gmail.com

cirstover.vidal@dnsc.edu.ph