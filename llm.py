from typing import Optional

from llama_cpp import Llama, LlamaGrammar

from prompt import PromptTemplate


class ClassifierLlm:
    model_path: str
    grammar_path: str
    prompt: PromptTemplate

    _llama: Llama
    _grammar: Optional[LlamaGrammar] = None

    def __init__(self, model_path: str, grammar_path: str, prompt: PromptTemplate):
        self._llama = Llama(
            model_path=model_path,
            n_gpu_layers=-1,
            seed=0,
            use_mlock=True,
            n_ctx=4096,
            n_batch=256,
            verbose=False
        )
        self._grammar = LlamaGrammar.from_file(grammar_path)
        self.prompt = prompt

    def inference(self, query: str) -> str:
        rendered_prompt = self.prompt.get_prompt(query)
        return self._llama(
            rendered_prompt,
            grammar=self._grammar,
            temperature=0
        )['choices'][0]['text']
