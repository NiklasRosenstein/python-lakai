import textwrap

import lakai


def test_lakai() -> None:
    grammar = r"""
        %ignore /\s+/
        %import common.INT
        ?atom: INT
        ?product: atom | product "*" atom | product "/" atom
        ?sum: product | sum "+" product | sum "-" product
    """
    parser = lakai.from_string(grammar, start="sum")
    tree = parser.parse("1 + 3 * 2 + 4 / 2")
    lakai.pprint(tree, indent="    ")
    assert (
        lakai.pformat(tree, indent="    ").strip()
        == textwrap.dedent(
            """
    sum
        sum
            INT: '1'
            product
                INT: '3'
                INT: '2'
        product
            INT: '4'
            INT: '2'
    """
        ).strip()
    )
