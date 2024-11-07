export default async function handler(req, res) {
    if (req.method !== 'POST') {
      return res.status(405).end(); // Method Not Allowed
    }
  
    const { question } = req.body;
  
    try {
      // Use the correct URL to your FastAPI endpoint
      const response = await fetch('http://127.0.0.1:8000/search/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: question }),
      });
  
      const data = await response.json();
      res.status(200).json({ response: data.response });
    } catch (error) {
      console.error('Error:', error);
      res.status(500).json({ error: 'An error occurred while fetching the response' });
    }
  }
  