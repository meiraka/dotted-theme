============
dotted-theme
============

gtk theme generator


usage
=====

::

  ./dotted active_bg inactive_bg active_font inactive_font active_buttons inactive_buttons

install
=======

uses setup.py
-------------

::

  python setup.py install


build debian pkg and install
----------------------------

::

  debuild -us -uc
  sudo dpkg -i ../dotted-theme_*_all.deb

