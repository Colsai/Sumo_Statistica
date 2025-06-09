# Sumo Statistica

This project contains tools for working with sumo wrestling data. The
`sumo_statistica` package wraps the OpenAI ChatGPT API so you can ask
questions about sumo wrestlers using your own API key.

## Installation

```bash
pip install pandas openai
```

## Usage

Set your OpenAI API key in the `OPENAI_API_KEY` environment variable or
pass it with `--api-key`. Then run:

```
python -m sumo_statistica.chat "Who won the most bouts?"
```
