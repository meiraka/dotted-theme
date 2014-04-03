"""gtk2 theme generator class."""

import os
import image

class Generator(image.RecursiveEffector):
    """A class for gtk2 theme generator."""
        
    def __init__(self, resource_dir, output_dir):
        """Setup in/out resource path and default color.

        :resource_dir: input index colored image files dir.
        :output_dir: theme saved dir.
        """
        self.__resource_dir = resource_dir
        self.__output_dir = output_dir
        image.RecursiveEffector.__init__(self, resource_dir+'/gtk-2.0/index')

    def generate(self):
        """Write gtk2 theme files to output dir."""

        self.add_filter(u'.*', self.hbg, self.bg)
        self._copy('gtkrc')
        self.__generate_rc(self.__output_dir)
        self.paint(self.__output_dir+'/gtk-2.0/colored')

    def __generate_rc(self, output_dir):
        """generate colorrc file."""
        strings = """#author: mei raka 
            #DO NOT EDIT THIS FILE!
            style "color"    #GtkWidget
            {
            fg[NORMAL] = "%(fg_)s" 
            fg[ACTIVE] = "%(fg_)s" 
            fg[PRELIGHT] = "%(hfg_)s" 
            fg[SELECTED] = "%(fg_)s" 
            fg[INSENSITIVE] = "%(fg_)s" 
            bg[NORMAL] = "%(bg_)s" 
            bg[ACTIVE] = "%(bg_)s" 
            bg[PRELIGHT] = "%(hbg_)s"
            bg[SELECTED] = "%(hbg_)s"
            bg[INSENSITIVE] = "%(bg_)s"
            base[NORMAL] = "%(bg_)s"
            base[ACTIVE] = "%(hbg_)s" 
            base[PRELIGHT] = "%(bg_)s"
            base[INSENSITIVE] = "%(bg_)s"
            base[SELECTED]     = "%(hbg_)s"
            text[NORMAL] = "%(fg_)s"
            text[INSENSITIVE] = "%(fg_)s"
            text[SELECTED] = "%(fg_)s"
            text[ACTIVE] = "%(fg_)s"
            text[PRELIGHT]     = "%(bg_)s"
            }
            class "GtkWidget" style "color"
            class "GtkWindow" style "color"

            style "toolbar-color"
            {
            bg[NORMAL] = "%(hbg_)s" 
            bg[ACTIVE] = "%(bg_)s" 
            bg[INSENSITIVE] = "%(hbg_)s"
            base[NORMAL] = "%(hbg_)s"
            base[ACTIVE] = "%(bg_)s" 
            base[PRELIGHT] = "%(bg_)s"
            base[INSENSITIVE] = "%(hbg_)s"
            base[SELECTED]     = "%(bg_)s"

            }

            style "menubar"
            {
            bg[NORMAL] = "%(bg_)s" 
            bg[ACTIVE] = "%(bg_)s" 
            bg[PRELIGHT] = "%(bg_)s" 
            bg[SELECTED] = "%(bg_)s" 
            bg[INSENSITIVE] = "%(bg_)s"
            base[NORMAL] = "%(bg_)s"
            base[ACTIVE] = "%(bg_)s" 
            base[PRELIGHT] = "%(bg_)s"
            base[INSENSITIVE] = "%(bg_)s"
            base[SELECTED]     = "%(bg_)s"
            }

            class "GtkMenuBar*"                     style "menubar"
            widget_class "*MenuBar.*"               style "menubar"

            style "menuitem"    #one of menu items    
            {
            bg[NORMAL] = "%(heg_)s" 
            bg[ACTIVE] = "%(eg_)s" 
            bg[PRELIGHT] = "%(eg_)s" 
            bg[SELECTED] = "%(eg_)s" 
            bg[INSENSITIVE] = "%(heg_)s"

            fg[NORMAL] = "%(hfg_)s" 
            fg[ACTIVE] = "%(fg_)s" 
            fg[PRELIGHT] = "%(fg_)s" 
            fg[SELECTED] = "%(fg_)s" 
            fg[INSENSITIVE] = "%(fg_)s" 
            }

            class "GtkMenu"             style "menuitem"
            widget_class "*.<MenuItem>."    style "menuitem"
            class "GtkMenuItem"        style "menuitem"
            class "GtkTearoffMenuItem"    style "menuitem"
            #widget_class "*GtkToolbar*" style "toolbar-color"


            style "list-header"  
            {
            GtkTreeView::odd_row_color = "%(bg_)s"
            GtkTreeView::even_row_color = "%(bg_)s"
            }

            widget_class "*List" style "list-header"
            widget_class "*GtkTree*" style "list-header"
            widget_class "*GtkCList*" style "list-header"


            """ % {
                'fg_':self.fg,
                'bg_':self.bg,
                'hfg_':self.hfg,
                'hbg_':self.hbg,
                                'eg_':self.eg,
                                'heg_':self.heg}
        f = open(self.__output_dir+'/gtk-2.0/colorrc', 'w')
        f.write(strings)
        f.close()

    def _copy(self, input):
        dir = os.path.dirname(self.__output_dir+'/gtk-2.0/'+input)
        if not os.path.exists(dir):
            os.makedirs(dir)
        f = open(self.__resource_dir+'/gtk-2.0/'+input, 'r')
        a = f.read()
        f.close()
        f = open(self.__output_dir+'/gtk-2.0/'+input, 'w')
        f.write(a)
        f.close()

