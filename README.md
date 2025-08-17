# Monthly Venmo
This project is a fork of  <a href="https://github.com/jsjoeio/monthly-venmo">monthly-venmo</a> originally created by  <a href="https://github.com/jsjoeio">Joe Previte</a>. I was inspired to start using this project to automate recurring monthly Venmo transactions in my day-to-day life while adding in some features I would find useful.

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jsjoeio/monthly-venmo">
    <img src="images/logo.svg" alt="Logo" width="180" height="180">
  </a>

  <h3 align="center">monthly-venmo</h3>

  <p align="center">
    A Python script to automate monthly Venmo requests with multi-friend support
    <br />
    <a href="https://github.com/jsjoeio/monthly-venmo"><strong>Original Project Link»</strong></a>
    <br />
    <br />
    <a href="https://www.youtube.com/watch?v=cMHORRmHDJs">View Demo</a>
    ·
    <a href="https://github.com/jsjoeio/monthly-venmo/issues">Report Bug</a>
    ·
    <a href="https://github.com/jsjoeio/monthly-venmo/issues">Ask a Question</a>
  </p>
</p>

[![ui.dev newsletter - your weekly dose of JS](/images/dose-16x1.jpg)](https://bytes.dev/?r=jsjoeio)
Support the project by signing up for the UI.dev newsletter using [our link](https://bytes.dev/?r=jsjoeio)!

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#enhancements">Enhancements</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#configuration">Configuration</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<div align="center">
  <img src="./images/venmo-screenshot.png" width="60%"/>
  <img src="./images/telegram-screenshot.png" width="60%"/>
</div>

This is a Python script which runs once a month and sends Venmo requests. And it notifies you via Telegram when the requests were sent.

There is also a second script — `health.py` — which runs once a week on Sundays to ensure everything is working as expected.

### Built With

- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Venmo](https://venmo.com/signup/)
- [Telegram](https://telegram.org/)

### Adjustments

This fork includes several tweaks over the original project:

- **Multi-Friend Support**: Handle multiple friends with individual configurations
- **Flexible Scheduling**: Each friend can have their own specified day of the month
- **Individual Settings**: Different amounts, descriptions, and actions per friend
- **Enhanced User ID Tools**: Separate scripts for finding your own ID vs others' IDs
- **Improved Error Handling**: Better logging and error messages
- **OpenSSL Compatibility**: Fixed SSL warnings on macOS

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python >= v3
- `pip`

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your-username/monthly-venmo.git
   ```
2. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```
3. Copy the `.env.example` to `.env` and add environment variables
4. Run the health script to verify setup:
   ```sh
   python3 health.py
   ```
5. Run the main script:
   ```sh
   python3 init.py
   ```

### Configuration

#### Environment Variables

The project now supports multiple friends with individual configurations:

```bash
# Core settings
VENMO_ACCESS_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
TELEGRAM_BOT_TOKEN=your_bot_token

# Friend 1 settings
FRIEND_ID_1=123456789
FRIEND_NAME_1=Jordan
SEND_OR_REQUEST_1=Request
AMOUNT_1=50.00
DESCRIPTION_1=Monthly rent payment
FUNDING_ID_1=your_funding_id
SPECIFIED_DAY_1=1

# Friend 2 settings
FRIEND_ID_2=987654321
FRIEND_NAME_2=Alex
SEND_OR_REQUEST_2=Send
AMOUNT_2=25.00
DESCRIPTION_2=Monthly utilities
FUNDING_ID_2=your_funding_id
SPECIFIED_DAY_2=15
```

#### Finding User IDs

Use the provided scripts to find Venmo user IDs:

```bash
# Find your own user ID
python3 find_my_id.py

# Find another user's ID
python3 find_id.py username

# Quick lookup (minimal output)
python3 quick_find_id.py username
```

### Updating the `requirements.txt`

1. Run this command

```shell
pip3 freeze > requirements.txt
```

2. delete all the nonesense (aka leave only the actual modules used in the script)

## Usage

### Main Script (`init.py`)
- Runs daily and checks if today matches any friend's specified day
- Processes transactions only for friends whose day matches today
- Sends Telegram notifications for successful transactions

### Health Check (`health.py`)
- Runs weekly to verify all systems are working
- Tests environment variables and Venmo API connectivity
- Sends status reports via Telegram

### User ID Tools
- `find_my_id.py`: Get your own Venmo user ID
- `find_id.py`: Look up other users by username
- `quick_find_id.py`: Minimal script for quick lookups

<!-- LICENSE -->

## License

Distributed under the GPL-3.0 License. See [`LICENSE`](./LICENSE) for more information.

<!-- CONTACT -->

## Contact

**Original Project**: Joe Previte - [@jsjoeio](https://twitter.com/jsjoeio)

**Original Project Link**: [https://github.com/jsjoeio/monthly-venmo](https://github.com/jsjoeio/monthly-venmo)

**This Fork**: Enhanced version with multi-friend support and improved functionality

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [@jsjoeio](https://github.com/jsjoeio) - Original project creator
- [@mmohades for the Venmo library](https://github.com/mmohades/Venmo)
- [@liiight for the notifiers library](https://github.com/liiight/notifiers)
- [@othneildrew for the README template](https://github.com/othneildrew/Best-README-Template)
