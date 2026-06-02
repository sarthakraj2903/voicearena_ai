🎙️ VoiceBench AI – TTS Model Evaluation & Analysis
A data-driven analysis project evaluating multiple Text-to-Speech (TTS) models based on real user feedback, focusing on naturalness, fluency, pronunciation, and reliability.

🚀 Project Overview
This project analyzes user feedback from VoiceBench to:

Identify common issues in TTS systems

Compare performance across multiple models

Extract actionable insights on voice quality

Understand what makes AI-generated speech feel human

📊 Key Insights
Top Issues Identified:

Robotic Voice

Fluency / Speed Problems

Missing / Broken Audio

Pronunciation Errors

User Preference:

Clear, natural, and well-paced voices are preferred over overly expressive or fast speech.

Critical Finding:

Naturalness and consistency matter more than raw capability.

🧠 Models Evaluated
Model A
Google DeepMind Gemini 3.1 Flash TTS

ElevenLabs Eleven v3

OpenAI gpt-4o-mini-tts

Cartesia Sonic-3

Microsoft Azure Dragon HD Omni

xAI Grok TTS

Model B
xAI Grok TTS

OpenAI gpt-4o-mini-tts

Cartesia Sonic-3

Fish Audio S2 Pro

Microsoft Azure Dragon HD Omni

Google DeepMind Gemini 3.1 Flash TTS

📈 Issue Breakdown
Issue Category	Count
Other	720
Positive Feedback	366
Robotic Voice	288
Missing / Audio Issue	275
Fluency / Speed Issue	271
Pronunciation Issue	208
Number Error	101
Pauses / Breathing Issue	69

🏆 Model Performance Summary
🥇 Best Performers
Cartesia Sonic-3 → Best balance of naturalness & pacing

Gemini 3.1 Flash TTS → Strong overall consistency

🥈 Mid-tier
Azure Dragon HD Omni → Stable but average

GPT-4o-mini-tts → Good but robotic tone issues

🥉 Needs Improvement
ElevenLabs v3

High robotic voice complaints

Over-expressive / unnatural tone

xAI Grok TTS

Low data usage / unclear performance

🔍 Key Observations from User Feedback
❌ Common Problems
Mispronunciations ("phenomenal", "St. Louis")

Unnatural emphasis

Speech too fast or robotic

Audible breathing artifacts

Missing audio outputs

✅ Positive Signals
Smooth pacing

Clear tone

Natural pauses

Human-like delivery

🎯 Final Takeaways
Naturalness > Expressiveness

Reliability is critical (no missing audio)

Pacing & fluency define user experience

Robotic voice is the biggest failure factor

💡 One-Line Insight
“The biggest gap in current TTS systems isn’t intelligence — it’s naturalness and consistency.”

🛠️ Tech Stack
Python

Pandas

Matplotlib

Data Analysis & Visualization

📂 Project Structure

voicebench-ai/
│── data/                  # Raw dataset
│── notebooks/             # Analysis notebooks (optional)
│── src/
│   └── main.py            # Main analysis script
│── outputs/
│   ├── charts/            # Visualizations
│   └── results.csv        # Processed results
│── README.md
│── requirements.txt
⚙️ Installation & Setup
Bash

# Clone repo
git clone https://github.com/your-username/voicebench-ai.git

# Navigate
cd voicebench-ai

# Install dependencies
pip install -r requirements.txt

# Run script
python main.py
📊 Example Output
Issue distribution charts

Model comparison tables

Aggregated insights

📌 Future Improvements
Add audio sample evaluation

Build scoring system for TTS quality

Deploy interactive dashboard

Real-time model comparison

🙌 Author
Sarthak Raj

Web Developer | ML Enthusiast | AI Builder

⭐ If you found this useful
Give this repo a ⭐ and feel free to contribute!
