.. |rose-pine-logo| image:: https://github.com/rose-pine/rose-pine-theme/raw/main/assets/icon.png
   :width: 30

=======================================
|rose-pine-logo| Rose Piné for Pygments
=======================================

All natural pine, faux fur and a bit of soho vibes for the classy minimalist

|Python versions| |Latest release| |test| |Codecov| |License| |Black| |Rose Pine Community|


.. toctree::
   :maxdepth: 1
   :caption: Contributing
   :hidden:

   changelog.rst
   contributing.rst
   code-of-conduct.rst
   license.rst

Installation
============

The ``pygments-rose-pine`` package is not currently published to
`PyPI <https://pypi.org/>`__. If, however, you still wish to install
this package, the following steps *should* work to install the `latest
release <https://github.com/drearondov/pygments-rose-pine/releases/latest>`__.

.. code:: bash

   repo="https://github.com/rose-pine/pygments.git"

   # Find the latest release.
   latest=$(git ls-remote --tags --refs $repo | # Fetch remote tags.
                    sort -t '/' -k 3 -V |       # Sort them by version.
                    tail -n 1 |                 # Take the latest one.
                    awk -F / '{print $3}')      # Return only the tag.

   # Craft the URL for the release asset.
   version=$(echo $latest | tr -d 'v')  # Remove the leading v.
   wheel="pygments_rose_pine-${version}-py3-none-any.whl"
   release="${repo}/releases/download/${latest}/${wheel}"

   # Install the release.
   pip install $release

Usage
=====

The style installs itself as a `Pygments
plugin <https://pygments.org/docs/plugins/#entrypoints>`__, so after
installation you should only need to launch your console with one of the
``rose-pine`` styles available (``rose-pine``, ``rose-pine-moon``,
``rose-pine-dawn``). Below there are some examples for common consoles.

IPython
-------

In the case of IPython, you can launch the console with the following
command.

.. code:: bash

   ipython --TerminalInteractiveShell.highlighting_style=rose-pine

or add it to your `IPython
config <https://ipython.readthedocs.io/en/stable/config/intro.html>`__.

.. code:: python

   config = get_config()
   config.TerminalInteractiveShell.highlighting_style = "rose-pine"

..

   *Note:* This will only affect your syntax highlighting. If you're
   looking to modify your prompt, Reilly Siemmens from the `IPython
   Gruvbox
   theme <https://github.com/reillysiemens/ipython-style-gruvbox>`__ has
   an excellent `example
   prompt <https://github.com/reillysiemens/dotfiles/blob/8994f69f23271aa93d83e81032542f17b38423fd/.ipython/profile_default/ipython_config.py>`__
   on how to customize it.

Radian
------

In the case of Radian, you can add the theme to your
`Radian <https://github.com/randy3k/radian>`__ configuration on your
``.radian_profile``

.. code:: python

   options(radian.color_scheme = "rose-pine")

..

   *Note:* For radian, the prompt modification options can be found on
   their `documentation <https://github.com/randy3k/radian>`__.

Gallery
=======

.. image:: static/rose-pine.png
   :align: left
   :width: 40%


.. image:: static/rose-pine-moon.png
   :width: 45%

.. image:: static/rose-pine-dawn.png
   :width: 40%


.. |Python versions| image:: https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fdrearondov%2Fpygments-rose-pine%2Fmain%2Fpyproject.toml&style=for-the-badge&logo=python&logoColor=white&color=blue
   :target: https://www.python.org/downloads/
.. |test| image:: https://github.com/drearondov/pygments-rose-pine/actions/workflows/test.yml/badge.svg
   :target: https://github.com/drearondov/pygments-rose-pine/actions/workflows/test.yml
.. |Codecov| image:: https://img.shields.io/codecov/c/github/drearondov/pygments-rose-pine?style=for-the-badge&logo=codecov&logoColor=white
.. |License| image:: https://img.shields.io/badge/license-ISC-purple?style=for-the-badge
   :target: https://github.com/drearondov/pygments-rose-pine/blob/main/LICENSE
.. |Latest release| image:: https://img.shields.io/github/v/release/drearondov/pygments-rose-pine?style=for-the-badge
   :target: https://github.com/drearondov/pygments-rose-pine/releases/latest
.. |Black| image:: https://img.shields.io/badge/code%20style-black-black?style=for-the-badge
   :target: https://github.com/psf/black
.. |Rose Pine Community| image:: https://img.shields.io/badge/community-rosé%20pine-26233a?labelColor=191724&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUwIiBoZWlnaHQ9IjIzNyIgdmlld0JveD0iMCAwIDI1MCAyMzciIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xNjEuMjI3IDE2MS4yNTFDMTMyLjE1NCAxNjkuMDQxIDExNC45MDEgMTk4LjkyNCAxMjIuNjkxIDIyNy45OTdDMTIzLjkyNSAyMzIuNjAzIDEyOC42NTkgMjM1LjMzNiAxMzMuMjY0IDIzNC4xMDJMMTg1LjkwNyAyMTkuOTk2QzIxOS41ODUgMjEwLjk3MiAyMzkuNTcgMTc2LjM1NCAyMzAuNTQ2IDE0Mi42NzdMMTYxLjIyNyAxNjEuMjUxWiIgZmlsbD0iIzI0NjI3QiIvPgo8cGF0aCBkPSJNODguMTgzNiAxNTkuOTg4QzExNy4yNTcgMTY3Ljc3OCAxMzQuNTEgMTk3LjY2MiAxMjYuNzIgMjI2LjczNUMxMjUuNDg2IDIzMS4zNCAxMjAuNzUyIDIzNC4wNzMgMTE2LjE0NyAyMzIuODM5TDYzLjUwNDEgMjE4LjczM0MyOS44MjY0IDIwOS43MSA5Ljg0MDk0IDE3NS4wOTIgMTguODY0OSAxNDEuNDE0TDg4LjE4MzYgMTU5Ljk4OFoiIGZpbGw9IiMyNDYyN0IiLz4KPHBhdGggZD0iTTE4Ni44NjcgMTcyLjk4QzE1Mi4wMDIgMTcyLjk4IDEyMy43MzcgMjAxLjI0NSAxMjMuNzM3IDIzNi4xMTFIMTg2Ljg3QzIyMS43MzYgMjM2LjExMSAyNTAgMjA3Ljg0NiAyNTAgMTcyLjk4TDE4Ni44NjcgMTcyLjk4WiIgZmlsbD0iIzMxNzQ4RiIvPgo8cGF0aCBkPSJNNjMuMTMyNyAxNzIuOThDOTcuOTk4NCAxNzIuOTggMTI2LjI2MyAyMDEuMjQ1IDEyNi4yNjMgMjM2LjExMUg2My4xM0MyOC4yNjQyIDIzNi4xMTEgLTEuNTI0MDNlLTA2IDIwNy44NDYgMCAxNzIuOThMNjMuMTMyNyAxNzIuOThaIiBmaWxsPSIjMzE3NDhGIi8+CjxwYXRoIGQ9Ik0xNzEuNzE3IDc1LjEyNjNDMTcxLjcxNyAxMDEuMjc2IDE1MC41MTggMTIyLjQ3NSAxMjQuMzY5IDEyMi40NzVDOTguMjE4OCAxMjIuNDc1IDc3LjAyMDIgMTAxLjI3NiA3Ny4wMjAyIDc1LjEyNjNDNzcuMDIwMiA0OC45NzY0IDk4LjIxODggMjcuNzc3OCAxMjQuMzY5IDI3Ljc3NzhDMTUwLjUxOCAyNy43Nzc4IDE3MS43MTcgNDguOTc2NCAxNzEuNzE3IDc1LjEyNjNaIiBmaWxsPSIjRUJCQ0JBIi8+CjxwYXRoIGQ9Ik0xNDQuMjE3IDg2LjIzNzlDMTYxLjY0OSA1Ni4wNDMyIDE1MS4zMDMgMTcuNDMyOSAxMjEuMTA4IDBMMTA2LjA2IDI2LjA2NDRDODguNjI3IDU2LjI1OSA5OC45NzM2IDk0Ljg2OTQgMTI5LjE2OCAxMTIuMzAyTDE0NC4yMTcgODYuMjM3OVoiIGZpbGw9IiNFQkJDQkEiLz4KPHBhdGggZD0iTTEyNS4yOTkgNjAuOTc4OUMxMTYuMjc1IDI3LjMwMTIgODEuNjU3NSA3LjMxNTY3IDQ3Ljk3OTcgMTYuMzM5Nkw2NC4zMTk3IDc3LjMyMTFDNzMuMzQzNiAxMTAuOTk5IDEwNy45NjEgMTMwLjk4NCAxNDEuNjM5IDEyMS45NkwxMjUuMjk5IDYwLjk3ODlaIiBmaWxsPSIjRUJCQ0JBIi8+CjxwYXRoIGQ9Ik0xMjQuOTI2IDYwLjk3ODlDMTMzLjk1IDI3LjMwMTIgMTY4LjU2NyA3LjMxNTY3IDIwMi4yNDUgMTYuMzM5NkwxODUuOTA1IDc3LjMyMTFDMTc2Ljg4MSAxMTAuOTk5IDE0Mi4yNjMgMTMwLjk4NCAxMDguNTg2IDEyMS45NkwxMjQuOTI2IDYwLjk3ODlaIiBmaWxsPSIjRUJCQ0JBIi8+Cjwvc3ZnPgo=&style=for-the-badge
   :target: https://github.com/rose-pine/rose-pine-theme
