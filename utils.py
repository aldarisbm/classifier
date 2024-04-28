from typing import List

from jinja2 import Environment, FileSystemLoader
from llama_cpp import LlamaGrammar


def get_grammar_from_template(template: str, labels: List[str]) -> LlamaGrammar:
    environment: Environment = Environment(loader=FileSystemLoader("grammar_templates/"))
    template = environment.get_template(template)
    return LlamaGrammar.from_string(
        template.render(
            labels=labels
        )
    )
