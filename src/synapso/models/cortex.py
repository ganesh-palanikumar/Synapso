from dataclasses import dataclass
from datetime import datetime


@dataclass
class Cortex:
    name: str
    path: str
    created_at: datetime
    is_favorite: bool
    n_files: int
