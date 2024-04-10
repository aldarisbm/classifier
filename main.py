import few_shots
from config import settings
from llm import ClassifierLlm
from prompt import PromptTemplate


def main():
    print(settings.llm_model_path)

    prompt_template = PromptTemplate(
        "./prompt_templates",
        "classifier.j2",
        dict(
            category="Industry",
            categories=[
                "Technology",
                "Healthcare",
                "Finance",
                "Manufacturing",
                "Retail",
                "Education",
                "Energy",
                "Agriculture"
            ],
            few_shots=few_shots.industry,
        )
    )

    llm = ClassifierLlm(
        settings.llm_model_path,
        settings.grammar_file_path,
        prompt_template
    )

    res = llm.inference("What are the main problems in school right now")
    print(res)


if __name__ == '__main__':
    main()
