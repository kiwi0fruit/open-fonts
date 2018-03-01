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
from os.path import join

repos = os.path.normpath(join(os.getcwd(), '../'))
googlefonts = join(repos, 'fonts')

robotomono = join(googlefonts, 'apache', 'robotomono')
refs = [join(robotomono, 'RobotoMono-Regular.ttf')]
merge = False
copy_metrics = True  # copy metrics


# Monospacify Roboto Mono:
# ------------------------
dir_ = join(repos, 'monospacified')
if not os.path.exists(dir_):
    os.makedirs(dir_)


def cat(string):
    return string.replace(' ', '')

styles = [
    ('RobotoMono-BoldItalic', 'Roboto Mono', 'Bold Italic'),
    ('RobotoMono-Italic', 'Roboto Mono', 'Italic'),
    # ('RobotoMono-LightItalic', 'Roboto Mono Light', 'Italic'),
    # ('RobotoMono-MediumItalic', 'Roboto Mono Medium', 'Italic'),
    # ('RobotoMono-ThinItalic', 'Roboto Mono Thin', 'Italic'),
]
fonts = [join(robotomono, fn +'.ttf') for fn, ff, st in styles]
monospacifier(fonts, refs, dir_, merge, copy_metrics)


# Rename monospacified Roboto Mono:
# ---------------------------------
for fn, ff, style in styles:
    ofn = fn + '_monospacified_for_RobotoMono.ttf'  # Old Font Name
    fn = fn.replace('Roboto', 'Open')  # Font Name
    ff = ff.replace('Roboto', 'Open')  # Font Family
    rename_font(join(dir_, ofn), join(dir_, fn +'.ttf'),
                fn,  ff,  ff +' '+ style,
                clean_up=True)

styles = [
    ('RobotoMono-Bold', 'Roboto Mono', 'Bold'),
    ('RobotoMono-Regular', 'Roboto Mono', 'Regular'),
    # ('RobotoMono-Light', 'Roboto Mono Light', 'Regular'),
    # ('RobotoMono-Medium', 'Roboto Mono Medium', 'Regular'),
    # ('RobotoMono-Thin', 'Roboto Mono Thin', 'Regular'),
]
for fn, ff, style in styles:
    ofn = fn + '.ttf'
    fn = fn.replace('Roboto', 'Open')
    ff = ff.replace('Roboto', 'Open')
    rename_font(join(robotomono, ofn), join(dir_, fn +'.ttf'),
                fn,  ff,  ff + (' '+ style if style != 'Regular' else ''),
                clean_up=False)


# Do not forget to replace BoldItalic with Bold Italic manually in Open Mono Bold Italic!
# ---------------------------------


"""
# Monospacify STIX Two Math, Symbola, Noto Sans Symbols:
# ------------------------------------------------------
fonts = [
    join('Fonts', 'STIX2Math.otf'),
    join('Fonts', 'Symbola.ttf'),
    join('Fonts', 'NotoSansSymbols-Regular.ttf'),
    join('Fonts', 'NotoSansSymbols2-Regular.ttf'),
    join('Fonts', 'texgyreschola-math.otf'),
]
monospacifier(fonts, refs, dir_, merge, copy_metrics)


# Rename monospacified STIX Two Math, Symbola, Noto Sans Symbols:
# ---------------------------------------------------------------
fonts = [
    'STIX Two Math',
    'Symbola',
    'Noto Sans Symbols',
    'Noto Sans Symbols2',
    'TeX Gyre Schola Math',
]
for font in fonts:
    ofn = cat(font) +'_monospacified_for_RobotoMono.ttf'
    fn = cat(font) +'ForRobotoMono'
    ff = font +' For Roboto Mono'
    rename_font(join(dir_, ofn), join(dir_, fn +'.sfd'),
                fn,  ff,  ff,
                clean_up=True)


# Monospacify Open Sans:
# ----------------------
styles = [
    ('OpenSans-Bold', 'Open Sans', 'Bold'),
    ('OpenSans-BoldItalic', 'Open Sans', 'Bold Italic'),
    ('OpenSans-Italic', 'Open Sans', 'Italic'),
    ('OpenSans-Regular', 'Open Sans', 'Regular'),
    # ('OpenSans-ExtraBold', 'Open Sans ExtraBold', ''),
    # ('OpenSans-ExtraBoldItalic', 'Open Sans ExtraBold', 'Italic'),
    # ('OpenSans-Light', 'Open Sans Light', ''),
    # ('OpenSans-LightItalic', 'Open Sans Light', 'Italic'),
    # ('OpenSans-SemiBold', 'Open Sans SemiBold', ''),
    # ('OpenSans-SemiBoldItalic', 'Open Sans SemiBold', ''),
]
fonts = [join(googlefonts, 'apache', 'opensans', fn +'.ttf') for fn, ff, st in styles]
monospacifier(fonts, refs, dir_, merge, copy_metrics)


# Rename monospacified Open Sans:
# -------------------------------
for fn, ff, style in styles:
    ofn = (fn if fn != 'OpenSans-Regular' else 'OpenSans') + '_monospacified_for_RobotoMono.ttf'
    fn = fn.replace('OpenSans', 'OpenSansForRobotoMono')
    ff = ff.replace('Open Sans', 'Open Sans For Roboto Mono')
    rename_font(join(dir_, ofn), join(dir_, fn +'.sfd'),
                fn,  ff,  ff + (' '+ style if style != '' else ''),
                clean_up=True)
"""