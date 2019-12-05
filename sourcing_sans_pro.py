# -*- coding: utf-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
from helper import rename_font
import os
import shutil
from os import path as p

here = p.dirname(p.abspath(__file__))
repos = p.dirname(here)
sourcesanspro = p.join(here, 'Fonts', 'SourceSansPro')

dir_ = p.join(repos, '_SourcingSansPro')
if not p.exists(dir_):
    os.makedirs(dir_)


# Rename Source Sans Pro:
# ---------------------------------
styles = [
    ('SourceSansPro-Black', 'Source Sans Pro Black', 'Regular'),
    ('SourceSansPro-BlackItalic', 'Source Sans Pro Black', 'Italic'),
    ('SourceSansPro-Bold', 'Source Sans Pro', 'Bold'),
    ('SourceSansPro-BoldItalic', 'Source Sans Pro', 'Bold Italic'),
    ('SourceSansPro-ExtraLight', 'Source Sans Pro ExtraLight', 'Regular'),
    ('SourceSansPro-ExtraLightItalic', 'Source Sans Pro ExtraLight', 'Italic'),
    ('SourceSansPro-Italic', 'Source Sans Pro', 'Italic'),
    ('SourceSansPro-Light', 'Source Sans Pro Light', 'Regular'),
    ('SourceSansPro-LightItalic', 'Source Sans Pro Light', 'Italic'),
    ('SourceSansPro-Regular', 'Source Sans Pro', 'Regular'),
    ('SourceSansPro-SemiBold', 'Source Sans Pro SemiBold', 'Regular'),
    ('SourceSansPro-SemiBoldItalic', 'Source Sans Pro SemiBold', 'Italic'),
]
shutil.copy(p.join(sourcesanspro, 'LICENSE.txt'), p.join(dir_, 'LICENSE.txt'))


reps = (('Source is a trademark', 'xxyyzz'), ('Source Sans Pro', 'Sourcing Sans Pro'), ('SourceSansPro', 'SourcingSansPro'), ('xxyyzz', 'Source is a trademark'))
def rep(s): return s.replace('Source', 'Sourcing')

for fn, ff, style in styles:
    clean_up = False
    ref = p.join(sourcesanspro, fn + '.ttf')
    of = ref  # Old Font

    rename_font(input=of, save_as=p.join(dir_, rep(fn) +'.ttf'),
                fontname=rep(fn),  # Font Name
                familyname=rep(ff),  # Font Family
                fullname=rep(ff) + ((' ' + style) if style != 'Regular' else ''),
                reps=reps, sfnt_ref=ref, clean_up=clean_up)
