import time
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

API_URL = "https://api-inference.huggingface.co/models/Eurosmart/bert-qa-mash-covid"

# API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-cased-distilled-squad"

headers = {"Authorization": "Bearer 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"}

# Load the model
tokenizer = AutoTokenizer.from_pretrained("Eurosmart/bert-qa-mash-covid")
model = AutoModelForQuestionAnswering.from_pretrained("Eurosmart/bert-qa-mash-covid")

# Initialize the question answering pipeline
qa_pipeline = pipeline('question-answering', model=model, tokenizer=tokenizer)

def query(question, context):
        # Use the pipeline to answer the question
    answer = qa_pipeline({
        'context': context,
        'question': question
    }, max_answer_len=500)
    return answer
	

def stream_data(response):
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.02)


def get_response(question, context):
    print(context)
    print (query(question, context))
    return query(question, context)['answer']