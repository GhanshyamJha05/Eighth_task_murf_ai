# 🚨 Day 6: Fraud Alert Voice Agent

A voice-powered fraud detection agent built with LiveKit Agents and Murf AI TTS that verifies customers and investigates suspicious transactions for SecureBank.

## 🎯 Features

### Fraud Detection Capabilities
- **Customer Verification** - Securely verifies identity using security questions (no sensitive data requested)
- **Transaction Investigation** - Reads out suspicious transaction details clearly
- **Real-time Decision Making** - Marks transactions as safe or fraudulent based on customer confirmation
- **Database Integration** - Loads cases from JSON database and persists outcomes
- **Professional Call Flow** - Follows banking industry best practices for fraud calls

### Security Features
- ✅ Never asks for full card numbers, PINs, or passwords
- ✅ Uses only non-sensitive verification (security questions)
- ✅ Maximum 2 verification attempts before call termination
- ✅ All data is fake/demo only
- ✅ Clear audit trail in database

### Call Flow
1. **Introduction** - Agent identifies itself as SecureBank Fraud Department
2. **Name Collection** - Asks for customer's full name
3. **Case Loading** - Retrieves fraud case from database
4. **Verification** - Asks security question (2 attempts max)
5. **Transaction Details** - Reads suspicious transaction information
6. **Confirmation** - Asks if customer made the transaction
7. **Action & Closing** - Takes appropriate action and confirms outcome

### Voice Integration
- **Murf AI Falcon TTS** - Ultra-fast, natural voice (Ryan voice)
- **Deepgram STT** - Accurate speech recognition
- **Google Gemini 2.5 Flash** - Intelligent conversation with function calling

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Murf AI API Key
- Deepgram API Key
- Google Gemini API Key
- LiveKit Server

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/GhanshyamJha05/fifth_day_Murf_api.git
cd fifth_day_Murf_api/ten-days-of-voice-agents-2025
```

2. **Setup Backend**
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
```

3. **Configure Backend Environment**
Create `backend/.env.local`:
```env
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret
DEEPGRAM_API_KEY=your_deepgram_key
GOOGLE_API_KEY=your_gemini_key
MURF_API_KEY=your_murf_key
```

4. **Setup Frontend**
```bash
cd ../frontend
npm install
```

5. **Configure Frontend Environment**
Create `frontend/.env.local`:
```env
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret
NEXT_PUBLIC_LIVEKIT_URL=ws://localhost:7880
```

### Running the Application

1. **Start LiveKit Server** (Terminal 1)
```bash
cd ten-days-of-voice-agents-2025
./livekit-server.exe --dev  # Windows
# or
./livekit-server --dev  # Mac/Linux
```

2. **Start Fraud Agent** (Terminal 2)
```bash
cd backend
.venv\Scripts\activate  # Windows
python src/agent.py dev
```

3. **Start Frontend** (Terminal 3)
```bash
cd frontend
npm run dev
```

4. **Open Browser**
Navigate to `http://localhost:3000`

## 💬 Example Conversations

### Scenario 1: Confirmed Safe Transaction

```
Agent: "Hello, this is the Fraud Detection Department from SecureBank. I'm calling about unusual activity on your account. May I have your full name please?"

You: "John Smith"

Agent: "Thank you, John. For security, what is your mother's maiden name?"

You: "Johnson"

Agent: "Thank you for confirming. We detected a suspicious transaction on your card ending in 4242:
- Amount: $1,247.99
- Merchant: ABC Electronics Ltd
- Location: Shanghai, China
- Time: November 25, 2025 at 3:42 PM EST

Did you make this transaction?"

You: "Yes, I did"

Agent: "Thank you for confirming. We've marked this as legitimate. Your card remains active. Have a great day!"
```

### Scenario 2: Confirmed Fraud

```
Agent: "Hello, this is the Fraud Detection Department from SecureBank..."

You: "Sarah Johnson"

Agent: "For security, what city were you born in?"

You: "Boston"

Agent: "We detected a suspicious transaction on your card ending in 8765:
- Amount: $3,599.00
- Merchant: Luxury Watches International
- Location: Moscow, Russia
- Time: November 26, 2025 at 1:15 AM EST

Did you make this transaction?"

You: "No, I didn't!"

Agent: "I understand. We've immediately blocked your card ending in 8765. A replacement will be mailed within 3-5 business days. You will not be charged for this transaction."
```

### Scenario 3: Verification Failed

```
Agent: "Hello, this is the Fraud Detection Department from SecureBank..."

You: "Michael Chen"

Agent: "For security, what is your favorite color?"

You: "Red"

Agent: "I'm sorry, that doesn't match our records. You have 1 attempt remaining."

You: "Green"

Agent: "I'm sorry, but for security reasons, I cannot proceed. Please visit your nearest branch. Goodbye."
```

## 📊 Test Cases in Database

The system includes 5 pre-loaded fraud cases:

1. **John Smith** - $1,247.99 from China (e-commerce)
2. **Sarah Johnson** - $3,599.00 from Russia (luxury goods)
3. **Michael Chen** - $899.50 from Nigeria (gaming)
4. **Emily Davis** - $2,150.00 from Philippines (wire transfer)
5. **Robert Wilson** - $567.25 from Romania (electronics)

Each case includes:
- Customer name and security question
- Card ending digits
- Transaction details (amount, merchant, location, time)
- Status tracking (pending_review → confirmed_safe/confirmed_fraud)

## 📁 Project Structure

```
.
├── backend/
│   ├── src/
│   │   ├── agent.py          # Fraud alert agent with verification
│   │   └── murf_tts.py       # Murf AI TTS integration
│   ├── .env.local            # Backend environment variables
│   └── pyproject.toml        # Python dependencies
├── frontend/
│   ├── app/                  # Next.js app directory
│   ├── components/           # React components
│   ├── .env.local           # Frontend environment variables
│   └── package.json         # Node dependencies
├── shared-data/
│   └── fraud_cases.json      # Fraud cases database (auto-updated)
├── challenges/
│   └── Day 6 Task.md         # Day 6 challenge documentation
└── livekit-server.exe        # LiveKit server binary
```

## 🔧 Customization

### Add More Fraud Cases

Edit `shared-data/fraud_cases.json`:
```json
{
  "userName": "Your Name",
  "securityIdentifier": "12345",
  "securityQuestion": "What is your pet's name?",
  "securityAnswer": "Fluffy",
  "cardEnding": "1234",
  "transactionAmount": "$999.99",
  "transactionName": "Suspicious Store",
  "transactionTime": "November 26, 2025 at 10:00 PM",
  "transactionCategory": "retail",
  "transactionSource": "suspicious-site.com",
  "transactionLocation": "Unknown Location",
  "status": "pending_review",
  "outcome": null
}
```

### Change Bank Name

In `backend/src/agent.py`, update the instructions to use your bank name instead of "SecureBank".

### Modify Voice Settings

```python
tts=murf_tts.TTS(
    voice="en-US-ryan",  # Change voice
    style="Conversational",  # Change style
    tokenizer=tokenize.basic.SentenceTokenizer(
        min_sentence_len=5,  # Adjust response speed
    ),
)
```

## 📊 Viewing Results

After each call, check `shared-data/fraud_cases.json` to see:
- Updated status (`confirmed_safe`, `confirmed_fraud`, or `verification_failed`)
- Outcome notes with timestamp
- Complete audit trail

## 🛠️ Tech Stack

- **Backend**: Python 3.11, LiveKit Agents SDK
- **Frontend**: Next.js 15, React, TypeScript
- **Voice**: Murf AI Falcon TTS (fastest TTS API), Deepgram STT
- **LLM**: Google Gemini 2.5 Flash with function calling
- **Real-time**: LiveKit WebRTC
- **Database**: JSON file storage (easily replaceable with SQL/MongoDB)

## 🔒 Security Notes

⚠️ **This is a demo application with fake data only!**

- Never use real customer data
- Never ask for real card numbers, PINs, or passwords
- In production, use proper database encryption
- Implement proper authentication and authorization
- Follow PCI DSS compliance for real banking applications
- Use secure communication channels (HTTPS/WSS)

## 📝 API Keys Required

1. **Murf AI** - Get from [murf.ai](https://murf.ai)
2. **Deepgram** - Get from [deepgram.com](https://deepgram.com)
3. **Google Gemini** - Get from [ai.google.dev](https://ai.google.dev)

## 🎓 Learning Resources

- [LiveKit Agents Documentation](https://docs.livekit.io/agents/)
- [Murf AI API Docs](https://murf.ai/api-docs)
- [Deepgram API Docs](https://developers.deepgram.com/)
- [Google Gemini API Docs](https://ai.google.dev/docs)

## 🤝 Contributing

This is a challenge project, but feel free to fork and customize!

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

Built as part of the Murf AI Voice Agent Challenge - Day 6
- Challenge by Murf AI
- LiveKit for the agents framework
- Inspired by real banking fraud detection systems

---

**Made with ❤️ by Ghanshyam Jha**

**⚠️ Demo purposes only - Use fake data always!**
