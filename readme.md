# lakai

Lakai is a wrapper around [Lark][] that provides a convenient API.

  [Lark]: https://github.com/lark-parser/lark

## Installation

    $ pip install lakai

## Usage

```py
import lakai
grammar = r"""
    %ignore /\s+/
    %import common.INT
    ?atom: INT
    ?product: atom | product "*" atom | product "/" atom
    ?sum: product | sum "+" product | sum "-" product
"""
parser = lakai.from_string(grammar, start="sum")
tree = parser.parse("1 + 3 * 2 + 4 / 2")
lakai.pprint(tree)
# sum
#     sum
#         INT: '1'
#         product
#             INT: '3'
#             INT: '2'
#     product
#         INT: '4'
#         INT: '2'
```

To use Lakai with a Lark standalone parser:

```py
import lakai
from ._standalone import Lark_Standalone
parser = lakai.Lakai(Lark_Standalone())
```
