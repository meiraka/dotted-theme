"""
"""
import os
import sys
import glob
from setuptools import setup

def get_pair(pair,base):
    lis = []
    for filename in os.listdir(base):
        if os.path.isdir(base+'/'+filename):
            get_pair(pair,base+'/'+filename)
        else:
            lis.append(base+'/'+filename)
    pair.append((base,lis))
    pair.reverse()
    return pair

resources_pair = []
get_pair(resources_pair,u'share')
res = [(b.replace('share','share/dotted-theme'),f) for b,f in resources_pair]
setup_args = {}
setup_args['packages'] = ['dotted']
setup_args['package_dir'] = {'dotted':'src'}
setup_args['data_files'] = res  + [('bin',['bin/dotted'])]

setup(name='dotted',
    version='1.0.0',
    author='mei raka',
    **setup_args)
