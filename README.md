# Day 4 - Teach-the-Tutor: Active Recall Coach

A voice-powered AI tutor built with LiveKit Agents and Murf AI TTS that helps you learn programming concepts through three interactive modes.

## 🎯 Features

### Three Learning Modes

1. **Learn Mode** - The AI explains programming concepts with examples and analogies
2. **Quiz Mode** - Test your knowledge with interactive questions
3. **Teach Back Mode** - Explain concepts back to the AI and receive feedback

### Programming Concepts Covered

- Variables
- Loops (for and while)
- Functions
- Conditional Statements (if/else)
- Arrays and Lists

### Voice Integration

- **Murf AI Falcon TTS** - High-quality, natural-sounding voices
- **Deepgram STT** - Fast and accurate speech recognition
- **Google Gemini 2.5 Flash** - Intelligent conversation handling

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 18+
- LiveKit Server
- API Keys:
  - Murf AI API Key
  - Deepgram API Key
  - Google AI API Key

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/GhanshyamJha05/fourth_day_task_murf_api.git
cd fourth_day_task_murf_api
```

2. **Setup Backend**
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Mac/Linux

pip install -e .
```

3. **Configure Environment Variables**

Create `backend/.env.local`:
```env
LIVEKIT_URL=ws://127.0.0.1:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret
GOOGLE_API_KEY=your_google_api_key
MURF_API_KEY=your_murf_api_key
DEEPGRAM_API_KEY=your_deepgram_api_key
```

4. **Setup Frontend**
```bash
cd ../frontend
npm install
```

Create `frontend/.env.local`:
```env
NEXT_PUBLIC_LIVEKIT_URL=ws://127.0.0.1:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret
```

### Running the Application

1. **Start LiveKit Server** (in project root)
```bash
./livekit-server.exe --dev
```

2. **Start Backend Agent** (in new terminal)
```bash
cd backend
.venv\Scripts\activate
python src/agent.py dev
```

3. **Start Frontend** (in new terminal)
```bash
cd frontend
npm run dev
```

4. **Open Browser**
Navigate to `http://localhost:3000` (or the port shown in terminal)

## 💬 How to Use

1. **Connect** - Click the connect button and allow microphone access
2. **Greet** - Say "Hello" to start the conversation
3. **Choose Mode** - Say "I want to learn mode" or "quiz mode" or "teach back mode"
4. **Learn** - Interact with the AI tutor based on your chosen mode
5. **Switch Modes** - You can switch between modes anytime by asking

### Example Conversations

**Learn Mode:**
- "Explain variables to me"
- "Tell me about loops"
- "What are functions?"

**Quiz Mode:**
- "Quiz me on variables"
- "Ask me about loops"
- "Test my knowledge of conditionals"

**Teach Back Mode:**
- "I'll explain variables"
- "Let me teach you about functions"
- "I want to explain loops"

## 🏗️ Project Structure

```
.
├── backend/
│   ├── src/
│   │   ├── agent.py          # Main agent logic with mode switching
│   │   └── murf_tts.py       # Murf AI TTS integration
│   ├── .env.local            # Backend environment variables
│   └── pyproject.toml        # Python dependencies
├── frontend/
│   ├── app/                  # Next.js app directory
│   ├── components/           # React components
│   ├── .env.local           # Frontend environment variables
│   └── package.json         # Node dependencies
├── shared-data/
│   └── day4_tutor_content.json  # Learning content
└── livekit-server.exe       # LiveKit server binary
```

## 🔧 Technical Details

### Backend Stack
- **LiveKit Agents SDK** - Voice agent framework
- **Murf AI Falcon** - Text-to-speech (Ryan voice)
- **Deepgram Nova-3** - Speech-to-text
- **Google Gemini 2.5 Flash** - LLM for conversation

### Frontend Stack
- **Next.js 15** - React framework
- **LiveKit Client SDK** - Real-time communication
- **Tailwind CSS** - Styling

## 📝 Content File

The tutor content is stored in `shared-data/day4_tutor_content.json`:

```json
[
  {
    "id": "variables",
    "title": "Variables",
    "summary": "Variables are like labeled containers...",
    "sample_question": "What is a variable and why is it useful?"
  }
]
```

## 🎤 Voice Configuration

The agent uses Murf AI Falcon voice:
- **Voice ID**: `en-US-ryan`
- **Style**: Conversational
- **Sample Rate**: 24kHz
- **Format**: WAV (Mono)

## 🐛 Troubleshooting

### Agent Not Responding
- Check all three services are running (LiveKit, Backend, Frontend)
- Verify API keys in `.env.local` files
- Check browser console for errors

### No Audio
- Ensure microphone permissions are granted
- Check Murf API key is valid
- Verify audio output device is working

### Connection Issues
- Confirm LiveKit server is running on port 7880
- Check firewall settings
- Verify `.env.local` URLs match

## 📚 Resources

- [LiveKit Agents Documentation](https://docs.livekit.io/agents/)
- [Murf AI API Documentation](https://murf.ai/api/docs)
- [Deepgram API Documentation](https://developers.deepgram.com/)
- [Google AI Documentation](https://ai.google.dev/)

## 🏆 Challenge Completion

This project completes Day 4 of the Murf AI Voice Agent Challenge:
- ✅ Three learning modes (Learn, Quiz, Teach Back)
- ✅ Content-driven conversations
- ✅ Mode switching functionality
- ✅ Murf Falcon TTS integration
- ✅ Interactive voice interface

## 📄 License

MIT License - See LICENSE file for details

## 👤 Author

**Ghanshyam Jha**
- GitHub: [@GhanshyamJha05](https://github.com/GhanshyamJha05)
- Challenge: #MurfAIVoiceAgentsChallenge #10DaysofAIVoiceAgents

## 🙏 Acknowledgments

- Murf AI for the Voice Agent Challenge
- LiveKit for the amazing agents framework
- The open-source community

---

Built with ❤️ for the Murf AI Voice Agent Challenge
