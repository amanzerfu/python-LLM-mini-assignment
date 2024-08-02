const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

app.use(express.json());

let conversationHistory = [];
let conversationIdCounter = 1;

// Helper function to generate a new conversation
function createConversation(model, question, response) {
    return {
        id: conversationIdCounter++,
        model: model,
        questions: [{ question: question, response: response }],
        createdAt: new Date().toISOString()
    };
}

// POST /query - Send query to the Python program and record conversation
app.post('/query', async (req, res) => {
    const { model, question } = req.body;

    try {
        // Send query to Python program
        const response = await axios.post('http://localhost:8000/query', { model, question });
        const { data } = response;

        // Record the conversation
        const conversation = createConversation(model, question, data.response);
        conversationHistory.push(conversation);

        res.json(conversation);
    } catch (error) {
        res.status(500).json({ error: 'An error occurred while processing the query.' });
    }
});

// GET /conversations - List all conversations
app.get('/conversations', (req, res) => {
    const sortedConversations = conversationHistory.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
    res.json(sortedConversations);
});

// GET /conversations/:id - Get details of a specific conversation
app.get('/conversations/:id', (req, res) => {
    const { id } = req.params;
    const conversation = conversationHistory.find(conv => conv.id === parseInt(id, 10));

    if (conversation) {
        res.json(conversation);
    } else {
        res.status(404).json({ error: 'Conversation not found.' });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
