# Mega Project Jarvis 🤖

A Python-based voice assistant (inspired by Jarvis) that listens to voice commands and can:
- Open websites (Google, Facebook, YouTube, Instagram)
- Play songs from a custom music library
- Answer general questions using AI (powered by Groq's LLaMA model)
- Speak responses out loud

## Features

- 🎙️ Voice recognition using the microphone
- 🌐 Opens common websites on command
- 🎵 Plays songs from a personal music library
- 🧠 AI-powered responses for general queries
- 🔊 Text-to-speech replies (using macOS's built-in `say` command)

## How It Works

1. Run the assistant — it says "Initializing Jarvis...."
2. It continuously listens for the wake word **"Jarvis"**
3. Once it hears "Jarvis", it replies "yes sir" and starts listening for your command
4. Say your command (e.g., "open google", "play perfect")
5. Jarvis executes the command or answers using AI if it doesn't match a known command

## Tech Stack

- Python 3
- `speech_recognition` – for converting voice to text
- `groq` – for AI-powered responses (LLaMA 3.3 model)
- `python-dotenv` – for managing API keys securely

## Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/PanchalAkshat/Mega-project-jarvis.git
cd Mega-project-jarvis
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv .venv
source .venv/bin/activate   # On Mac/Linux
.venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
This project uses the [Groq API](https://console.groq.com) for AI responses. You'll need your own free API key.

1. Create a free account at [console.groq.com](https://console.groq.com)
2. Generate an API key
3. Create a file named `.env` in the project root folder
4. Add this line to it (replace with your actual key):
```
groq_api_key=your_api_key_here
```

⚠️ **Never share your `.env` file or commit it to GitHub.** It's already excluded via `.gitignore`.

### 5. Add your own songs (optional)
Open `musicLibrary.py` and add song names (lowercase) mapped to their YouTube links:
```python
music = {
    "perfect": "https://www.youtube.com/watch?v=...",
    "tu hi mera": "https://www.youtube.com/watch?v=..."
}
```

### 6. Run the assistant
```bash
python main.py
```

Say **"Jarvis"** to wake it up, then give a command, for example:
- "open google"
- "play perfect"
- "what is the capital of France"

## Notes
- Make sure your microphone permissions are enabled.
- The `speak()` function uses macOS's built-in `say` command for text-to-speech. Windows/Linux users will need to replace this with an alternative (e.g., `pyttsx3` or `gTTS`).
- Internet connection is required to run this project.

## License
Feel free to use and modify this project for learning purposes.
