#!/usr/bin/python
"""Gtk theme generator."""

import os

import static
import aggregate

def cli(resource_dir, output_dir):
    """Generate gtk theme. get colors by commandline arguments."""
    import sys
    g = aggregate.Generator(resource_dir, output_dir)
    print 'bg', sys.argv[1:3]
    g.background(*sys.argv[1:3])
    print 'font', sys.argv[3:5]
    g.font(*sys.argv[3:5])
    print 'eventable', sys.argv[5:7]
    g.eventable(*sys.argv[5:7])
    g.generate()

def get_install_path():
	if 'USERNAME' in os.environ and os.environ['USERNAME'] == 'root':
		installpath = '/usr/share/themes/%s' % static.theme_dir
	elif 'HOME' in os.environ:
		installpath = os.environ['HOME']+'/.themes/%s' % static.theme_dir
	return installpath



