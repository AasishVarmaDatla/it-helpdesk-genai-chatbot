# IT Helpdesk Chatbot-Pari

This project is a GenAI-based IT Helpdesk Chatbot that helps users resolve common technical issues through natural language interaction.Pari can understand user problems, search a knowledge base, and provide troubleshooting suggestions similar to IT support systems.

The goal of this project is to learn how AI-powered chat systems are used in enterprise IT environments.

---

## What This Project Does

- Allows users to ask IT-related questions in chat format  
- Identifies the type of technical issue (network, software, hardware, account)  
- Provides step-by-step troubleshooting guidance  
- Stores basic ticket information for unresolved issues  
- Simulates how real helpdesk systems operate  

---

## Features Implemented

- Natural language query processing 
- Issue category detection  
- Knowledge base search  
- Automated response generation  
- Basic ticket creation system  
- Simple chat interface  

---

## Tech Stack Used

### Backend
- Python  
- - Flask / FastAPI 

### Frontend
- HTML, CSS, JavaScript  

### Storage
- JSON / SQLite database  
- Vector database (FAISS / ChromaDB)
- Sample SQLite DB included for demo purposes. 

---

## How The System Works

1. User submits a query  
2. The query is processed using NLP  
3. Relevant solutions are retrieved from the knowledge base  
4. Chatbot generates a response using the AI model 
5. If the issue is unresolved, a support ticket is created  

---

## Example Queries

- My laptop is not connecting to WiFi  
- VPN is not working  
- How do I reset my email password  
- System is running very slow  
- Printer is not detected  

---

## Deployment

Backend:
- Hosted on Render
- Gunicorn used for production
- requirements.txt included

Frontend:
- Hosted on Netlify
- Static HTML/CSS/JS
- Connected to backend API


## Live Demo
Frontend: https://it-helpdesk-chatbot-pari.netlify.app  
Backend API: https://it-helpdesk-genai-chatbot.onrender.com/chat


## Running The Project Locally


### Clone Repository

```bash
git clone https://github.com/AasishVarmaDatla/it-helpdesk-genai-chatbot.git
cd it-helpdesk-genai-chatbot
```

## What I Learned From This Project

This project helped me understand how a chatbot works and how GenAI can be applied to real world applications.
