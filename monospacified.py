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
consolas_refs = [p.expandvars("%WINDIR%\Fonts\consola.ttf") if (os.name == "nt") else "consola.ttf"]
shutil.copy(p.join(dejavu, 'LICENSE'), p.join(dir_, 'DejaVu_Sans_Mono_LICENSE.txt'))

styles = [
    ('DejaVuSansMono', 'DejaVu Sans Mono', 'Regular'),
    ('DejaVuSansMono-Oblique', 'DejaVu Sans Mono', 'Oblique'),
    ('DejaVuSansMono-Bold', 'DejaVu Sans Mono', 'Bold'),
    ('DejaVuSansMono-BoldOblique', 'DejaVu Sans Mono', 'Bold Oblique'),
]
fonts = [p.join(dejavu, fn +'.ttf') for fn, ff, st in styles]
monospacifier(fonts, consolas_refs, save_to=dir_, merge=merge, copy_metrics=copy_metrics)

reps = (('DejaVu Sans Mono', 'DejaVu Sans Mono For Conso1as'), ('DejaVuSansMono', 'DejaVuSansMonoForConso1as'))
def rep(s): return s.replace('DejaVu Sans Mono', 'DejaVu Sans Mono For Conso1as').replace('DejaVuSansMono', 'DejaVuSansMonoForConso1as')

for fn, ff, style in styles:
    clean_up = True
    ref = p.join(dejavu, fn + '.ttf')
    of = p.join(dir_, fn + '_monospacified_for_Consolas.ttf')  # Old Font

    rename_font(input=of, save_as=p.join(dir_, rep(fn) +'.ttf'),
                fontname=rep(fn),  # Font Name
                familyname=rep(ff),  # Font Family
                fullname=rep(ff) + ((' ' + style) if style != 'Regular' else ''),
                reps=reps, sfnt_ref=ref, clean_up=clean_up, mono=True)


# Monospacify Symbola and STIX Two Math for Consolas and Roboto Mono:
# -------------------------------------------------------------------
robotomono_refs = [p.join(repos, 'fonts', 'apache', 'robotomono', 'RobotoMono-Regular.ttf')]
symbola = p.join(here, 'Fonts', 'hintedSymbola.ttf')
stix = p.join(repos, 'stixfonts', 'OTF', 'STIX2Math.otf')

shutil.copy(p.join(here, 'Fonts', 'Symbola-PublicDomain.odt'), p.join(dir_, 'Symbola-PublicDomain.odt'))
shutil.copy(p.join(here, 'Fonts', 'STIXTwo-OFL.txt'), p.join(dir_, 'STIXTwo-OFL.txt'))
shutil.copy(p.join(repos, 'stixfonts', 'docs', 'STIX_2.0.0_release_notes.txt'), p.join(dir_, 'STIX_2.0.0_release_notes.txt'))

monospacifier([symbola, stix], consolas_refs, save_to=dir_, merge=merge, copy_metrics=copy_metrics)
monospacifier([symbola, stix], robotomono_refs, save_to=dir_, merge=merge, copy_metrics=copy_metrics)


def rep(s):
    return s.replace('Roboto', 'Robot0').replace('Consolas', 'Conso1as').replace('STIX', 'ST1X')


def rep2(s, _reps):
    for _from, _to in _reps:
        s = s.replace(_from, _to)
    return s


for mono_ref in ('Consolas', 'Roboto Mono'):
    monoRef = mono_ref.replace(' ', '')

    reps = (
        ('STIX Two Math', 'ST1X Two Math For ' + rep(mono_ref)),
        ('STIXTwoMath', 'ST1XTwoMathFor' + rep(monoRef)),
        ('Symbola', 'Symbola For ' + rep(mono_ref)),
        # ('STIX Two ', 'ST1X Two'),
        # ('STIXTwo', 'ST1XTwo'),
        # ('STIPub:', 'ST1Pub:'),
        # ('(TM)', '(TM)__this_statement_is_void_but_still_may_be_true__'),
    )

    for ofn, ref in (('STIX Two Math', stix), ('Symbola', symbola)):  # Original Font Name
        clean_up = True

        of = p.join(dir_, ofn.replace(' ', '') + '_monospacified_for_' + monoRef + '.ttf')  # Old Font
        ff = rep2(ofn, reps)
        fn = ff.replace(' ', '')

        rename_font(input=of, save_as=p.join(dir_, rep(fn) +'.ttf'),
                    fontname=rep(fn),  # Font Name
                    familyname=rep(ff),  # Font Family
                    fullname=rep(ff) + ((' ' + style) if style != 'Regular' else ''),
                    reps=reps, sfnt_ref=ref, clean_up=clean_up, mono=True)
