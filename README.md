# Tweet Agent 🐦

A Python-based CLI tool that automatically converts long-form text into a 
Twitter/X thread and posts it sequentially — no manual splitting required.

## Features
- Automatically splits text into tweet-sized chunks (280 chars)
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

## Usage
   python3 tweet_agent.py

Paste your content when prompted, press Enter twice, preview your thread,
then confirm with y to post.

## Example
Input:
   "This is a long piece of text that will be automatically split into 
   multiple tweets and posted as a thread..."

Output:
   [1] This is a long piece of text that will be automatically (1/3)
   [2] split into multiple tweets and posted (2/3)
   [3] as a thread... (3/3)

## Security
- Never commit your .env file
- .env is listed in .gitignore to prevent accidental exposure
- Regenerate your API keys if ever exposed

## Future Improvements
- Claude AI integration for text refinement before posting
- Streamlit UI for a web-based interface
- Tweet scheduling support

## License
MIT