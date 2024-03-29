import os

import openai

# You will need to get your API key from https://platform.openai.com/account/api-keys
openai.api_key = os.getenv("OPENAI_API_KEY")



# Got this function from this amazing course https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def summarise_news_stories(stories):
    """
    Takes in a list of news stories and prompts ChatGPT to
    generate a short summary of each story based on the provided
    Section, Subsection, Title, and Abstract.
    The function returns the summary generated by ChatGPT.

    Args:
    - stories (str): A list of news stories to be summarised.
    Each story should be a block of text with the following format
    where each part is on a newline:

    Section: the section
    Subsection: the subsection
    Title: the title
    Abstract: the Abstract

    The values for 'Subsection' and 'Abstract' can be empty
    strings if not applicable.

    Returns:
    - summary (str): A string containing the summary generated by ChatGPT
    for all the news stories.
    """

    print("Beginning summary")
    prompt = f"""
    Your task is to generate a short summary of a series of
    news stories given the Section, Subsection, Title and
    Abstract, of each story.

    The sections are after the 'Section:'.
    The subsections are after the 'Subsection:'. The subsections can be empty.

    The title is after the 'Title:'. The abstract is after the 'Abstract:'.
    The abstract can be empty.

    Summarise the stories below, delimited by triple backticks,
    in the style of an AI trying to convey information to humans.
    Please use paragraphs where appropriate and use at most 800 words.

    Stories: ```{stories}```
    """

    return get_completion(prompt)