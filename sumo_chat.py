import os
import pandas as pd
import openai

DATA_FILE = "sumo_since_1957.csv"

class SumoChat:
    """Wrapper for querying OpenAI's ChatGPT about sumo wrestlers."""

    def __init__(self, api_key: str, data_file: str = DATA_FILE, model: str = "gpt-3.5-turbo"):
        openai.api_key = api_key
        self.df = pd.read_csv(data_file)
        self.model = model

    def _lookup_snippet(self, text: str) -> str:
        """Return CSV snippet for rows containing the text in the wrestler name."""
        matches = self.df[self.df["Rikishi"].str.contains(text, case=False, na=False)]
        if matches.empty:
            return "No matching wrestler found in dataset."
        # Show at most first three rows to keep context short
        return matches.head(3).to_csv(index=False)

    def ask(self, question: str) -> str:
        """Send a question to ChatGPT with relevant dataset snippet."""
        snippet = self._lookup_snippet(question)
        messages = [
            {"role": "system", "content": "You are a helpful assistant knowledgeable about sumo wrestling."},
            {"role": "assistant", "content": f"Dataset snippet:\n{snippet}"},
            {"role": "user", "content": question},
        ]
        response = openai.ChatCompletion.create(model=self.model, messages=messages)
        return response["choices"][0]["message"]["content"].strip()

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Ask questions about sumo wrestlers using OpenAI ChatGPT.")
    parser.add_argument("question", help="Question to ask the model")
    parser.add_argument("--api-key", help="OpenAI API key. If omitted, OPENAI_API_KEY env var is used")
    args = parser.parse_args()

    api_key = args.api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("An OpenAI API key is required. Provide via --api-key or OPENAI_API_KEY environment variable.")

    chat = SumoChat(api_key)
    answer = chat.ask(args.question)
    print(answer)

if __name__ == "__main__":
    main()
