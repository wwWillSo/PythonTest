#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'WillSo'

from PIL import Image

im = Image.open('format.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((300, 200))
im.save('thumb.jpg', 'JPEG')
