# Tweet Agent 🐦

A Python-based CLI tool that automatically converts long-form text into a 
Twitter/X thread and posts it sequentially — no manual splitting required.
Supports both X Free and X Premium subscription tiers.

## Features
- Automatically splits text into tweet-sized chunks
- Subscription-aware character limits:
  - X Free: 280 characters per tweet
  - X Premium: 1000 characters per tweet
- Numbers each tweet e.g. (1/5), (2/5) for thread continuity
- Posts tweets as a proper thread (each reply to the previous)
- Preview before posting — see all tweets before confirming
- Secure API key management via .env file

## Requirements
- Python 3.9+
- Twitter/X Developer account with Read & Write permissions

## Installation

1. Clone the repository
   git clone https://github.com/Vivek7551/tweet-agent.git
   cd tweet-agent

2. Install dependencies
   pip install tweepy python-dotenv

3. Create a .env file in the root folder
   TWITTER_API_KEY=your_Consumer_Key
   TWITTER_API_SECRET=your_Consumer_Secret
   TWITTER_ACCESS_TOKEN=your_Access_Token
   TWITTER_ACCESS_SECRET=your_Access_Token_Secret
   X_SUBSCRIBED=false

## Configuration

### Subscription Setting
In your .env file, set X_SUBSCRIBED based on your X account type:

   X_SUBSCRIBED=false   → Free tier (280 chars per tweet)
   X_SUBSCRIBED=true    → X Premium (1000 chars per tweet)

## Usage
   python3 tweet_agent.py

Paste your content when prompted, press Enter twice, preview your thread,
then confirm with y to post.

## Example

Free Tier (X_SUBSCRIBED=false):
   Input: A long piece of text...
   Output:
   [1] First 270 characters of your text... (1/3)
   [2] Next 270 characters of your text... (2/3)
   [3] Remaining text... (3/3)

Premium Tier (X_SUBSCRIBED=true):
   Input: A long piece of text...
   Output:
   [1] First 990 characters of your text... (1/2)
   [2] Remaining text... (2/2)

## Project Structure
   tweet-agent/
   ├── tweet_agent.py   # Main script
   ├── .env             # API keys and config (never commit this)
   ├── .gitignore       # Ensures .env is not pushed to GitHub
   └── README.md        # Project documentation

## Security
- Never commit your .env file
- .env is listed in .gitignore to prevent accidental exposure
- Regenerate your API keys if ever exposed

## Future Improvements
- Claude AI integration for text refinement before posting
- Streamlit UI for a web-based interface
- Tweet scheduling support
- Auto-detect subscription status via X API

## License
MIT