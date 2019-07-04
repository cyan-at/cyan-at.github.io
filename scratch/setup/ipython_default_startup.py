#!/usr/bin/env python

# USAGE: symlink wherever this file lives to:
# ~/.ipython/profile_default/startup/ipython_default_startup.py

import numpy as np
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

print "hello from your custom ipython_default_startup.py"
import os
print os.path.dirname(os.path.abspath(__file__))

import math
import cPickle as pickle