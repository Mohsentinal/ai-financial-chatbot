
# AI Financial Chatbot

A conversational AI chatbot built using the **Hugging Face Transformers** library and **PyTorch**. The chatbot is designed to answer financial questions and perform financial calculations like compound interest.

## Features
- Answers financial questions using GPT-Neo (or GPT-J).
- Calculates compound interest interactively.
- Logs user interactions in a `chatbot_log.txt` file.

## Directory Structure
```
ai-financial-chatbot/
├── README.md                # Project overview
├── requirements.txt         # Dependencies
├── src/
│   ├── chatbot.py           # Main chatbot script
│   ├── utils.py             # Helper functions for logging and calculations
├── data/                    # Data folder to store logs
│   └── chatbot_log.txt      # Log file for user-chatbot interactions
```

## Requirements
To run the chatbot, ensure you have the following installed:
- Python 3.8+
- Transformers
- PyTorch

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ai-financial-chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ai-financial-chatbot
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the chatbot script:
   ```bash
   python src/chatbot.py
   ```

2. Start interacting:
   ```
   You: What is compound interest?
   Chatbot: Compound interest is the process of earning interest on both the principal and the accumulated interest over time...
   ```

## Future Enhancements
- Add real-time stock data using APIs.
- Build a web interface with Streamlit.
- Include additional financial tools like loan calculations.

## License
This project is licensed under the MIT License.
