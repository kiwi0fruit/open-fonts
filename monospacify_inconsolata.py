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

from monospacifier_api import monospacifier
from helper import rename_font
import os
import shutil
from os import path as p

here = p.dirname(p.abspath(__file__))
repos = p.dirname(here)
inconsolata = p.join(here, 'Fonts', 'Inconsolata', 'Inconsolata')

merge = False
copy_metrics = True
remove = (
    # ---- Bad dashes: ----
    # [\u1806 \uFE63 \uFF0D \u00AD]
    u'᠆',  u'﹣', u'－', u'­',
    # ---- OK dashes: ----
    # [u2E3A \u2E3B] (multiple of character width)
    # u'⸺', u'⸻',
)
spaces = (
    # ---- Bad whitespaces (dont't touch): ----
    # [\u1680]
    u' ',
    # ---- Bad whitespaces: ----
    # [\u202F \u205F \u3000]
    u' ', u' ', u'　',
)

dir_ = p.join(repos, '_Inconsolatos')
if not p.exists(dir_):
    os.makedirs(dir_)

refs = [p.join(p.dirname(inconsolata), 'InconsolataLGC-Regular.sfd')]


# Monospacify Inconsolata:
# ------------------------
styles = [
    ('Inconsolata-Regular', 'Inconsolata', 'Regular'),
    ('Inconsolata-Bold', 'Inconsolata', 'Bold'),
]
fonts = [p.join(inconsolata, fn +'.ttf') for fn, ff, st in styles]
monospacifier(fonts, refs, dir_, merge, copy_metrics)
shutil.copy(p.join(inconsolata, 'OFL.txt'), p.join(dir_, 'OFL.txt'))


# Rename monospacified Inconsolata to Inconsolatos (temporal name):
# ---------------------------------
reps = (('Inconsolata', 'Inconsolatos'),)
def rep(s): return s.replace('Inconsolata', 'Inconsolatos')

for fn, ff, style in styles:
    clean_up = True
    ref = p.join(inconsolata, fn + '.ttf')
    of = p.join(dir_, (fn if fn != 'Inconsolata-Regular' else 'Inconsolata') + '_monospacified_for_InconsolataLGC.ttf')  # Old Font

    rename_font(input=of, save_as=p.join(dir_, rep(fn) +'.ttf'),
                fontname=rep(fn),  # Font Name
                familyname=rep(ff),  # Font Family
                fullname=rep(ff) + ((' ' + style) if style != 'Regular' else ''),
                reps=reps, sfnt_ref=ref, clean_up=clean_up, mono=True, remove=remove, spaces=spaces)
