from dataclasses import dataclass
from typing import List

from jinja2 import Template
from pydantic import BaseModel


@dataclass
class Prompt:
    template: Template
    kwargs: dict


@dataclass
class Category(BaseModel):
    name: str
    categories: List[str]
    prompt: Prompt
