#!/usr/bin/env python3
from typing import Callable
"""make multiplier"""

def make_multiplier(multiplier:float)-> Callable[[float], float]:
    return lambda n:n*multiplier