# -*- coding: utf-8 -*-
import os
from os import path as p
import fontforge
import shutil

here = p.dirname(p.abspath(__file__))
repos = p.dirname(here)
libertinus = p.join(here, 'Fonts', 'LibertinusSerif')
dir_ = p.join(repos, '_LinusLibertinus')
if not p.exists(dir_):
    os.makedirs(dir_)


# Linus Libertinus
# ----------------------------------------------
# Linus Libertinus does not have semibold styles
libert_all = [
    'LibertinusSerif-Italic.otf',
    'LibertinusSerif-Bold.otf',
    'LibertinusSerif-Regular.otf',
    'LibertinusSerif-BoldItalic.otf',
]


def rep0(s):
    return s.replace(
        'LibertinusSerif', 'LinusLibertinus').replace(
        'Libertinus Serif', 'Linus Libertinus')


def rep1(obj, _rep):
    if isinstance(obj, str):
        return _rep(obj)
    elif isinstance(obj, tuple):
        return tuple(rep(item) for item in obj)
    else:
        raise RuntimeError('{} is neither str nor tuple'.format(obj))


def rep(s):
    return rep1(s, rep0)


for file_ in libert_all:
    f = p.join(dir_, file_)
    shutil.copy(p.join(libertinus, file_), f)
    font = fontforge.open(f)
    font.fontname = rep(font.fontname)
    font.familyname = rep(font.familyname)
    font.fullname = rep(font.fullname)
    font.sfnt_names = [rep(item) for item in font.sfnt_names]
    font.generate(rep(f).replace('.otf', '.ttf'))
    font.close()
    os.remove(f)


# Copy License
# ----------------------------------------------
for file_ in ['OFL.txt', 'FONTLOG.txt', 'AUTHORS.txt', 'LinusLibertinusMath-Regular.ttf']:
    shutil.copy(p.join(libertinus, file_), p.join(dir_, file_))
