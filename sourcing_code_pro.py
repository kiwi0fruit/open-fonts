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
sourcecodepro = p.join(here, 'Fonts', 'SourceCodePro')

merge = False
copy_metrics = True
remove = (
    u'∕',
    # bad controls:
    u'\u000B', u'\u000C', u'\u001C', u'\u001D', u'\u001E', u'\u001F', u'\u0085',
    # u' ', u' ',  # controls that are OK
    # bad whitespaces u'\u1680', u'\u205F', u'\u3000':
    u' ', u' ', u'　',
    # bad whitespaces:
    # u'\u2000', u'\u2001', u'\u2002', u'2003', u'\u2004', u'\u2005', u'\u2006', u'\u2009', u'\u200A':
    u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ',
    # bas dashes u'\u00AD', u'\u1806', u'\uFE63', u'\uFF0D':
    u'­', u'᠆', u'﹣', u'－',
    # u'⸺', u'⸻',  # dashes that are OK: u'\u2E3A', u'\u2E3B'
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
    # ('SourceCodePro-LightIt', 'Source Code Pro Light', 'Italic'),
    # ('SourceCodePro-ExtraLightIt', 'Source Code Pro ExtraLight', 'Italic'),
    ('SourceCodePro-Regular', 'Source Code Pro', 'Regular'),
    ('SourceCodePro-Medium', 'Source Code Pro Medium', 'Regular'),
    ('SourceCodePro-Semibold', 'Source Code Pro Semibold', 'Regular'),
    ('SourceCodePro-Bold', 'Source Code Pro', 'Bold'),
    ('SourceCodePro-Black', 'Source Code Pro Black', 'Regular'),
    # ('SourceCodePro-Light', 'Source Code Pro Light', 'Regular'),
    # ('SourceCodePro-ExtraLight', 'Source Code Pro ExtraLight', 'Regular'),
]
shutil.copy(p.join(sourcecodepro, 'LICENSE.txt'), p.join(dir_, 'LICENSE.txt'))


reps = (('Source is a trademark', 'xxyyzz'), ('Source Code Pro', 'Sourcing Code Pro'), ('SourceCodePro', 'SourcingCodePro'), ('xxyyzz', 'Source is a trademark'))
def rep(s): return s.replace('Source', 'Sourcing')

for fn, ff, style in styles:
    clean_up=False
    ref = p.join(sourcecodepro, fn + '.ttf')
    of = ref  # Old Font

    rename_font(input=of, save_as=p.join(dir_, rep(fn).replace('It', 'Italic') +'.ttf'),
                fontname=rep(fn),  # Font Name
                familyname=rep(ff),  # Font Family
                fullname=rep(ff) + ((' ' + style) if style != 'Regular' else ''),
                reps=reps, sfnt_ref=ref, clean_up=clean_up, mono=True, remove=remove)
