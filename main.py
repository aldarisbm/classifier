from category import Prompt
from config import settings


def main():
    print(settings.llm_model_path)

    prompt = Prompt(
        "./prompt_templates",
        "intent.j2",
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
            few_shots=[
                dict(
                    prompt="What are the latest trends on silicone chip technology?",
                    response="{\"response\": \"Technology\"}"
                ),
                dict(
                    prompt="What kind of new harvesting technology is available? Has there been any new breakthroughs?",
                    response="{\"response\": \"Agriculture\"}"
                ),
                dict(
                    prompt="What kind of new software development tools are there? Are there any interesting trends in AI?",
                    response="{\"response\": \"Technology\"}"
                ),
                dict(
                    prompt="What are some recent advancements in gene editing? Are there any new drugs in development for cancer treatment?",
                    response="{\"response\": \"Healthcare\"}"
                ),
                dict(
                    prompt="What are the new regulations for cryptocurrency? How is the stock market performing?",
                    response="{\"response\": \"Finance\"}"
                ),
                dict(
                    prompt="What are the challenges of automating car assembly lines? How can manufacturers improve supply chain efficiency?",
                    response="{\"response\": \"Manufacturing\"}"
                ),
                dict(
                    prompt="What are some effective omnichannel marketing strategies? How can e-commerce businesses improve customer experience?",
                    response="{\"response\": \"Retail\"}"
                ),
                dict(
                    prompt="What are some new developments in educational technology? How can we improve online learning platforms?",
                    response="{\"response\": \"Education\"}"
                ),
                dict(
                    prompt="What are the benefits of solar energy? How can we achieve energy independence?",
                    response="{\"response\": \"Energy\"}"
                ),
                dict(
                    prompt="How can we improve public transportation systems? What are some new initiatives in urban planning?",
                    response="{\"response\": \"Government & Public Administration\"}"
                ),
                dict(
                    prompt="What are some new technologies used in precision agriculture? How can we improve farm efficiency?",
                    response="{\"response\": \"Agriculture\"}"
                ),
            ],
            query="What is the fastest growing tech startup?",
        )
    )

    print(prompt.get_prompt())


if __name__ == '__main__':
    main()
