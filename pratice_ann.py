#!/usr/bin/env python3

from typing import  List, Union, Tuple,  Optional, Dict, get_type_hints
"""
def my_test_function(a: int, b: List[str]) -> Tuple[float, Optional[int]]:
    output: float = a * 3.1
    output1: Optional[int] = None if len(b) == 0 else len(b)
    return output, output1
result = my_test_function(5, ["hello", "world"])
print(result)

from typing import List, Tuple

def myfunc(a: int, b: List[str]) -> Tuple[float, int]:
    output: float = b *1.5
    output1: int = len(b)
    return output,   output1
print(myfunc.__annotations__)
"""

def g_func(s: int, f: List[str]) -> Tuple[float, int]:
    output: float = a * 6.1
    output1: int = len(b)
    return output, output1
our_hints = get_type_hints(g_func)
print(our_hints)
