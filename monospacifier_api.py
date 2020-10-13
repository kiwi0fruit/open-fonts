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
import os.path as p
sys.path.insert(0, p.join(p.dirname(p.abspath(__file__)), 'monospacifier'))
import monospacifier as m
import unicodedata


class Args:
    def __init__(self, inputs, references, save_to, merge, copy_metrics, renames):
        self.inputs = inputs
        self.references = references
        self.save_to = save_to
        self.merge = merge
        self.copy_metrics = copy_metrics
        self.rename = renames


def needs_scaling(self, glyph):
    uni = glyph.unicode
    def _unichr(u):
        try:
            return unichr(u)
        except Exception:
            return chr(u)
    category = unicodedata.category(_unichr(uni)) if (uni >= 0) and (uni <= sys.maxunicode) else None
    return glyph.width > 0 and category not in ['Mn', 'Mc', 'Me']

m.GlyphScaler.needs_scaling = needs_scaling


def monospacifier(inputs, references, save_to=".", merge=False, copy_metrics=False, renames=()):
    """
    Parameters
    ----------
    inputs : Union[list, str]
        Variable-width fonts to monospacify.
    references : Union[list, str]
        Reference monospace fonts. The metrics (character width, ...) of the newly created monospace fonts are inherited from these.
    save_to : str
        Where to save the newly generated monospace fonts. Defaults to current directory.
    merge : bool
        Whether to create copies of the reference font, extended with monospacified glyphs of the inputs.
    copy_metrics : bool
        Whether to apply the metrics of the reference font to the new font.
    renames : Tuple[Tuple[str, str]]
        Like: (('STIX', 'ST1X'),)
    """
    def parse_arguments():
        return Args(inputs, references, save_to, merge, copy_metrics, renames)

    m.parse_arguments = parse_arguments
    m.main()
