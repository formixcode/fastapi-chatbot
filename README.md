# FastAPI Chatbot with React Frontend

A modern chatbot application built with FastAPI backend and React frontend, powered by OpenAI's GPT-4o-mini model.

![FastAPI + React Chatbot](https://img.shields.io/badge/FastAPI-React-blue)

## 📋 Overview

This project implements a full-stack chatbot application with:

- **Backend**: FastAPI server that handles API requests and communicates with OpenAI's API
- **Frontend**: React application with TypeScript for a responsive chat interface
- **AI Integration**: Uses OpenAI's GPT-4o-mini model for generating responses

## 🚀 Features

- Real-time chat interface with auto-scrolling
- Secure API communication with optional API key authentication
- Loading indicators for better user experience
- Responsive design that works on desktop and mobile devices
- Error handling for both frontend and backend

## 🛠️ Tech Stack

### Backend
- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [OpenAI API](https://openai.com/api/) - AI model integration
- [Uvicorn](https://www.uvicorn.org/) - ASGI server for running the FastAPI application
- [Python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management

### Frontend
- [React 19](https://react.dev/) - UI library
- [TypeScript](https://www.typescriptlang.org/) - Type-safe JavaScript
- [Vite](https://vitejs.dev/) - Next-generation frontend tooling

## 📦 Prerequisites

- Python 3.8+
- Node.js 18+ or Bun
- OpenAI API key

## 🔧 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-chatbot.git
cd fastapi-chatbot
```

### Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### Frontend Setup

1. Navigate to the React directory:
```bash
cd react
```

2. Install dependencies:
```bash
npm install
# or if using Bun
bun install
```

3. Build the frontend:
```bash
npm run build
# or if using Bun
bun run build
```

## 🚀 Running the Application

### Development Mode

1. Start the backend server:
```bash
uvicorn main:app --reload
```

2. In a separate terminal, start the frontend development server:
```bash
cd react
npm run dev
# or if using Bun
bun run dev
```

3. Access the application:
   - Backend API: http://localhost:8000
   - Frontend (when running separate dev server): http://localhost:5173

### Production Mode

1. Build the frontend:
```bash
cd react
npm run build
# or if using Bun
bun run build
```

2. Start the FastAPI server:
```bash
uvicorn main:app
```

3. Access the application at http://localhost:8000

## 📝 API Endpoints

- `GET /` - Serves the React frontend
- `POST /api/chat` - Chat endpoint that communicates with OpenAI
  - Request body:
    ```json
    {
      "messages": [
        {"role": "user", "content": "Hello, how are you?"}
      ],
      "max_tokens": 1000,
      "temperature": 0.7
    }
    ```
  - Response:
    ```json
    {
      "response": "I'm doing well, thank you for asking! How can I assist you today?"
    }
    ```

## 🔒 Security

- The application includes optional API key authentication for external access
- CORS middleware is configured to allow cross-origin requests
- Environment variables are used for sensitive information

## 🧩 Project Structure

```
fastapi-chatbot/
├── .env                    # Environment variables
├── .gitignore              # Git ignore file
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── react/                  # React frontend
    ├── public/             # Public assets
    ├── src/                # Source code
    │   ├── assets/         # Frontend assets
    │   ├── App.css         # Application styles
    │   ├── App.tsx         # Main application component
    │   ├── index.css       # Global styles
    │   └── main.tsx        # Entry point
    ├── package.json        # Node.js dependencies
    ├── tsconfig.json       # TypeScript configuration
    └── vite.config.ts      # Vite configuration
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [OpenAI](https://openai.com/) for providing the GPT models
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent API framework
- [React](https://react.dev/) for the frontend library