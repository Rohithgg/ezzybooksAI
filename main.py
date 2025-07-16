import os
from http.client import responses
from fastapi import FastAPI, UploadFile, HTTPException
import pdfplumber
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import getpass
import os
from langchain_core.messages import AIMessage, HumanMessage

# import the model from langchain
model = OllamaLLM(model="llama3.1")
# define the model
workflow = StateGraph(state_schema=MessagesState)
# define the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}
# define the single state node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)
# save the memory
memory_saver = MemorySaver()
aiapp = workflow.compile(checkpointer=memory_saver)
#config
config = {"configurable": {"thread_id": "abc123"}}

app = FastAPI()

def extract_pdf_book(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text.strip()

@app.post("/summarize/") #TODO: pipline this into the front end
# summerize the text using the model and context
def summary(text):
    query = "summarize this in a manageable chunks and help the user understand better and fast: {}".format(text)
    input_messages = [HumanMessage(query)]
    output = aiapp.invoke({"messages": input_messages}, config)
    output["messages"][-1].pretty_print()

def chat():
    while True:
        user_input = input("User: ")
        if user_input.lower() == "/exit":
            break
        input_messages = [HumanMessage(user_input)]
        output = aiapp.invoke({"messages": input_messages}, config)
        output["messages"][-1].pretty_print()

@app.post("/upload/")
def main():#this is just a console not a UI TODO: make UI and pipeline it 
    # pages for the pdf and chatbot
    print("Welcome to the PDF Summarizer!")
    print("Please upload a PDF or DOCX file to summarize it.")
    print("You can also chat with the chatbot to get a summary.")
    print("You can type 'exit' to exit the chatbot.")
    print("")
    print("Please enter the path to the file you want to summarize:")
    file_path = input("File Path: ")
    if not os.path.exists(file_path):
        print("File not found.")
        return
    if file_path.endswith(".pdf"):
        text = extract_pdf_book(file_path)
    else:
        print("Unsupported file type.")
        return
    print("Summarizing the file...")
    print("Chatbot:")
    summary(text)
    print("continue chatting with the chatbot")
    chat()




if __name__ == "__main__":
    main()
