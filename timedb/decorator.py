from __future__ import annotations

import typing as t

FuncT = t.Callable[[str], t.Coroutine[t.Any, t.Any, None]]

def set_name(name: str) -> t.Callable[[FuncT], FuncT]:
  
  
  def decorator(func: FuncT) -> FuncT:
    return func
  
  return decorator


