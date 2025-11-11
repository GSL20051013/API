# main.py
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize the FastAPI app
app = FastAPI()

# 2. This is where your AI agent logic would go.
#    For this example, it's just a simple function.
#    In a real project, this function would load your model,
#    process the input, and return the prediction.
def get_ai_agent_response(query: str):
    """A dummy AI agent function."""
    query = query.lower()
    if "hello" in query:
        return "Hello there! How can I help you today?"
    elif "how are you" in query:
        return "I am just a set of instructions, but I'm operating perfectly!"
    else:
        return "I'm not sure how to respond to that. I am a simple AI agent."

# 3. Define the structure of the incoming request data using Pydantic.
#    This ensures the data you receive is in the correct format.
class QueryRequest(BaseModel):
    text: str

# 4. Define the structure of the outgoing response data.
class QueryResponse(BaseModel):
    answer: str

# 5. Create the API endpoint.
#    @app.post("/ask") means this endpoint listens for POST requests at the URL path /ask.
@app.post("/ask", response_model=QueryResponse)
def ask_agent(request: QueryRequest):
    """
    Receives a query, passes it to the AI agent, and returns the response.
    """
    # Get the response from your AI function
    agent_answer = get_ai_agent_response(request.text)

    # Return the response in the format we defined
    return {"answer": agent_answer}

# A simple "root" endpoint to check if the server is running
@app.get("/")
def read_root():
    return {"status": "AI Agent API is running!"}
