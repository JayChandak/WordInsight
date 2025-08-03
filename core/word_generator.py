# core/word_generator.py
from core.llm_client import get_words_from_groq

def get_category_words(category: str) -> list[dict]:
    raw_output = get_words_from_groq(category)

    # Handle error
    if raw_output.startswith("Error:"):
        return [{"word": "Error", "definition": raw_output}]

    lines = [line.strip("-• ") for line in raw_output.split("\n") if line.strip()]
    words_data = []

    for line in lines[:11]:
        if ":" in line:
            word, definition = line.split(":", 1)
            words_data.append({"word": word.strip(), "definition": definition.strip()})
        else:
            words_data.append({"word": line.strip(), "definition": ""})

    # Pad to 10 if fewer
    while len(words_data) < 10:
        words_data.append({"word": f"Extra_{len(words_data)+1}", "definition": "No definition"})

    return words_data
