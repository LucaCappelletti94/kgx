from __future__ import absolute_import

__version__ = '0.0.1'

from .pandas_transformer import PandasTransformer
from .nx_transformer import GraphMLTransformer
from .sparql_transformer import SparqlTransformer
from .rdf_transformer2 import ObanRdfTransformer
from .json_transformer import JsonTransformer
from .neo_transformer import NeoTransformer
from .logicterm_transformer import LogicTermTransformer
from .transformer import Transformer
from .filter import Filter, FilterLocation, FilterType

from .validator import Validator
from .prefix_manager import PrefixManager
from .mapper import map_graph

import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(filename)s][%(funcName)20s] %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
