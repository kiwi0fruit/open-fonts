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

import sys
import os
sys.path.insert(0, os.path.join(os.path.normpath(os.path.join(os.getcwd(), '../')), 'monospacifier'))
from monospacifier import *


def monospacifier(inputs, references, save_to=".", merge=False, copy_metrics=False):
    """
    Parameters
    ----------
    inputs: list of str
        Variable-width fonts to monospacify.
    references: list of str
        Reference monospace fonts. The metrics (character width, ...) of the newly created monospace fonts are inherited from these.
    save_to: str, default "."
        Where to save the newly generated monospace fonts. Defaults to current directory.
    merge: bool, default False
        Whether to create copies of the reference font, extended with monospacified glyphs of the inputs.
    copy_metrics: bool, default False
        Whether to apply the metrics of the reference font to the new font.
    """

    # del inputs[1:]
    # del references[1:]
    results = list(process_fonts(references, inputs, save_to, merge, copy_metrics))

    tabdata = {}
    for ref, fnt, ttf in results:
        tabdata.setdefault(u"**{}**".format(ref), []).append(u"[{}]({}?raw=true)".format(fnt, ttf))
    table = [(header, u", ".join(items)) for header, items in sorted(tabdata.items())]

    try:
        from tabulate import tabulate
        print(tabulate(table, headers=[u'Programming font', u'Monospacified fallback fonts'], tablefmt='pipe'))
    except ImportError:
        print("!!! tabulate package not available")
