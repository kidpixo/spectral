#########################################################################
#
#   Spectral/__init__.py - This file is part of the Spectral Python (SPy)
#   package.
#
#   Copyright (C) 2001-2008 Thomas Boggs
#
#   Spectral Python is free software; you can redistribute it and/
#   or modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation; either version 2
#   of the License, or (at your option) any later version.
#
#   Spectral Python is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#     
#   You should have received a copy of the GNU General Public License
#   along with this software; if not, write to
#
#               Free Software Foundation, Inc.
#               59 Temple Place, Suite 330
#               Boston, MA 02111-1307
#               USA
#
#########################################################################
#
# Send comments to:
# Thomas Boggs, tboggs@users.sourceforge.net
#

__version__ = '0.5'
byteOrder = 0   # little endian

BSQ = 0
BIL = 1
BIP = 2

#from numpy import *
from Spectral import image, loadTrainingSets, saveTrainingSets, settings, tileImage, spyColors
from Io import *
from Algorithms import *
from Graphics import *
#from Io.Aviris import openAviris

import Utilities.Status
status = Utilities.Status.StatusDisplay()
