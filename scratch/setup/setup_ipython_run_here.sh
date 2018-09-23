#!/bin/bash
 
 rm -f ~/.ipython/profile_default/startup/ipython_default_startup.py
 ln -s ${PWD}/ipython_default_startup.py ~/.ipython/profile_default/startup/ipython_default_startup.py