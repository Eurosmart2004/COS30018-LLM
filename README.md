# Fine-tuning LLM Model

## Description

This project is about fine-tuning the LLM model. We chose the `google-bert/bert-base-cased` model to fine-tune with the MASHQA and COVID datasets.

Users first enter the context they want to ask in the context input. Then they type the question to receive an answer.

This model has been tested on MASHQA and COVID with results
| Dataset | Exact Match | F1 Score |
|---------|-------------|----------|
| MASHQA | 21.19 | 56.99 |
| COVID | 17.12 | 48.67 |

## Demo

You can view a live demo of the project [here](https://cos30018-llm.streamlit.app/).
