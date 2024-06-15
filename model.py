from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_core.prompts import PromptTemplate

pipe = pipeline("question-answering", model="Eurosmart/distilbert-qa-mash-covid")
hf = HuggingFacePipeline(pipeline=pipe)

template = """
Context: {context}
Question: {question}
Answer: """
prompt = PromptTemplate.from_template(template)

chain = prompt | hf

question = "Where do I live?"
context = "My name is Sarah and I live in London"
print(chain.invoke({"question": question, "context": context}))
