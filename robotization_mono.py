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
robotomono = p.join(repos, 'fonts', 'apache', 'robotomono')
# robotomono = p.join(here, 'Fonts', 'RobotoMono')

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
    # ---- Bad whitespaces: ----
    # [\u1680 \u202F \u205F \u3000]
    u' ', u' ', u' ', u'　',
)

dir_ = p.join(repos, '_RobotizationMono')
if not p.exists(dir_):
    os.makedirs(dir_)

refs = [p.join(robotomono, 'RobotoMono-Regular.ttf')]
# refs = [p.join(dir_, 'RobotoMono-Regular.ttf')]
# shutil.copy(p.join(robotomono, 'RobotoMono-Regular.ttf'), refs[0])


# Monospacify Roboto Mono:
# ------------------------
styles = [
    ('RobotoMono-Italic', 'Roboto Mono', 'Italic'),
    ('RobotoMono-MediumItalic', 'Roboto Mono Medium', 'Italic'),
    ('RobotoMono-BoldItalic', 'Roboto Mono', 'Bold Italic'),
    # ('RobotoMono-LightItalic', 'Roboto Mono Light', 'Italic'),
    # ('RobotoMono-ThinItalic', 'Roboto Mono Thin', 'Italic'),
    # ('RobotoMono-Regular', 'Roboto Mono', 'Regular'),
    # ('RobotoMono-Medium', 'Roboto Mono Medium', 'Regular'),
    # ('RobotoMono-Bold', 'Roboto Mono', 'Bold'),
    # ('RobotoMono-Light', 'Roboto Mono Light', 'Regular'),
    # ('RobotoMono-Thin', 'Roboto Mono Thin', 'Regular'),
]
fonts = [p.join(robotomono, fn +'.ttf') for fn, ff, st in styles]
monospacifier(fonts, refs, dir_, merge, copy_metrics)
# os.remove(refs[0])
shutil.copy(p.join(robotomono, 'LICENSE.txt'), p.join(dir_, 'LICENSE.txt'))


# Rename monospacified Roboto Mono:
# ---------------------------------
reps = (('Roboto Mono is a trademark', 'xxyyzz'), ('Roboto Mono', 'Robotization Mono'), ('RobotoMono', 'RobotizationMono'), ('xxyyzz', 'Roboto Mono is a trademark'))
def rep(s): return s.replace('Roboto', 'Robotization')

for fn, ff, style in styles:
    clean_up = True
    ref = p.join(robotomono, fn + '.ttf')
    of = p.join(dir_, (fn if fn != 'RobotoMono-Regular' else 'RobotoMono') + '_monospacified_for_RobotoMono.ttf')  # Old Font

    rename_font(input=of, save_as=p.join(dir_, rep(fn) +'.ttf'),
                fontname=rep(fn),  # Font Name
                familyname=rep(ff),  # Font Family
                fullname=rep(ff) + ((' ' + style) if style != 'Regular' else ''),
                reps=reps, sfnt_ref=ref, clean_up=clean_up, mono=True, remove=remove, spaces=spaces)

styles2 = [
    ('RobotoMono-Regular', 'Roboto Mono', 'Regular'),
    ('RobotoMono-Medium', 'Roboto Mono Medium', 'Regular'),
    ('RobotoMono-Bold', 'Roboto Mono', 'Bold'),
    # ('RobotoMono-Light', 'Roboto Mono Light', 'Regular'),
    # ('RobotoMono-Thin', 'Roboto Mono Thin', 'Regular'),
]
for fn, ff, style in styles2:
    clean_up=False
    ref = p.join(robotomono, fn + '.ttf')
    of = ref  # Old Font

    rename_font(input=of, save_as=p.join(dir_, rep(fn) +'.ttf'),
                fontname=rep(fn),  # Font Name
                familyname=rep(ff),  # Font Family
                fullname=rep(ff) + ((' ' + style) if (style != 'Regular') else ''),
                reps=reps, sfnt_ref=ref, clean_up=clean_up, mono=True, remove=remove, spaces=spaces)
