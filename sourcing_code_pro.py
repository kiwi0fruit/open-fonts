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
sourcecodepro = p.join(here, 'Fonts', 'SourceCodePro')

remove = (
    u'∕',
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
    # ---- Bad whitespaces (dont't touch): ----
    # [\u1680]
    # u' ',
    # ---- Bad whitespaces: ----
    # [\u205F \u3000]
    u' ', u'　',
    # ---- Bad whitespaces: ----
    # [\u2000 \u2001 \u2002 \u2003 \u2004 \u2005 \u2006 \u2009 \u200A]
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ',
)

dir_ = p.join(repos, '_SourcingCodePro')
if not p.exists(dir_):
    os.makedirs(dir_)


# Rename Source Code Pro:
# ---------------------------------
styles = [
    ('SourceCodePro-It', 'Source Code Pro', 'Italic'),
    ('SourceCodePro-MediumIt', 'Source Code Pro Medium', 'Italic'),
    ('SourceCodePro-SemiboldIt', 'Source Code Pro Semibold', 'Italic'),
    ('SourceCodePro-BoldIt', 'Source Code Pro', 'Bold Italic'),
    ('SourceCodePro-BlackIt', 'Source Code Pro Black', 'Italic'),
    ('SourceCodePro-LightIt', 'Source Code Pro Light', 'Italic'),
    ('SourceCodePro-ExtraLightIt', 'Source Code Pro ExtraLight', 'Italic'),
    ('SourceCodePro-Regular', 'Source Code Pro', 'Regular'),
    ('SourceCodePro-Medium', 'Source Code Pro Medium', 'Regular'),
    ('SourceCodePro-Semibold', 'Source Code Pro Semibold', 'Regular'),
    ('SourceCodePro-Bold', 'Source Code Pro', 'Bold'),
    ('SourceCodePro-Black', 'Source Code Pro Black', 'Regular'),
    ('SourceCodePro-Light', 'Source Code Pro Light', 'Regular'),
    ('SourceCodePro-ExtraLight', 'Source Code Pro ExtraLight', 'Regular'),
]
shutil.copy(p.join(sourcecodepro, 'LICENSE.txt'), p.join(dir_, 'LICENSE.txt'))


reps = (('Source is a trademark', 'xxyyzz'), ('Source Code Pro', 'Sourcing Code Pro'), ('SourceCodePro', 'SourcingCodePro'), ('xxyyzz', 'Source is a trademark'))
def rep(s): return s.replace('Source', 'Sourcing')

for fn, ff, style in styles:
    clean_up = False
    ref = p.join(sourcecodepro, fn + '.ttf')
    of = ref  # Old Font

    rename_font(input=of, save_as=p.join(dir_, rep(fn).replace('It', 'Italic') +'.ttf'),
                fontname=rep(fn),  # Font Name
                familyname=rep(ff),  # Font Family
                fullname=rep(ff) + ((' ' + style) if style != 'Regular' else ''),
                reps=reps, sfnt_ref=ref, clean_up=clean_up, mono=True, remove=remove, spaces=spaces)
