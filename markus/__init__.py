# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from markus.main import get_metrics  # noqa

INCR = 'incr'
GAUGE = 'gauge'
TIMING = 'timing'
HISTOGRAM = 'histogram'

__all__ = ['get_metrics', 'INCR', 'GAUGE', 'TIMING', 'HISTOGRAM']

__author__ = 'Will Kahn-Greene'
__email__ = 'willkg@mozilla.com'

# yyyymmdd
__releasedate__ = ''
# x.y or x.y.dev0
__version__ = '0.1.dev0'
