#!/usr/bin/env python
"""image generator.
"""
import os
import re
import sys
import bitmap

class RecursiveGenerator(object):
    """Recursive image generator.

    """
        
    def __init__(self, resource_dir, output_dir):
        """Setup in/out resource path and default color.

        :resource_dir: input index colored image files dir.
        :output_dir: theme saved dir.
        """
        self.__resource_dir = resource_dir
        self.__output_dir = output_dir
        self.__filter = []
        self.fg='#404040'
        self.bg='#ffffff'
        self.hfg='#ffffff'
        self.hbg='#808080'
        
    def add_filter(self, regex_format, hexcolor1, hexcolor2):
        """add regex filter."""
        self.__filter.append({u'str':regex_format, 
            u'regex':re.compile(regex_format), 
            u'color1':hexcolor1, 
            u'color2':hexcolor2})

    def clear_filter(self):
        """clear regex filter."""
        self.__filter = []

    def background(self, active, inactive):
        self.bg = inactive
        self.hbg = active

    def font(self, active, inactive):
        self.fg = inactive
        self.hfg = active

    def eventable(self, active, inactive):
        """Sets eventable object color."""
        self.add_filter(u'.+base.+', active, inactive)
        self.add_filter(u'.+normal.+', active, inactive)
        self.add_filter(u'.+active.+', active, inactive)
        self.add_filter(u'.+inactive.+', active, inactive)
        self.add_filter(u'.+hover.+', active, inactive)
        self.add_filter(u'.+pressed.+', active, inactive)

    def paint_images(self):
        """!"""
        self.add_filter(u'.*', self.hbg, self.bg)
        self.__paint_images(self.__resource_dir, self.__output_dir)

    def __paint_images(self, input_dir, output_dir, root=''):
        """Convert gray scaled images to RGB images recursively."""
        if not root:
            root= input_dir
        self.__make_dirs(output_dir)
        for i in os.listdir(input_dir):
            if os.path.isdir(input_dir+u'/'+i):
                self.__paint_images(input_dir+u'/'+i, output_dir, root)
            else:
                if i.endswith('png'):
                    image_path = input_dir+u'/'+i
                    save_path = input_dir.replace(
                        root, 
                        output_dir)+u'/'+i
                    save_dir = os.path.dirname(save_path)
                    if not os.path.exists(save_dir):
                        os.makedirs(save_dir)
                    self.__paint_image(image_path, save_path)

    def __paint_image(self, image_path, save_path):
        """paint an image and save to save_path"""
        for i in self.__filter:
            if i[u'regex'].match(image_path):
                bitmap.pigment(image_path, save_path, i[u'color1'], i[u'color2'])
                break

    def __make_dirs(self, output_path):
        """Generate directory to make file."""
        if not os.path.exists(os.path.dirname(output_path)):
            os.makedirs(os.path.dirname(output_path))

