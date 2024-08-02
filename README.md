LLM Chatbot Project
This project includes two components: a Python service and a Node.js API server. The Python service handles interactions with language models, while the Node.js server acts as an intermediary, forwarding queries to the Python service and managing conversation history.

Python Service
Overview
The Python service interacts with language models (Llama2 and Mistral) and provides endpoints to query these models and manage conversation history. The service runs on port 8000.

Endpoints
POST /query

Description: Send a query to the selected language model and get a response.
Request Body:
json
Copy code
{
  "model": "llama2",
  "query": "What is the capital of France?"
}
Response:
json
Copy code
{
  "answer": "The capital of France is Paris."
}
GET /conversations

Description: List all conversations, ordered by date in descending order.
Response:
json
Copy code
[
  {
    "_id": "60d5f7e2f12d3b4c7a1f7e8f",
    "model": "llama2",
    "messages": [
      {"role": "user", "content": "What's the weather like today?", "date": "2024-08-02T12:00:00Z"},
      {"role": "assistant", "content": "The weather is sunny.", "date": "2024-08-02T12:01:00Z"}
    ],
    "createdAt": "2024-08-02T12:00:00Z",
    "updatedAt": "2024-08-02T12:01:00Z"
  }
]
GET /conversations/{id}

Description: Get details of a specific conversation by ID.
Response:
json
Copy code
{
  "_id": "60d5f7e2f12d3b4c7a1f7e8f",
  "model": "llama2",
  "messages": [
    {"role": "user", "content": "What's the weather like today?", "date": "2024-08-02T12:00:00Z"},
    {"role": "assistant", "content": "The weather is sunny.", "date": "2024-08-02T12:01:00Z"}
  ],
  "createdAt": "2024-08-02T12:00:00Z",
  "updatedAt": "2024-08-02T12:01:00Z"
}
Running the Python Service
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Service:

bash
Copy code
python main.py
Access the Service:

URL: http://localhost:8000
Node.js API Server
Overview
The Node.js API server acts as a middleware between the client and the Python service. It forwards queries to the Python service and manages conversation history. The server runs on port 3000.

Endpoints
POST /api/query

Description: Forward a query to the Python service and get the response.
Request Body:
json
Copy code
{
  "model": "llama2",
  "query": "What is the capital of France?"
}
Response:
json
Copy code
{
  "answer": "The capital of France is Paris."
}
GET /api/conversations

Description: Retrieve a list of all conversations from the Node.js server.
Response:
json
Copy code
[
  {
    "_id": "60d5f7e2f12d3b4c7a1f7e8f",
    "model": "llama2",
    "messages": [
      {"role": "user", "content": "What's the weather like today?", "date": "2024-08-02T12:00:00Z"},
      {"role": "assistant", "content": "The weather is sunny.", "date": "2024-08-02T12:01:00Z"}
    ],
    "createdAt": "2024-08-02T12:00:00Z",
    "updatedAt": "2024-08-02T12:01:00Z"
  }
]
GET /api/conversations/{id}

Description: Get details of a specific conversation from the Node.js server.
Response:
json
Copy code
{
  "_id": "60d5f7e2f12d3b4c7a1f7e8f",
  "model": "llama2",
  "messages": [
    {"role": "user", "content": "What's the weather like today?", "date": "2024-08-02T12:00:00Z"},
    {"role": "assistant", "content": "The weather is sunny.", "date": "2024-08-02T12:01:00Z"}
  ],
  "createdAt": "2024-08-02T12:00:00Z",
  "updatedAt": "2024-08-02T12:01:00Z"
}
Running the Node.js Server
Install Dependencies:

bash
Copy code
npm install
Run the Server:

bash
Copy code
npm start
Access the Server:

URL: http://localhost:3000
Docker Setup
Building and Running with Docker
Build Docker Images:

bash
Copy code
docker-compose build
Run Containers:

bash
Copy code
docker-compose up
This will start both the Python and Node.js services, each exposed on their respective ports.


