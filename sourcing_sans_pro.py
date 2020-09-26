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

dir_ = p.join(repos, '_SourceSansPro')
if not p.exists(dir_):
    os.makedirs(dir_)


# Rename Source Sans 3:
# ---------------------------------
styles = [
    ('SourceSans3-Black', 'Source Sans 3 Black', 'Regular'),
    ('SourceSans3-BlackIt', 'Source Sans 3 Black', 'Italic'),
    ('SourceSans3-Bold', 'Source Sans 3', 'Bold'),
    ('SourceSans3-BoldIt', 'Source Sans 3', 'Bold Italic'),
    ('SourceSans3-ExtraLight', 'Source Sans 3 ExtraLight', 'Regular'),
    ('SourceSans3-ExtraLightIt', 'Source Sans 3 ExtraLight', 'Italic'),
    ('SourceSans3-It', 'Source Sans 3', 'Italic'),
    ('SourceSans3-Light', 'Source Sans 3 Light', 'Regular'),
    ('SourceSans3-LightIt', 'Source Sans 3 Light', 'Italic'),
    ('SourceSans3-Regular', 'Source Sans 3', 'Regular'),
    ('SourceSans3-SemiBold', 'Source Sans 3 SemiBold', 'Regular'),
    ('SourceSans3-SemiBoldIt', 'Source Sans 3 SemiBold', 'Italic'),
]
shutil.copy(p.join(sourcesanspro, 'LICENSE.md'), p.join(dir_, 'LICENSE.md'))


reps = (('Source is a trademark', 'xxyyzz'), ('Source Sans 3', 'Sourcing Sans Pro'), ('SourceSans3', 'SourcingSansPro'), ('xxyyzz', 'Source is a trademark'))
def rep(s): return s.replace('Source', 'Sourcing').replace('3', 'Pro')

for fn, ff, style in styles:
    clean_up = False
    ref = p.join(sourcesanspro, fn + '.ttf')
    of = ref  # Old Font

    rename_font(input=of, save_as=p.join(dir_, rep(fn) +'.ttf'),
                fontname=rep(fn),  # Font Name
                familyname=rep(ff),  # Font Family
                fullname=rep(ff) + ((' ' + style) if style != 'Regular' else ''),
                reps=reps, sfnt_ref=ref, clean_up=clean_up)


for fl in [
    'SourceSansPro-Black',
    'SourceSansPro-BlackIt',
    'SourceSansPro-Bold',
    'SourceSansPro-BoldIt',
    'SourceSansPro-ExtraLight',
    'SourceSansPro-ExtraLightIt',
    'SourceSansPro-It',
    'SourceSansPro-Light',
    'SourceSansPro-LightIt',
    'SourceSansPro-Regular',
    'SourceSansPro-SemiBold',
    'SourceSansPro-SemiBoldIt',
]:
    shutil.copy(p.join(sourcesanspro, fl + '.ttf'), p.join(dir_, fl + '.ttf'))
