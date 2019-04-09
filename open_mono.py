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

robotomono = p.join(here, 'Fonts', 'RobotoMono')
merge = False
copy_metrics = True

dir_ = p.join(repos, '_OpenMono')
if not p.exists(dir_):
    os.makedirs(dir_)

refs = [p.join(robotomono, 'RobotoMono-Regular.ttf')]


# Monospacify Roboto Mono:
# ------------------------
styles = [
    ('RobotoMono-Italic', 'Roboto Mono', 'Italic'),
    ('RobotoMono-MediumItalic', 'Roboto Mono Medium', 'Italic'),
    ('RobotoMono-BoldItalic', 'Roboto Mono', 'Bold Italic'),
    # ('RobotoMono-LightItalic', 'Roboto Mono Light', 'Italic'),
    # ('RobotoMono-ThinItalic', 'Roboto Mono Thin', 'Italic'),
    ('RobotoMono-Regular', 'Roboto Mono', 'Regular'),
    ('RobotoMono-Medium', 'Roboto Mono Medium', 'Regular'),
    ('RobotoMono-Bold', 'Roboto Mono', 'Bold'),
    # ('RobotoMono-Light', 'Roboto Mono Light', 'Regular'),
    # ('RobotoMono-Thin', 'Roboto Mono Thin', 'Regular'),
]
fonts = [p.join(robotomono, fn +'.ttf') for fn, ff, st in styles]
monospacifier(fonts, refs, dir_, merge, copy_metrics)


# Rename monospacified Roboto Mono:
# ---------------------------------
reps = (('Roboto', 'Open'), ('Google', 'Google__this_statement_is_void_but_still_may_be_true__'))
def rep(s): return s.replace('Roboto', 'Open')

for fn, ff, style in styles:
    clean_up = True
    ref = p.join(robotomono, fn + '.ttf')
    of = p.join(dir_, (fn if fn != 'RobotoMono-Regular' else 'RobotoMono') + '_monospacified_for_RobotoMono.ttf')  # Old Font

    rename_font(input=of, save_as=p.join(dir_, rep(fn) +'.ttf'),
                fontname=rep(fn),  # Font Name
                familyname=rep(ff),  # Font Family
                fullname=rep(ff) + ((' ' + style) if style != 'Regular' else ''),
                reps=reps, sfnt_ref=ref, clean_up=clean_up)

styles2 = [
    # ('RobotoMono-Regular', 'Roboto Mono', 'Regular'),
    # ('RobotoMono-Medium', 'Roboto Mono Medium', 'Regular'),
    # ('RobotoMono-Bold', 'Roboto Mono', 'Bold'),
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
                fullname=rep(ff) + ((' ' + style) if style != 'Regular' else ''),
                reps=reps, sfnt_ref=ref, clean_up=clean_up)


# Set isFixedPitch flag:
# ---------------------------------
for fn, ff, style in styles:
    print(subprocess.check_output([os.environ['python3'], './setisFixedPitch-fonttools.py', p.join(dir_, rep(fn) +'.ttf')]))


# Other:
# ---------------------------------
shutil.copy(p.join(robotomono, 'LICENSE.txt'), p.join(dir_, 'fixed', 'LICENSE.txt'))
