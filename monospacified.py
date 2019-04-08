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
dejavu = p.join(here, 'Fonts', 'DejaVu')

merge = False
copy_metrics = True

dir_ = p.join(repos, '_monospacified')
if not p.exists(dir_):
    os.makedirs(dir_)


# Monospacify DejaVu Sans Mono for Consolas:
# ------------------------------------------
refs = [p.expandvars("%WINDIR%\Fonts\consola.ttf") if (os.name == "nt") else "consola.ttf"]
shutil.copy(p.join(dejavu, 'LICENSE'), p.join(dir_, 'DejaVu_Sans_Mono_LICENSE.txt'))

styles = [
    ('DejaVuSansMono', 'DejaVu Sans Mono', 'Regular'),
    ('DejaVuSansMono-Oblique', 'DejaVu Sans Mono', 'Oblique'),
    ('DejaVuSansMono-Bold', 'DejaVu Sans Mono', 'Bold'),
    ('DejaVuSansMono-BoldOblique', 'DejaVu Sans Mono', 'Bold Oblique'),
]
fonts = [p.join(dejavu, fn +'.ttf') for fn, ff, st in styles]
monospacifier(fonts, refs, save_to=dir_, merge=merge, copy_metrics=copy_metrics)

reps = (('Mono', 'MonoForConso1as'),)
def rep(s): return s.replace('Mono', 'MonoForConso1as')

for fn, ff, style in styles:
    clean_up = True
    ref = p.join(dejavu, fn + '.ttf')
    of = p.join(dir_, fn + '_monospacified_for_Consolas.ttf')  # Old Font

    rename_font(input=of, save_as=p.join(dir_, rep(fn) +'.ttf'),
                fontname=rep(fn),  # Font Name
                familyname=rep(ff),  # Font Family
                fullname=rep(ff) + ((' ' + style) if style != 'Regular' else ''),
                reps=reps, sfnt_ref=ref, clean_up=clean_up)
