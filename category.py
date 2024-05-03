from typing import List, Dict

from pydantic import BaseModel


class Category(BaseModel):
    category: str
    labels: List[str]
    few_shots: List[Dict]
    classify_type: str

    class Config:
        arbitrary_types_allowed = True
        validate_assignment = True


class Industry(Category):
    pass
