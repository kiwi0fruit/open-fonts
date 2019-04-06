# -*- coding: utf-8 -*-
import os
from os.path import join
import fontforge
import shutil


repos = os.path.normpath(join(os.getcwd(), '../'))
libertinus = join(repos, 'libertinus')
pt = join(os.getcwd(), 'Fonts')
dir_ = join(repos, '_linus_libertini')
if not os.path.exists(dir_):
    os.makedirs(dir_)


# Linus Libertini
# ----------------------------------------------
# Linus Libertini does not have semibold styles
libert_all = [
    'LibertinusSerif-Italic.otf',
    'LibertinusSerif-Bold.otf',
    'LibertinusSerif-Regular.otf',
    'LibertinusSerif-BoldItalic.otf',
]


def rep(string):
    def _rep(s):
        return s.replace('ibertinus', 'inus').replace('serif', 'libertini').replace('Serif', 'Libertini')

    if isinstance(string, str):
        return _rep(string)
    else:
        if isinstance(string, tuple):
            return tuple(_rep(item) for item in string)
        else:
            return string


for file_ in libert_all:
    f = join(dir_, file_)
    shutil.copy(join(libertinus, file_), f)
    font = fontforge.open(f)
    font.fontname = rep(font.fontname)
    font.familyname = rep(font.familyname)
    font.fullname = rep(font.fullname)
    font.sfnt_names = [rep(item) for item in font.sfnt_names]
    font.generate(rep(f))
    os.remove(f)


# Copy License
# ----------------------------------------------
for file_ in ['OFL.txt', 'FONTLOG.txt']:
    shutil.copy(join(libertinus, file_), join(dir_, file_))
