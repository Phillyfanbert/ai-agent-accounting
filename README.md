# AI Personal Finance Agent

A proactive financial management agent that automates expense logging, categorizes transactions, and monitors subscriptions using Google Gemini AI.

## Features
- **Natural Language Expense Logging:** Send text descriptions (e.g., "I spent $5 on coffee") to be automatically parsed and categorized.
- **Data Management (CRUD):** Full support to create, read, update, and delete expense records.
- **Proactive Insights:** (Planned) Subscription monitoring and market comparison.

## Tech Stack
- **Backend:** FastAPI, Python, SQLAlchemy, SQLite
- **AI Integration:** Google Gemini
- **Frontend:** React / Vite (In Progress)

## Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/Phillyfanbert/ai-agent-accounting.git](https://github.com/Phillyfanbert/ai-agent-accounting.git)
cd ai-agent-accounting
```

### 2. Setup Environment
Navigate to the backend folder and set up your environment variables:
```bash
cd backend
# Create a .env file and app your API key:
# GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Install Dependencies
Ensure you are in the backend folder:
```bash
pip install -r requirements.txt
```

### 4. Run the Backend
```bash
uvicorn main:app --reload
```

## API Documentation
Once the server is running, explore and test and endpoints interactively by visiting: http://127.0.0.1:8000/docs

## Current Status
- [x] Backend Architecture & Database (SQLite)
- [x] Natural Language AI Extraction (Gemini)
- [x] Full CRUD Endpoints
- [ ] Frontend Development
- [ ] Subscription Optimizer