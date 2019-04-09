# -*- coding: utf-8 -*-
import os
from os import path as p
import fontforge
import shutil

here = p.dirname(p.abspath(__file__))
repos = p.dirname(here)
libertinus = p.join(repos, 'libertinus')
pt = p.join(here, 'Fonts')
dir_ = p.join(repos, '_LinusLibertini')
if not p.exists(dir_):
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


def rep0(s):
    return s.replace('ibertinus', 'inus').replace('serif', 'libertini').replace('Serif', 'Libertini')


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
    font.generate(rep(f))
    font.close()
    os.remove(f)


# Libertinus Serif RRegular, IItalic, BBold, BBoldIItalic
# ------------------------------------------------------
subdir = p.join(dir_, 'linus_libertini_font_swap_chrome_bugfix')
if not p.exists(subdir):
    os.makedirs(subdir)


def rep2(s):
    return s.replace('Regular', 'RRegular').replace('Bold', 'BBold').replace('Italic', 'IItalic')


def rep3(s, _style):
    return s.replace(
        'Linus Libertini ' + rep2(_style),
        'Linus Libertini'
    ).replace(
        'Linus Libertini',
        'Linus Libertini ' + rep2(_style)
    ).replace(
        'LinusLibertini',
        'LinusLibertini' + rep2(_style)
    )


for style in [
    'Italic',
    'Bold',
    'Regular',
    'BoldItalic',
]:
    file_ = 'LinusLibertini-' + style + '.otf'
    font = fontforge.open(p.join(dir_, file_))

    font.fontname = rep2(font.fontname.replace('-', ''))
    new_fn = rep2(font.familyname + ' ' + style)
    font.fullname = font.fullname.replace(font.familyname, new_fn)
    font.familyname = new_fn

    def rep(s):
        return rep1(s, lambda s: rep3(s, style))
    font.sfnt_names = [rep(item) for item in font.sfnt_names]

    font.generate(p.join(subdir, font.fontname + '.otf'))
    font.close()


# Copy License
# ----------------------------------------------
for file_ in ['OFL.txt', 'FONTLOG.txt']:
    shutil.copy(p.join(libertinus, file_), p.join(dir_, file_))
    shutil.copy(p.join(libertinus, file_), p.join(subdir, file_))
