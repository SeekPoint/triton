from typing import Tuple

import dataclasses
from pydebug import gd

@dataclasses.dataclass
class ExecutionContext:
    program_id: Tuple[int]
    program_size: Tuple[int]
