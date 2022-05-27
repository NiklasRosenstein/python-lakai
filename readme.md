# lakai

Lakai is a wrapper around [Lark][] that provides an easier to use API.

## Installation

    $ pip install lakai

## Usage

```py
import lakai
parser = lakai.from_resource(__name__, "grammar.lark")
tree = parser.parse("1 + 2 - 3")
lakai.pprint(tree)
```

To use Lakai with a Lark standalone parser:

```py
import lakai
from ._standalone import Lark_Standalone
parser = lakai.Lakai(Lark_Standalone())
```
