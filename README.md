# Fine-tuning LLM Model

## Description

This project is about fine-tuning the LLM model. We chose the `google-bert/bert-base-cased` model to fine-tune with the MASHQA and COVID datasets.

Users first enter the context they want to ask in the context input. Then they type the question to receive an answer.

This model has been tested on MASHQA and COVID with results
| Dataset | Exact Match | F1 Score |
|---------|-------------|----------|
| MASHQA | 21.19 | 56.99 |
| COVID | 17.12 | 48.67 |

## Installation

Before running the program, ensure that you have Python installed on your system. Then, follow these steps to set up a virtual environment and install the necessary packages:

1. Create a virtual environment:

```
python -m venv venv
```

2. Activate the virtual environment:

- On Windows:

```
./venv/Scripts/activate
```

- On macOS and Linux:

```
source venv/bin/activate
```

3. Install the required packages:

```
pip install -r requirements.txt
```

## Running the Program

You can run program following this method:

```
streamlit run app.py
```

## Demo

You can view a live demo of the project [here](https://cos30018-llm.streamlit.app/).
