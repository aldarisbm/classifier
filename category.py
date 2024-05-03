from enum import Enum
from typing import List, Dict

from pydantic import BaseModel


class ClassifyType(Enum):
    SINGLE = "single"
    MULTI = "multi"


class Category(BaseModel):
    category: str
    labels: List[str]
    few_shots: List[Dict]
    classify_type: ClassifyType

    class Config:
        arbitrary_types_allowed = True
        validate_assignment = True


class Industry(Category):
    pass
