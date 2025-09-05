"""Soho vibes for Pygments.

Inspired or informed by the following:
    - rose-pine's theme: https://rosepinetheme.com
    - Reylly Siemmens's gruvbox Pygments theme:
      https://github.com/reillysiemens/ipython-style-gruvbox
    - The Pygments Python lexer: https://git.io/Jviis
"""

from collections.abc import Mapping
from dataclasses import dataclass

from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Keyword,
    Name,
    Number,
    Operator,
    String,
    Text,
    Token,
    _TokenType,
)


@dataclass(frozen=True)
class Color:
    """Absolute colors as defined by rose-pine: https://rosepinetheme.com/palette."""  # noqa: E501

    dawn_base = "#faf4ed"
    dawn_surface = "#fffaf3"
    dawn_overlay = "#f2e9e1"
    dawn_muted = "#9893a5"
    dawn_subtle = "#797593"
    dawn_text = "#575279"
    dawn_love = "#b4637a"
    dawn_gold = "#ea9d34"
    dawn_rose = "#d7827e"
    dawn_pine = "#286983"
    dawn_foam = "#56949f"
    dawn_iris = "#907aa9"
    dawn_highlightlow = "#f4ede8"
    dawn_highlightmed = "#dfdad9"
    dawn_highlighthigh = "#cecacd"


class RosePineDawnStyle(Style):
    """Soho vibes for Pygments. Based on the colors of Rose Pine Dawn theme."""  # noqa: E501

    background_color: str = Color.dawn_base

    styles: Mapping[_TokenType, str] = {
        Comment: Color.dawn_subtle,
        Error: Color.dawn_love,
        Keyword.Namespace: Color.dawn_pine,
        Keyword.Constant: Color.dawn_rose,
        Keyword.Type: Color.dawn_foam,
        Keyword: Color.dawn_pine,
        Name.Builtin.Pseudo: Color.dawn_love,
        Name.Builtin: Color.dawn_text,
        Name.Class: Color.dawn_foam,
        Name.Decorator: f"{Color.dawn_iris} bold",
        Name.Exception: Color.dawn_foam,
        Name.Function: Color.dawn_love,
        Name.Variable.Magic: Color.dawn_love,
        Name: Color.dawn_text,
        Number: Color.dawn_rose,
        Operator.Word: Color.dawn_pine,
        Operator: Color.dawn_pine,
        String.Affix: Color.dawn_pine,
        String.Escape: Color.dawn_pine,
        String.Interpol: Color.dawn_text,
        String: Color.dawn_gold,
        Text: Color.dawn_text,
        Token.Punctuation: Color.dawn_subtle,
    }
