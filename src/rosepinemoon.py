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


@dataclass(frozen=True)
class Color:
    """Absolute colors as defined by rose-pine: https://rosepinetheme.com/palette."""

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


class RosePineMoonStyle(Style):
    """Soho vibes for Pygments. Based on the colors of Rose Pine Moon theme."""

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
