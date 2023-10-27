"""Soho vibes for Pygments.

Inspired or informed by the following:
    - rose-pine's theme: https://rosepinetheme.com
    - Reylly Siemmens's gruvbox Pygments theme:
      https://github.com/reillysiemens/ipython-style-gruvbox
    - python-mode's syntax highlighting: https://git.io/JvV4t
    - The Pygments Python lexer: https://git.io/Jviis
"""

from dataclasses import dataclass
from typing import Any, Dict

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
)

__author__: str = "Andrea Rondón"
__email__: str = "andrea.estefania.rv@gmail.com"
__version__: str = "1.0.0"


@dataclass(frozen=True)
class Color:
    """
    Absolute colors as defined by rose-pine: https://rosepinetheme.com/palette
    """

    pine_base = "#191724"
    pine_surface = "#1f1d2e"
    pine_overlay = "#26233a"
    pine_muted = "#6e6a86"
    pine_subtle = "#908caa"
    pine_text = "#e0def4"
    pine_love = "#eb6f92"
    pine_gold = "#f6c177"
    pine_rose = "#ebbcba"
    pine_pine = "#31748f"
    pine_foam = "#9ccfd8"
    pine_iris = "#c4a7e7"
    pine_highlightlow = "#21202e"
    pine_highlightmed = "#403d52"
    pine_highlighthigh = "#524f67"


class RosePineStyle(Style):
    """Soho vibes for Pygments. Based on the colors of Rose Pine main theme"""

    styles: Dict[Any, str] = {
        Comment: Color.pine_subtle,
        Error: Color.pine_love,
        Keyword.Namespace: Color.pine_pine,
        Keyword.Constant: Color.pine_rose,
        Keyword.Type: Color.pine_foam,
        Keyword: Color.pine_pine,
        Name.Builtin.Pseudo: Color.pine_love,
        Name.Builtin: Color.pine_text,
        Name.Class: Color.pine_foam,
        Name.Decorator: f"{Color.pine_iris} bold",
        Name.Exception: Color.pine_foam,
        Name.Function: Color.pine_love,
        Name.Variable.Magic: Color.pine_love,
        Name: Color.pine_text,
        Number: Color.pine_rose,
        Operator.Word: Color.pine_pine,
        Operator: Color.pine_pine,
        String.Affix: Color.pine_pine,
        String.Escape: Color.pine_pine,
        String.Interpol: Color.pine_text,
        String: Color.pine_gold,
        Text: Color.pine_text,
        Token.Punctuation: Color.pine_subtle,
    }
