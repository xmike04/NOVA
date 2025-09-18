# Configuration Setup

## Quick Start
1. Copy `config_template.py` to `config.py`
2. Fill in your API keys and credentials
3. Never commit `config.py` to version control (it's in .gitignore)

## Required API Keys

### OpenWeatherMap API
- Get your key at: https://openweathermap.org/api
- Free tier: 1,000 calls/day

### WolframAlpha API  
- Get your App ID at: https://www.wolframalpha.com/
- Free tier: 2,000 calls/month

### Gmail App Password
- Enable 2FA on your Google account
- Generate App Password: https://myaccount.google.com/apppasswords
- Use this password, not your regular Gmail password

### Google Calendar (Optional)
- Download `credentials.json` from Google Cloud Console
- Place it in the root directory of the project

## Security Note
Your `config.py` file contains sensitive information and is automatically excluded from version control. Never share these credentials publicly.
