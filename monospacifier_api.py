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
import monospacifier as m


class Args:
    def __init__(self, references, inputs, save_to, merge, copy_metrics, renames):
        self.references = references
        self.inputs = inputs
        self.save_to = save_to
        self.merge = merge
        self.copy_metrics = copy_metrics
        self.rename = renames


def monospacifier(inputs, references, save_to=".", merge=False, copy_metrics=False, renames=(('STIX', 'ST1X'),)):
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
    """
    def parse_arguments():
        return Args(references, inputs, save_to, merge, copy_metrics, renames)

    m.parse_arguments = parse_arguments
    m.main()
