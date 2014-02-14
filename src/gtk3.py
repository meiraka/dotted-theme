"""gtk3 theme generator class."""

import os
import image

class Generator(image.RecursiveEffector):
    """A class for gkt3 theme generater."""
    def __init__(self, resource_dir, output_dir):
        """Setup in/out resource path and default color.

        :resource_dir: input index colored image files dir.
        :output_dir: theme saved dir.
        """
        self.__resource_dir = resource_dir
        self.__output_dir = output_dir
        image.RecursiveEffector.__init__(self, resource_dir+'/gtk-3.0/index')

    def generate(self):
        """Write gtk3 theme files to output dir.

        Arguments:
        output_dir -- string output path (ex. /usr/share/themes/test)
        """
        self.__generate_rc(self.__output_dir)
        self.paint(self.__output_dir+'/gtk-3.0/colored')

    def __generate_rc(self, output_dir):

        self.__output_dir = output_dir
        #copy from share/
        self._copy('gtk.css')
        self._copy('gtk-widgets.css')
        self._copy('assets/check1.png')
        self._copy('assets/check2.png')
        self._copy('assets/check3.png')
        self._copy('assets/option1.png')
        self._copy('assets/option2.png')
        self._copy('assets/option3.png')
        #generato color.css
        color = """
            @define-color fg_inactive %(fg_)s; 
            @define-color bg_inactive %(bg_)s; 
            @define-color eg_inactive %(eg_)s;
            @define-color fg_normal %(fg_)s; 
            @define-color bg_normal %(bg_)s; 
            @define-color eg_normal %(eg_)s;
            @define-color fg_active %(hfg_)s; 
            @define-color bg_active %(hbg_)s;
            @define-color eg_active %(heg_)s;
            @define-color link_color #605060; 
            @define-color error_color #805060; 
            """ % {
                'fg_':self.fg,
                'bg_':self.bg,
                'eg_':self.eg,
                'hfg_':self.hfg,
                'hbg_':self.hbg,
                'heg_':self.heg,
                '':''}
        f = open(self.__output_dir+'/gtk-3.0/color.css', 'w')
        f.write(color)
        f.close()

    def _copy(self, input):
        dir = os.path.dirname(self.__output_dir+'/gtk-3.0/'+input)
        if not os.path.exists(dir):
            os.makedirs(dir)
        f = open(self.__resource_dir+'/gtk-3.0/'+input, 'r')
        a = f.read()
        f.close()
        f = open(self.__output_dir+'/gtk-3.0/'+input, 'w')
        f.write(a)
        f.close()

