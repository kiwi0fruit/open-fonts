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
from monospacifier_api import monospacifier
from helper import rename_font
import os
import shutil
from os import path as p

here = p.dirname(p.abspath(__file__))
repos = p.dirname(here)
inconsolata = p.join(repos, 'Inconsolata-LGC')

merge = False
copy_metrics = True
remove = (
    # ---- Bad dashes: ----
    # [\u00AD \u1806 \uFE63 \uFF0D]
    u'­', u'᠆',  u'﹣', u'－',
    # ---- OK dashes: ----
    # [u2E3A \u2E3B] (multiple of character width)
    # u'⸺', u'⸻',
)
spaces = (
    # ---- OK whitespaces: ----
    # [\u202F]
    # u' ',
    # ---- Bad whitespaces: ----
    # [\u1680 \u205F \u3000]
    u' ', u' ', u'　',
    # ---- Bad whitespaces: ----
    # [\u2000 \u2001 \u2002 \u2003 \u2004 \u2005 \u2006 \u2009 \u200A]
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ',
)

# TODO: test which whitespaces are good.
# Check if there's a replacement mode that replaces references.
# Check for other "a"-like and "д"-like characters.

dir_ = p.join(repos, '_InconsolataSugar')
if not p.exists(dir_):
    os.makedirs(dir_)


# Rename Source Code Pro:
# ---------------------------------
styles = [
    ('Inconsolata-LGC-Italic', 'Inconsolata LGC', 'Italic'),
    ('Inconsolata-LGC-BoldItalic', 'Inconsolata LGC', 'Bold Italic'),
    ('Inconsolata-LGC', 'Inconsolata LGC', 'Regular'),
    ('Inconsolata-LGC-Bold', 'Inconsolata LGC', 'Bold'),
]
shutil.copy(p.join(inconsolata, 'LICENSE'), p.join(dir_, 'LICENSE.txt'))


reps = (('Inconsolata LGC', 'Inconsolata Sugar'), ('InconsolataLGC', 'InconsolataSugar'))
def rep(s): return s.replace('LGC', 'Sugar')

for fn, ff, style in styles:
    clean_up=False
    ref = p.join(inconsolata, fn + '.sfd')
    of = ref  # Old Font

    rename_font(input=of, save_as=p.join(dir_, rep(fn) +'.ttf'),
                fontname=rep(fn),  # Font Name
                familyname=rep(ff),  # Font Family
                fullname=rep(ff) + ((' ' + style) if style != 'Regular' else ''),
                reps=reps, sfnt_ref=ref, clean_up=clean_up, mono=True, remove=remove, spaces=spaces)
