#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:53:41 2020

@author: Alejandro Villada Balbuena
"""
#%%
from __future__ import division, unicode_literals, print_function  # for compatibility with Python 2 and 3

from pims import ND2Reader_SDK
from tifffile import imsave
import os

workdir = '/home/user/folder/'
filename = 'test'
frames = ND2Reader_SDK(workdir + filename + '.nd2')
#%%
n=len(frames)
outdir = workdir + 'sep/'
os.makedirs(outdir)
for x in range (0,n):
    imsave(outdir + filename + '_T' + str(x).zfill(6) + '.tif', frames[x])
