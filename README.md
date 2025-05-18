Phillies Stats Tracker

A Streamlit web app that fetches, processes, and visualizes statistics related to the Philadelphia Phillies' 2025 MLB season. The app currently focuses on home run data but is built to support future expansions into other performance and game metrics.

🚀 Features

Top 10 Longest Home Runs: Cleanly styled HTML table showing the longest home runs by total distance.

Interactive Timeline: Altair chart plotting Phillies home runs over time, colored by hitter.

Automatic Daily Updates: GitHub Actions workflow runs nightly to fetch updated data and regenerate static CSVs.

🧱 Tech Stack

Python 3.10+

Streamlit

MLB Stats API

Altair (for visualization)

GitHub Actions (for automation)

📁 Project Structure


🛠 Local Development

Clone the repo:

git clone https://github.com/dlempa/phillies-stats.git
cd phillies-stats

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate       # On Windows use: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run pages/1_Home_Runs.py

🤖 GitHub Actions Automation

The GitHub Actions workflow (.github/workflows/update-data.yml) runs once per day to:

Fetch the Phillies game schedule

Collect updated player or game data

Save processed data as static CSVs in the data/ folder

Commit and push updates to the repo

You can also manually run the workflow from the GitHub UI (Actions tab).


🔮 Planned Expansions

TBD

📎 Acknowledgments

This project uses the following data sources:

mlb-statsapi, a Python wrapper for the unofficial MLB Stats API

Direct calls to the MLB Stats API for schedule and play-by-play game data

This project is not affiliated with Major League Baseball or its data providers.
