import pygments
import pytest

from pygments.lexers import PythonLexer
from pygments.formatters import TerminalTrueColorFormatter
from pytest import param

from rosepine import RosePineStyle, RosePineMoonStyle, RosePineDawnStyle


def highlight_base(code: str) -> str:
    """Highlight code in true color (24-bit) with the RosePineStyle.

    Args:
        code (str): Piece of code to highlight.

    Returns:
        str: Highlighted string using style.
    """
    return pygments.highlight(
        code=code,
        lexer=PythonLexer(),
        formatter=TerminalTrueColorFormatter(style=RosePineStyle),
    )


def highlight_moon(code: str) -> str:
    """Highlight code in true color (24-bit) with the RosePineMoonStyle."""
    return pygments.highlight(
        code=code,
        lexer=PythonLexer(),
        formatter=TerminalTrueColorFormatter(style=RosePineMoonStyle),
    )


def highlight_dawn(code: str) -> str:
    """Highlight code in true color (24-bit) with the RosePineDawnStyle."""
    return pygments.highlight(
        code=code,
        lexer=PythonLexer(),
        formatter=TerminalTrueColorFormatter(style=RosePineDawnStyle),
    )


@pytest.mark.parametrize(
    "code,expected",
    [
        param(
            "# This is a comment",
            "\x1b[38;2;144;140;170m# This is a comment\x1b[39m\n",
            id="Comment",
        ),
        param(
            "err?",
            "\x1b[38;2;224;222;244merr\x1b[39m\x1b[38;2;235;111;146m?\x1b[39m\n",  # noqa: E501
            id="Error",
        ),
        param(
            "from rosepine import RosePineStyle",
            "\x1b[38;2;49;116;143mfrom\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mrosepine\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143mimport\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mRosePineStyle\x1b[39m\n",  # noqa: E501
            id="Keyword.Namespace",
        ),
        param(
            "None",
            "\x1b[38;2;235;188;186mNone\x1b[39m\n",
            id="Keyword.Constant",
        ),
        param(
            "int",
            "\x1b[38;2;224;222;244mint\x1b[39m\n",
            id="Keyword.Type",
        ),
        param(
            "try:\n    pass\nexcept:\n    raise",
            "\x1b[38;2;49;116;143mtry\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\n\x1b[38;2;224;222;244m    \x1b[39m\x1b[38;2;49;116;143mpass\x1b[39m\n\x1b[38;2;49;116;143mexcept\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\n\x1b[38;2;224;222;244m    \x1b[39m\x1b[38;2;49;116;143mraise\x1b[39m\n",  # noqa: E501
            id="Keyword",
        ),
        param(
            "def method(self, other): ...",
            "\x1b[38;2;49;116;143mdef\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;111;146mmethod\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;235;111;146mself\x1b[39m\x1b[38;2;144;140;170m,\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mother\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\n",  # noqa: E501
            id="Name.Builtin.Pseudo",
        ),
        param(
            "list(map(lambda n: n + 1, range(5)))",
            "\x1b[38;2;224;222;244mlist\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;224;222;244mmap\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;49;116;143mlambda\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mn\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mn\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m+\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;188;186m1\x1b[39m\x1b[38;2;144;140;170m,\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mrange\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;235;188;186m5\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\n",  # noqa: E501
            id="Name.Builtin",
        ),
        param(
            "class IsDismissed: ...",
            "\x1b[38;2;49;116;143mclass\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;156;207;216mIsDismissed\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\n",  # noqa: E501
            id="Name.Class",
        ),
        param(
            "@decorator\ndef function(): ...",
            "\x1b[38;2;196;167;231;01m@decorator\x1b[39;00m\n\x1b[38;2;49;116;143mdef\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;111;146mfunction\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\n",  # noqa: E501
            id="Name.Decorator",
        ),
        param(
            'raise KeyError("Wrong lock.")',
            '\x1b[38;2;49;116;143mraise\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;156;207;216mKeyError\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;246;193;119mWrong lock.\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\n',  # noqa: E501
            id="Name.Exception",
        ),
        param(
            "def foo(bar: int, baz: Optional[str] = None) -> None: ...",
            "\x1b[38;2;49;116;143mdef\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;111;146mfoo\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;224;222;244mbar\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mint\x1b[39m\x1b[38;2;144;140;170m,\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mbaz\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mOptional\x1b[39m\x1b[38;2;144;140;170m[\x1b[39m\x1b[38;2;224;222;244mstr\x1b[39m\x1b[38;2;144;140;170m]\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m=\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;188;186mNone\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m-\x1b[39m\x1b[38;2;49;116;143m>\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;188;186mNone\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\n",  # noqa: E501
            id="Name.Function",
        ),
        param(
            'class IsDismissed:\n    __slots__ = ("attr",)',
            '\x1b[38;2;49;116;143mclass\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;156;207;216mIsDismissed\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\n\x1b[38;2;224;222;244m    \x1b[39m\x1b[38;2;235;111;146m__slots__\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m=\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;246;193;119mattr\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;144;140;170m,\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\n',  # noqa: E501
            id="Name.Variable.Magic",
        ),
        param(
            "life = 42",
            "\x1b[38;2;224;222;244mlife\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m=\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;188;186m42\x1b[39m\n",  # noqa: E501
            id="Name",
        ),
        param(
            "0b1101001",
            "\x1b[38;2;235;188;186m0b1101001\x1b[39m\n",
            id="Number.Bin",
        ),
        param(
            "105.0",
            "\x1b[38;2;235;188;186m105.0\x1b[39m\n",
            id="Number.Float",
        ),
        param(
            "0x69",
            "\x1b[38;2;235;188;186m0x69\x1b[39m\n",
            id="Number.Hex",
        ),
        param(
            "105",
            "\x1b[38;2;235;188;186m105\x1b[39m\n",
            id="Number.Integer",
        ),
        param(
            "0o151",
            "\x1b[38;2;235;188;186m0o151\x1b[39m\n",
            id="Number.Oct",
        ),
        param(
            "x is not y and w is (y or z)",
            "\x1b[38;2;224;222;244mx\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143mis\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143mnot\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244my\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143mand\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mw\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143mis\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;224;222;244my\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143mor\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mz\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\n",  # noqa: E501
            id="Operator.Word",
        ),
        param(
            "3 != 4, 5 == 5, 0b001 << 3",
            "\x1b[38;2;235;188;186m3\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m!=\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;188;186m4\x1b[39m\x1b[38;2;144;140;170m,\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;188;186m5\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m==\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;188;186m5\x1b[39m\x1b[38;2;144;140;170m,\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;188;186m0b001\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m<<\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;188;186m3\x1b[39m\n",  # noqa: E501
            id="Operator",
        ),
        param(
            'f"f-strings {rule}"',
            '\x1b[38;2;49;116;143mf\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;246;193;119mf-strings \x1b[39m\x1b[38;2;224;222;244m{\x1b[39m\x1b[38;2;224;222;244mrule\x1b[39m\x1b[38;2;224;222;244m}\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\n',  # noqa: E501
            id="String.Affix",
        ),
        param(
            '"""This is a docstring."""',
            '\x1b[38;2;246;193;119m"""This is a docstring."""\x1b[39m\n',
            id="String.Doc",
        ),
        param(
            '"\\n\\t"',
            '\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;49;116;143m\\n\x1b[39m\x1b[38;2;49;116;143m\\t\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\n',  # noqa: E501
            id="String.Escape",
        ),
        param(
            '"%s" % "{xyzzy}".format(xyzzy="plugh")',
            '\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;224;222;244m%s\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;49;116;143m%\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;224;222;244m{xyzzy}\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\x1b[38;2;224;222;244mformat\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;224;222;244mxyzzy\x1b[39m\x1b[38;2;49;116;143m=\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;246;193;119mplugh\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\n',  # noqa: E501
            id="String.Interpol",
        ),
        param(
            '"This is a string."',
            '\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;246;193;119mThis is a string.\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\n',  # noqa: E501
            id="String",
        ),
        param(
            "    \n    ",
            "\x1b[38;2;224;222;244m    \x1b[39m\n\x1b[38;2;224;222;244m    \x1b[39m\n",  # noqa: E501
            id="Text",
        ),
        param(
            "[].reverse()",
            "\x1b[38;2;144;140;170m[\x1b[39m\x1b[38;2;144;140;170m]\x1b[39m\x1b[38;2;49;116;143m.\x1b[39m\x1b[38;2;224;222;244mreverse\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\n",  # noqa: E501
            id="Token.Punctuation",
        ),
    ],
)
def test_highlighting_base(code: str, expected: str) -> None:
    """The given code should highlight as expected."""
    assert highlight_base(code) == expected


@pytest.mark.parametrize(
    "code,expected",
    [
        param(
            "# This is a comment.",
            "\x1b[38;2;144;140;170m# This is a comment.\x1b[39m\n",
            id="Comment",
        ),
        param(
            "err?",
            "\x1b[38;2;224;222;244merr\x1b[39m\x1b[38;2;235;111;146m?\x1b[39m\n",  # noqa: E501
            id="Error",
        ),
        param(
            "from rosepine import RosePineMoonStyle",
            "\x1b[38;2;62;143;176mfrom\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mrosepine\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176mimport\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mRosePineMoonStyle\x1b[39m\n",  # noqa: E501
            id="Keyword.Namespace",
        ),
        param(
            "None",
            "\x1b[38;2;234;154;151mNone\x1b[39m\n",
            id="Keyword.Constant",
        ),
        param(
            "int",
            "\x1b[38;2;224;222;244mint\x1b[39m\n",
            id="Keyword.Type",
        ),
        param(
            "try:\n    pass\nexcept:\n    raise",
            "\x1b[38;2;62;143;176mtry\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\n\x1b[38;2;224;222;244m    \x1b[39m\x1b[38;2;62;143;176mpass\x1b[39m\n\x1b[38;2;62;143;176mexcept\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\n\x1b[38;2;224;222;244m    \x1b[39m\x1b[38;2;62;143;176mraise\x1b[39m\n",  # noqa: E501
            id="Keyword",
        ),
        param(
            "def method(self, other): ...",
            "\x1b[38;2;62;143;176mdef\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;111;146mmethod\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;235;111;146mself\x1b[39m\x1b[38;2;144;140;170m,\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mother\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\n",  # noqa: E501
            id="Name.Builtin.Pseudo",
        ),
        param(
            "list(map(lambda n: n + 1, range(5)))",
            "\x1b[38;2;224;222;244mlist\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;224;222;244mmap\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;62;143;176mlambda\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mn\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mn\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m+\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;234;154;151m1\x1b[39m\x1b[38;2;144;140;170m,\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mrange\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;234;154;151m5\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\n",  # noqa: E501
            id="Name.Builtin",
        ),
        param(
            "class IsDismissed: ...",
            "\x1b[38;2;62;143;176mclass\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;156;207;216mIsDismissed\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\n",  # noqa: E501
            id="Name.Class",
        ),
        param(
            "@decorator\ndef function(): ...",
            "\x1b[38;2;196;167;231;01m@decorator\x1b[39;00m\n\x1b[38;2;62;143;176mdef\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;111;146mfunction\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\n",  # noqa: E501
            id="Name.Decorator",
        ),
        param(
            'raise KeyError("Wrong lock.")',
            '\x1b[38;2;62;143;176mraise\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;156;207;216mKeyError\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;246;193;119mWrong lock.\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\n',  # noqa: E501
            id="Name.Exception",
        ),
        param(
            "def foo(bar: int, baz: Optional[str] = None) -> None: ...",
            "\x1b[38;2;62;143;176mdef\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;235;111;146mfoo\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;224;222;244mbar\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mint\x1b[39m\x1b[38;2;144;140;170m,\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mbaz\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mOptional\x1b[39m\x1b[38;2;144;140;170m[\x1b[39m\x1b[38;2;224;222;244mstr\x1b[39m\x1b[38;2;144;140;170m]\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m=\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;234;154;151mNone\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m-\x1b[39m\x1b[38;2;62;143;176m>\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;234;154;151mNone\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\n",  # noqa: E501
            id="Name.Function",
        ),
        param(
            'class IsDismissed:\n    __slots__ = ("attr",)',
            '\x1b[38;2;62;143;176mclass\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;156;207;216mIsDismissed\x1b[39m\x1b[38;2;144;140;170m:\x1b[39m\n\x1b[38;2;224;222;244m    \x1b[39m\x1b[38;2;235;111;146m__slots__\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m=\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;246;193;119mattr\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;144;140;170m,\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\n',  # noqa: E501
            id="Name.Variable.Magic",
        ),
        param(
            "life = 42",
            "\x1b[38;2;224;222;244mlife\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m=\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;234;154;151m42\x1b[39m\n",  # noqa: E501
            id="Name",
        ),
        param(
            "0b1101001",
            "\x1b[38;2;234;154;151m0b1101001\x1b[39m\n",
            id="Number.Bin",
        ),
        param(
            "105.0",
            "\x1b[38;2;234;154;151m105.0\x1b[39m\n",
            id="Number.Float",
        ),
        param(
            "0x69",
            "\x1b[38;2;234;154;151m0x69\x1b[39m\n",
            id="Number.Hex",
        ),
        param(
            "105",
            "\x1b[38;2;234;154;151m105\x1b[39m\n",
            id="Number.Integer",
        ),
        param(
            "0o151",
            "\x1b[38;2;234;154;151m0o151\x1b[39m\n",
            id="Number.Oct",
        ),
        param(
            "x is not y and w is (y or z)",
            "\x1b[38;2;224;222;244mx\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176mis\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176mnot\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244my\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176mand\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mw\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176mis\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;224;222;244my\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176mor\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;224;222;244mz\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\n",  # noqa: E501
            id="Operator.Word",
        ),
        param(
            "3 != 4, 5 == 5, 0b001 << 3",
            "\x1b[38;2;234;154;151m3\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m!=\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;234;154;151m4\x1b[39m\x1b[38;2;144;140;170m,\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;234;154;151m5\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m==\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;234;154;151m5\x1b[39m\x1b[38;2;144;140;170m,\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;234;154;151m0b001\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m<<\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;234;154;151m3\x1b[39m\n",  # noqa: E501
            id="Operator",
        ),
        param(
            'f"f-strings {rule}"',
            '\x1b[38;2;62;143;176mf\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;246;193;119mf-strings \x1b[39m\x1b[38;2;224;222;244m{\x1b[39m\x1b[38;2;224;222;244mrule\x1b[39m\x1b[38;2;224;222;244m}\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\n',  # noqa: E501
            id="String.Affix",
        ),
        param(
            '"""This is a docstring."""',
            '\x1b[38;2;246;193;119m"""This is a docstring."""\x1b[39m\n',
            id="String.Doc",
        ),
        param(
            '"\\n\\t"',
            '\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;62;143;176m\\n\x1b[39m\x1b[38;2;62;143;176m\\t\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\n',  # noqa: E501
            id="String.Escape",
        ),
        param(
            '"%s" % "{xyzzy}".format(xyzzy="plugh")',
            '\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;224;222;244m%s\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;62;143;176m%\x1b[39m\x1b[38;2;224;222;244m \x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;224;222;244m{xyzzy}\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\x1b[38;2;224;222;244mformat\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;224;222;244mxyzzy\x1b[39m\x1b[38;2;62;143;176m=\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;246;193;119mplugh\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\n',  # noqa: E501
            id="String.Interpol",
        ),
        param(
            '"This is a string."',
            '\x1b[38;2;246;193;119m"\x1b[39m\x1b[38;2;246;193;119mThis is a string.\x1b[39m\x1b[38;2;246;193;119m"\x1b[39m\n',  # noqa: E501
            id="String",
        ),
        param(
            "    \n    ",
            "\x1b[38;2;224;222;244m    \x1b[39m\n\x1b[38;2;224;222;244m    \x1b[39m\n",  # noqa: E501
            id="Text",
        ),
        param(
            "[].reverse()",
            "\x1b[38;2;144;140;170m[\x1b[39m\x1b[38;2;144;140;170m]\x1b[39m\x1b[38;2;62;143;176m.\x1b[39m\x1b[38;2;224;222;244mreverse\x1b[39m\x1b[38;2;144;140;170m(\x1b[39m\x1b[38;2;144;140;170m)\x1b[39m\n",  # noqa: E501
            id="Token.Punctuation",
        ),
    ],
)
def test_highlighting_moon(code: str, expected: str) -> None:
    """The given code should highlight as expected."""
    assert highlight_moon(code) == expected


@pytest.mark.parametrize(
    "code,expected",
    [
        param(
            "# This is a comment.",
            "\x1b[38;2;121;117;147m# This is a comment.\x1b[39m\n",
            id="Comment",
        ),
        param(
            "err?",
            "\x1b[38;2;87;82;121merr\x1b[39m\x1b[38;2;180;99;122m?\x1b[39m\n",
            id="Error",
        ),
        param(
            "from rosepine import RosePineDawnStyle",
            "\x1b[38;2;40;105;131mfrom\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;87;82;121mrosepine\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131mimport\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;87;82;121mRosePineDawnStyle\x1b[39m\n",  # noqa: E501
            id="Keyword.Namespace",
        ),
        param(
            "None",
            "\x1b[38;2;215;130;126mNone\x1b[39m\n",
            id="Keyword.Constant",
        ),
        param(
            "int",
            "\x1b[38;2;87;82;121mint\x1b[39m\n",
            id="Keyword.Type",
        ),
        param(
            "try:\n    pass\nexcept:\n    raise",
            "\x1b[38;2;40;105;131mtry\x1b[39m\x1b[38;2;121;117;147m:\x1b[39m\n\x1b[38;2;87;82;121m    \x1b[39m\x1b[38;2;40;105;131mpass\x1b[39m\n\x1b[38;2;40;105;131mexcept\x1b[39m\x1b[38;2;121;117;147m:\x1b[39m\n\x1b[38;2;87;82;121m    \x1b[39m\x1b[38;2;40;105;131mraise\x1b[39m\n",  # noqa: E501
            id="Keyword",
        ),
        param(
            "def method(self, other): ...",
            "\x1b[38;2;40;105;131mdef\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;180;99;122mmethod\x1b[39m\x1b[38;2;121;117;147m(\x1b[39m\x1b[38;2;180;99;122mself\x1b[39m\x1b[38;2;121;117;147m,\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;87;82;121mother\x1b[39m\x1b[38;2;121;117;147m)\x1b[39m\x1b[38;2;121;117;147m:\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\n",  # noqa: E501
            id="Name.Builtin.Pseudo",
        ),
        param(
            "list(map(lambda n: n + 1, range(5)))",
            "\x1b[38;2;87;82;121mlist\x1b[39m\x1b[38;2;121;117;147m(\x1b[39m\x1b[38;2;87;82;121mmap\x1b[39m\x1b[38;2;121;117;147m(\x1b[39m\x1b[38;2;40;105;131mlambda\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;87;82;121mn\x1b[39m\x1b[38;2;121;117;147m:\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;87;82;121mn\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m+\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;215;130;126m1\x1b[39m\x1b[38;2;121;117;147m,\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;87;82;121mrange\x1b[39m\x1b[38;2;121;117;147m(\x1b[39m\x1b[38;2;215;130;126m5\x1b[39m\x1b[38;2;121;117;147m)\x1b[39m\x1b[38;2;121;117;147m)\x1b[39m\x1b[38;2;121;117;147m)\x1b[39m\n",  # noqa: E501
            id="Name.Builtin",
        ),
        param(
            "class IsDismissed: ...",
            "\x1b[38;2;40;105;131mclass\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;86;148;159mIsDismissed\x1b[39m\x1b[38;2;121;117;147m:\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\n",  # noqa: E501
            id="Name.Class",
        ),
        param(
            "@decorator\ndef function(): ...",
            "\x1b[38;2;144;122;169;01m@decorator\x1b[39;00m\n\x1b[38;2;40;105;131mdef\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;180;99;122mfunction\x1b[39m\x1b[38;2;121;117;147m(\x1b[39m\x1b[38;2;121;117;147m)\x1b[39m\x1b[38;2;121;117;147m:\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\n",  # noqa: E501
            id="Name.Decorator",
        ),
        param(
            'raise KeyError("Wrong lock.")',
            '\x1b[38;2;40;105;131mraise\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;86;148;159mKeyError\x1b[39m\x1b[38;2;121;117;147m(\x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;234;157;52mWrong lock.\x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;121;117;147m)\x1b[39m\n',  # noqa: E501
            id="Name.Exception",
        ),
        param(
            "def foo(bar: int, baz: Optional[str] = None) -> None: ...",
            "\x1b[38;2;40;105;131mdef\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;180;99;122mfoo\x1b[39m\x1b[38;2;121;117;147m(\x1b[39m\x1b[38;2;87;82;121mbar\x1b[39m\x1b[38;2;121;117;147m:\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;87;82;121mint\x1b[39m\x1b[38;2;121;117;147m,\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;87;82;121mbaz\x1b[39m\x1b[38;2;121;117;147m:\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;87;82;121mOptional\x1b[39m\x1b[38;2;121;117;147m[\x1b[39m\x1b[38;2;87;82;121mstr\x1b[39m\x1b[38;2;121;117;147m]\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m=\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;215;130;126mNone\x1b[39m\x1b[38;2;121;117;147m)\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m-\x1b[39m\x1b[38;2;40;105;131m>\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;215;130;126mNone\x1b[39m\x1b[38;2;121;117;147m:\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\n",  # noqa: E501
            id="Name.Function",
        ),
        param(
            'class IsDismissed:\n    __slots__ = ("attr",)',
            '\x1b[38;2;40;105;131mclass\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;86;148;159mIsDismissed\x1b[39m\x1b[38;2;121;117;147m:\x1b[39m\n\x1b[38;2;87;82;121m    \x1b[39m\x1b[38;2;180;99;122m__slots__\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m=\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;121;117;147m(\x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;234;157;52mattr\x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;121;117;147m,\x1b[39m\x1b[38;2;121;117;147m)\x1b[39m\n',  # noqa: E501
            id="Name.Variable.Magic",
        ),
        param(
            "life = 42",
            "\x1b[38;2;87;82;121mlife\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m=\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;215;130;126m42\x1b[39m\n",  # noqa: E501
            id="Name",
        ),
        param(
            "0b1101001",
            "\x1b[38;2;215;130;126m0b1101001\x1b[39m\n",
            id="Number.Bin",
        ),
        param(
            "105.0",
            "\x1b[38;2;215;130;126m105.0\x1b[39m\n",
            id="Number.Float",
        ),
        param(
            "0x69",
            "\x1b[38;2;215;130;126m0x69\x1b[39m\n",
            id="Number.Hex",
        ),
        param(
            "105",
            "\x1b[38;2;215;130;126m105\x1b[39m\n",
            id="Number.Integer",
        ),
        param(
            "0o151",
            "\x1b[38;2;215;130;126m0o151\x1b[39m\n",
            id="Number.Oct",
        ),
        param(
            "x is not y and w is (y or z)",
            "\x1b[38;2;87;82;121mx\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131mis\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131mnot\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;87;82;121my\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131mand\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;87;82;121mw\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131mis\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;121;117;147m(\x1b[39m\x1b[38;2;87;82;121my\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131mor\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;87;82;121mz\x1b[39m\x1b[38;2;121;117;147m)\x1b[39m\n",  # noqa: E501
            id="Operator.Word",
        ),
        param(
            "3 != 4, 5 == 5, 0b001 << 3",
            "\x1b[38;2;215;130;126m3\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m!=\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;215;130;126m4\x1b[39m\x1b[38;2;121;117;147m,\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;215;130;126m5\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m==\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;215;130;126m5\x1b[39m\x1b[38;2;121;117;147m,\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;215;130;126m0b001\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m<<\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;215;130;126m3\x1b[39m\n",  # noqa: E501
            id="Operator",
        ),
        param(
            'f"f-strings {rule}"',
            '\x1b[38;2;40;105;131mf\x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;234;157;52mf-strings \x1b[39m\x1b[38;2;87;82;121m{\x1b[39m\x1b[38;2;87;82;121mrule\x1b[39m\x1b[38;2;87;82;121m}\x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\n',  # noqa: E501
            id="String.Affix",
        ),
        param(
            '"""This is a docstring."""',
            '\x1b[38;2;234;157;52m"""This is a docstring."""\x1b[39m\n',
            id="String.Doc",
        ),
        param(
            '"\\n\\t"',
            '\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;40;105;131m\\n\x1b[39m\x1b[38;2;40;105;131m\\t\x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\n',  # noqa: E501
            id="String.Escape",
        ),
        param(
            '"%s" % "{xyzzy}".format(xyzzy="plugh")',
            '\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;87;82;121m%s\x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;40;105;131m%\x1b[39m\x1b[38;2;87;82;121m \x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;87;82;121m{xyzzy}\x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\x1b[38;2;87;82;121mformat\x1b[39m\x1b[38;2;121;117;147m(\x1b[39m\x1b[38;2;87;82;121mxyzzy\x1b[39m\x1b[38;2;40;105;131m=\x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;234;157;52mplugh\x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;121;117;147m)\x1b[39m\n',  # noqa: E501
            id="String.Interpol",
        ),
        param(
            '"This is a string."',
            '\x1b[38;2;234;157;52m"\x1b[39m\x1b[38;2;234;157;52mThis is a string.\x1b[39m\x1b[38;2;234;157;52m"\x1b[39m\n',  # noqa: E501
            id="String",
        ),
        param(
            "    \n    ",
            "\x1b[38;2;87;82;121m    \x1b[39m\n\x1b[38;2;87;82;121m    \x1b[39m\n",  # noqa: E501
            id="Text",
        ),
        param(
            "[].reverse()",
            "\x1b[38;2;121;117;147m[\x1b[39m\x1b[38;2;121;117;147m]\x1b[39m\x1b[38;2;40;105;131m.\x1b[39m\x1b[38;2;87;82;121mreverse\x1b[39m\x1b[38;2;121;117;147m(\x1b[39m\x1b[38;2;121;117;147m)\x1b[39m\n",  # noqa: E501
            id="Token.Punctuation",
        ),
    ],
)
def test_highlighting_dawn(code: str, expected: str) -> None:
    """The given code should highlight as expected."""
    assert highlight_dawn(code) == expected
