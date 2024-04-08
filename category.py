from dataclasses import dataclass
from typing import List

from jinja2 import Template, Environment, FileSystemLoader
from pydantic import BaseModel


@dataclass
class Prompt:
    template_path: str
    template_args: dict

    def load_template(template: str) -> Template:
        environment: Environment = Environment(loader=FileSystemLoader("prompt_templates/"))
        ptpl: Template = environment.get_template(f"{template}.j2")
        return ptpl


@dataclass
class Category(BaseModel):
    name: str
    categories: List[str]
    prompt: Prompt
