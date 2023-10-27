"""Soho vibes for Pygments.

Inspired or informed by the following:
    - rose-pine's theme: https://rosepinetheme.com
    - Reylly Siemmens's gruvbox Pygments theme: https://github.com/reillysiemens/ipython-style-gruvbox
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

    moon_base = "#232136"
    moon_surface = "#2a273f"
    moon_overlay = "#393552"
    moon_muted = "#6e6a86"
    moon_subtle = "#908caa"
    moon_text = "#e0def4"
    moon_love = "#eb6f92"
    moon_gold = "#f6c177"
    moon_rose = "#ea9a97"
    moon_pine = "#3e8fb0"
    moon_foam = "#9ccfd8"
    moon_iris = "#c4a7e7"
    moon_highlightlow = "#2a283e"
    moon_highlightmed = "#44415a"
    moon_highlighthigh = "#56526e"

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


class RosePineDawnStyle(Style):
    """Soho vibes for Pygments. Based on the colors of Rose Pine Dawn theme"""

    styles: Dict[Any, str] = {
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


class RosePineMoonStyle(Style):
    """Soho vibes for Pygments. Based on the colors of Rose Pine Moon theme"""

    styles: Dict[Any, str] = {
        Comment: Color.moon_subtle,
        Error: Color.moon_love,
        Keyword.Namespace: Color.moon_pine,
        Keyword.Constant: Color.moon_rose,
        Keyword.Type: Color.moon_foam,
        Keyword: Color.moon_pine,
        Name.Builtin.Pseudo: Color.moon_love,
        Name.Builtin: Color.moon_text,
        Name.Class: Color.moon_foam,
        Name.Decorator: f"{Color.moon_iris} bold",
        Name.Exception: Color.moon_foam,
        Name.Function: Color.moon_love,
        Name.Variable.Magic: Color.moon_love,
        Name: Color.moon_text,
        Number: Color.moon_rose,
        Operator.Word: Color.moon_pine,
        Operator: Color.moon_pine,
        String.Affix: Color.moon_pine,
        String.Escape: Color.moon_pine,
        String.Interpol: Color.moon_text,
        String: Color.moon_gold,
        Text: Color.moon_text,
        Token.Punctuation: Color.moon_subtle,
    }
