#!/usr/bin/env python

import numpy as np
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

print "hello from jim's ipython_default_startup.py"

from wall_borg.interaction.utils import *
from wall_borg import dynamics as dyn
