LLM Chatbot API
This project provides a two-tiered API solution for interacting with language models (Llama2 and Mistral). The backend is composed of a Python FastAPI server for processing queries and a Node.js server that serves as an intermediary, forwarding requests to the Python server and handling conversation history.

Table of Contents
Python FastAPI Server
Installation
Running the Server
Endpoints
Node.js API Server
Installation
Running the Server
Endpoints
Docker
Environment Variables
Python FastAPI Server
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/llm-chatbot.git
cd llm-chatbot
Navigate to the app directory:

bash
Copy code
cd app
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Server
Run the FastAPI server on port 8000:

bash
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000
Endpoints
POST /query

Description: Send a query to the selected model.
Body:
json
Copy code
{
  "model": "llama2",  // or "mistral"
  "query": "Your question here"
}
Response:
json
Copy code
{
  "answer": "Response from the model"
}
GET /conversations

Description: Retrieve a list of all conversation histories, ordered by date (DESC).
Response:
json
Copy code
[
  {
    "id": "conversation_id",
    "model": "llama2",
    "messages": [
      { "role": "user", "content": "Your question here" },
      { "role": "assistant", "content": "Response from the model" }
    ],
    "createdAt": "timestamp",
    "updatedAt": "timestamp"
  },
  ...
]
GET /conversations/{id}

Description: Get the details of a specific conversation.
Response:
json
Copy code
{
  "id": "conversation_id",
  "model": "llama2",
  "messages": [
    { "role": "user", "content": "Your question here" },
    { "role": "assistant", "content": "Response from the model" }
  ],
  "createdAt": "timestamp",
  "updatedAt": "timestamp"
}
Node.js API Server
Installation
Navigate to the node_api_server directory:

bash
Copy code
cd node_api_server
Install the required dependencies:

bash
Copy code
npm install
Running the Server
Run the Node.js server on port 3000:

bash
Copy code
node server.js
Endpoints
POST /api/query

Description: Send a query to the Python server.
Body:
json
Copy code
{
  "model": "llama2",  // or "mistral"
  "query": "Your question here"
}
Response:
json
Copy code
{
  "answer": "Response from the model"
}
GET /api/conversations

Description: Retrieve a list of all conversation histories, ordered by date (DESC).
Response:
json
Copy code
[
  {
    "id": "conversation_id",
    "model": "llama2",
    "messages": [
      { "role": "user", "content": "Your question here" },
      { "role": "assistant", "content": "Response from the model" }
    ],
    "createdAt": "timestamp",
    "updatedAt": "timestamp"
  },
  ...
]
GET /api/conversations/{id}

Description: Get the details of a specific conversation.
Response:
json
Copy code
{
  "id": "conversation_id",
  "model": "llama2",
  "messages": [
    { "role": "user", "content": "Your question here" },
    { "role": "assistant", "content": "Response from the model" }
  ],
  "createdAt": "timestamp",
  "updatedAt": "timestamp"
}
Docker
You can run both servers using Docker and Docker Compose.

Build and run the Docker containers:

bash
Copy code
docker-compose up --build
The FastAPI server will be available at http://localhost:8000.

The Node.js server will be available at http://localhost:3000.

Environment Variables
Create a .env file in the node_api_server directory with the following content:

arduino
Copy code
MONGO_URI=mongodb://your_mongo_db_uri
Replace your_mongo_db_uri with your actual MongoDB URI.
