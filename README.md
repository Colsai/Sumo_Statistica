# Sumo Statistica

This project contains tools for working with sumo wrestling data. The
`sumo_chat.py` module wraps the OpenAI ChatGPT API so you can ask
questions about sumo wrestlers using your own API key.

## Installation

```
pip install pandas openai
```

## Usage

Set your OpenAI API key in the `OPENAI_API_KEY` environment variable or
pass it with `--api-key`. Then run:

```
python sumo_chat.py "Who won the most bouts?"
```
