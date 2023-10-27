# Rose Pine for Pygments

Release v. (`Changelog <changelog>`{.interpreted-text role="ref"})

[![GitHub Actions test status](https://img.shields.io/github/workflow/status/reillysiemens/ipython-style-gruvbox/Test/main.svg?style=flat-square&label=tests)](https://github.com/reillysiemens/ipython-style-gruvbox/actions?query=workflow%3ATest)

[![Coveralls code coverage](https://img.shields.io/coveralls/github/reillysiemens/ipython-style-gruvbox/main?style=flat-square)](https://coveralls.io/github/reillysiemens/ipython-style-gruvbox)

[![License](https://img.shields.io/badge/license-ISC-purple?style=flat-square)](https://github.com/reillysiemens/ipython-style-gruvbox/blob/main/LICENSE)

[![Python versions](https://img.shields.io/badge/python-3.8%20%7C%203.9-blue?style=flat-square)](https://www.python.org/downloads/)

[![Latest release](https://img.shields.io/github/v/release/reillysiemens/ipython-style-gruvbox?style=flat-square)](https://github.com/reillysiemens/ipython-style-gruvbox/releases/latest)

[![Any color you like](https://img.shields.io/badge/code%20style-black-black?style=flat-square)](https://github.com/psf/black)

An opinionated terminal colorscheme for IPython using
[gruvbox](https://github.com/morhetz/gruvbox) colors.

![Rose Pine for Pygments](static/ipython-style-gruvbox.png)

## Installation

The `ipython-style-gruvbox` package is not currently published to
[PyPI](https://pypi.org/) because of its highly opinionated, personal
nature. If, however, you still wish to install this package, the
following steps *should* work to install the [latest
release](https://github.com/reillysiemens/ipython-style-gruvbox/releases/latest).

``` bash
repo='https://github.com/reillysiemens/ipython-style-gruvbox'

# Find the latest release.
latest=$(git ls-remote --tags --refs $repo | # Fetch remote tags.
                 sort -t '/' -k 3 -V |       # Sort them by version.
                 tail -n 1 |                 # Take the latest one.
                 awk -F / '{print $3}')      # Return only the tag.

# Craft the URL for the release asset.
version=$(echo $latest | tr -d 'v')  # Remove the leading v.
wheel="ipython_style_gruvbox-${version}-py3-none-any.whl"
release="${repo}/releases/download/${latest}/${wheel}"

# Install the release.
pip install $release
```

## Usage

The style installs itself as a [Pygments
plugin](https://pygments.org/docs/plugins/#entrypoints), so after
installation you should only need to launch IPython with the `gruvbox`
style

``` bash
ipython --TerminalInteractiveShell.highlighting_style=gruvbox
```

or add it to your [IPython
config](https://ipython.readthedocs.io/en/stable/config/intro.html).

``` python
config = get_config()
config.TerminalInteractiveShell.highlighting_style = "rose-pine"
```

::: note
::: title
Note
:::

This will only affect your syntax highlighting. If you\'re looking to
create a prompt that looks exactly like the one in the image above this
[example
prompt](https://github.com/reillysiemens/dotfiles/blob/8994f69f23271aa93d83e81032542f17b38423fd/.ipython/profile_default/ipython_config.py)
might help.
:::

::: {.toctree hidden="" maxdepth="1"}
Code of Conduct \<code-of-conduct\> changelog contributing
:::
