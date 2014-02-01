#!/usr/bin/env python
"""Bitmap file image controller."""

import Image
import ImageFilter
import ImageEnhance

def pigment(filepath, savepath, color1, color2='#ffffff'):
    """Generates colored image from index colored bitmap image.

    :filepath: base image path.
    :savepath: colored image path. if empty, show image result.
    :color1: convert bright color to given hexcolor
    :color2: convert dark color to given hexcolor
    """
    rgb = (int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16))
    target_rgb = (int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16))
    image = Image.open(filepath)
    image.convert('RGBA')
    if image.mode == 'LA':
        _, alpha = image.split()
    elif image.mode == 'L':
        _,  = image.split()
        alpha = None
    elif image.mode == 'RGBA':
        _r, _g, _b, alpha = image.split()
        print 'warning! file:'+filepath +' is '+image.mode
    else:
        print 'warning! file:'+filepath +' is '+image.mode
        overlay = Image.new('RGB', image.size, rgb)
        overlay.save(savepath)
        return False

    overlay = Image.new('RGB', image.size, rgb)
    R, G, B = overlay.split()
    if alpha:
        colored = Image.merge('RGBA', (R, G, B, alpha))
    else:
        colored = Image.merge('RGB', (R, G, B))
        
    if image.mode == 'LA' or image.mode == 'L':
        target_r, target_g, target_b = target_rgb
        grays_pix = _.load()
        colored_pix = colored.load()
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                if image.mode == 'LA':
                    R, G, B, A = colored_pix[x, y]
                    mix = float(grays_pix[x, y])/255.0
                    colored_pix[x, y] = (int(R+(target_r-R)*mix), int(G+(target_g-G)*mix), int(B+(target_b-B)*mix), A)
                else:
                    R , G, B = colored_pix[x, y]
                    mix = float(grays_pix[x, y])/255.0
                    colored_pix[x, y] = (int(R+(target_r-R)*mix), int(G+(target_g-G)*mix), int(B+(target_b-B)*mix))
    
    if savepath:
        colored.save(savepath)
    else:
        colored.show()
        pass
    return True
