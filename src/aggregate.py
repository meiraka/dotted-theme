#!/usr/bin/python
"""Aggregates generator."""

import gtk2
import gtk3

class Generator(object):
    def __init__(self, resource_dir, output_dir):
        self.generators = [ gtk2.Generator(resource_dir, output_dir)
                          , gtk3.Generator(resource_dir, output_dir)]

    def background(self, active, inactive):
        for g in self.generators:
            g.background(active, inactive)

    def font(self, active, inactive):
        for g in self.generators:
            g.font(active, inactive)

    def eventable(self, active, inactive):
        for g in self.generators:
            g.eventable(active, inactive)

    def generate(self):
        for g in self.generators:
            g.generate()


