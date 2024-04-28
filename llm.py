import logging
from typing import Optional

from llama_cpp import Llama, LlamaGrammar

from prompt import PromptTemplate


class ClassifierLlm:
    model_path: str
    grammar_path: str

    _prompt_template: PromptTemplate
    _llama: Llama
    _grammar: Optional[LlamaGrammar] = None

    def __init__(self, model_path: str, grammar: LlamaGrammar, prompt_template: PromptTemplate):
        self._llama = Llama(
            model_path=model_path,
            n_gpu_layers=-1,
            seed=0,
            use_mlock=True,
            n_ctx=4096,
            n_batch=256,
            verbose=False
        )
        self._grammar = grammar
        self._prompt_template = prompt_template

    def inference(self, query: str) -> str:
        rendered_prompt = self._prompt_template.get_prompt(query)
        logging.debug("rendered_prompt: %s", rendered_prompt)
        return self._llama(
            rendered_prompt,
            grammar=self._grammar,
            temperature=0
        )['choices'][0]['text']
