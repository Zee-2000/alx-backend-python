#!/usr/bin/python3
from typing import Sequence, Tuple, Iterable, List

"""Re weite the function"""

def elemrnt_length(lst:Iterable[Sequence])->List[Tuple[Sequence, int]]:
    return [(x,len(x))for x in lst]