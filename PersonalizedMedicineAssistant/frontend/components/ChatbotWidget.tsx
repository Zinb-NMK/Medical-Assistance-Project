// ChatbotWidget.tsx
import React, { useState } from 'react';
import axios from 'axios';

const ChatbotWidget = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMessage = { sender: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const response = await axios.post('/api/chatbot', { message: input });
      const botMessage = { sender: 'bot', text: response.data.reply };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error('Chatbot error:', error);
    }
    setInput('');
  };

  return (
    <div className="chatbot-widget p-4 rounded-lg shadow-lg bg-white">
      <h2 className="text-xl font-bold mb-2">AI Chatbot</h2>
      <div className="messages h-64 overflow-y-auto mb-2">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message p-2 my-1 rounded ${msg.sender === 'user' ? 'bg-blue-100' : 'bg-gray-200'}`}
          >
            {msg.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
        placeholder="Ask me anything..."
        className="w-full p-2 border rounded"
      />
      <button onClick={sendMessage} className="mt-2 w-full bg-blue-500 text-white p-2 rounded">
        Send
      </button>
    </div>
  );
};

export default ChatbotWidget;