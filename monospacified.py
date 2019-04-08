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
import os
from os import path as p

repos = os.path.normpath(p.join(os.getcwd(), '../'))
merge = False
copy_metrics = True

dir_ = p.join(repos, 'monospacified')
if not os.path.exists(dir_):
    os.makedirs(dir_)


# Monospacify DejaVu Sans Mono:
# ---------------------------------
monospacifier([p.join('Fonts', 'DejaVuSansMono.ttf')],
              [p.expandvars("%WINDIR%\Fonts\consola.ttf") if (os.name == "nt") else "consola.ttf"],
              dir_, merge, copy_metrics)
