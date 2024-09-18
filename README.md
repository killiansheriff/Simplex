# Simplex 
![PyPI Version](https://img.shields.io/pypi/v/nsimplex.svg) ![PyPI Downloads](https://static.pepy.tech/badge/nsimplex)

A python package that implements the geometric object of a [simplex](https://en.wikipedia.org/wiki/Simplex).

## Usage 
Here is an example on how to get the mapping from barycentric coordinates (``concentrations``) to cartesian coordinates (``coords``) for a ``n_dim = 2`` for motifs with 12 atoms in their first coordination shell. ``generators`` return the unique set of concentration of the sorted possible concentrations, ``count`` is their multiplicities. This example can be found in the ``examples/`` folder. 

```python
import simplex as sp 

triangle = sp.Simplex(n_dim=2, edge_length=1, nneigh=12)
concentrations, coords = triangle.get_mapping()
generators, counts = triangle.get_generators(concentrations)
```

## Installation
For a standalone Python package or Conda environment, please use:
```bash
pip install --user nsimplex
```

If you want to install the lastest git commit, please replace ``nsimplex`` by ``git+https://github.com/killiansheriff/simplex.git``.

## Contact
If any questions, feel free to contact me (ksheriff at mit dot edu).

## References & Citing 
If you use this repository in your work, please cite:

```
@article{sheriffquantifying2024,
	title = {Quantifying chemical short-range order in metallic alloys},
	doi = {10.1073/pnas.2322962121},
	journaltitle = {Proceedings of the National Academy of Sciences},
	author = {Sheriff, Killian and Cao, Yifan and Smidt, Tess and Freitas, Rodrigo},
	date = {2024-06-18},
}
```

and 

```
@article{sheriff2024chemicalmotif,
  title = {Chemical-motif characterization of short-range order with E(3)-equivariant graph neural networks},
  DOI = {10.1038/s41524-024-01393-5},
  journal = {npj Computational Materials},
  author = {Sheriff,  Killian and Cao,  Yifan and Freitas,  Rodrigo},
  year = {2024},
  month = sep,
}
```
