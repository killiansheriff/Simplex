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
@article{sheriff2023quantifying,
  title={Quantifying chemical short-range order in metallic alloys},
  author={Sheriff, Killian and Cao, Yifan and Smidt, Tess and Freitas, Rodrigo},
  journal={arXiv},
  year={2023},
  doi={10.48550/arXiv.2311.01545}
}
```

and 

```
@article{sheriff2024chemicalmotif,
  title={Chemical-motif characterization of short-range order with E(3)-equivariant graph neural networks}, 
  author={Killian Sheriff and Yifan Cao and Rodrigo Freitas},
  journal={arXiv},
  year={2024},
  doi={10.48550/arXiv.2405.08628}
```
