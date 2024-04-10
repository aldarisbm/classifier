from dataclasses import dataclass
from typing import Optional

from jinja2 import Template, Environment, FileSystemLoader


@dataclass
class PromptTemplate:
    _template_path: str
    _template_name: str
    _template_args: dict
    _tpl: Optional[Template] = None

    def __post_init__(self):
        self._load_template()

    def _load_template(self) -> None:
        environment: Environment = Environment(loader=FileSystemLoader(f"{self._template_path}/"))
        self._tpl = environment.get_template(f"{self._template_name}")

    def get_prompt(self, query: str) -> str:
        self._template_args['query'] = query
        return self._tpl.render(**self._template_args)
