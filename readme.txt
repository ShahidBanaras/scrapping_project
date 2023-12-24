# Web Scraping Script for Carrier Rate Website

This script utilizes Selenium and BeautifulSoup to scrape data from the Carrier Rate website and save it in JSON format.

## Setup

### Prerequisites

- **Python**: Ensure that you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

- **PyCharm**: Install PyCharm, a popular Python IDE, from [jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download/).

### Clone the Repository

```bash
git clone [https://github.com/ShahidBanaras/scrapping_project.git]
cd [scrapping_project]
Create a Virtual Environment (Optional but Recommended)
# On PyCharm Terminal
python -m venv venv
Activate the Virtual Environment
# On PyCharm Terminal
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
Install Dependencies
pip install -r requirements.txt
Running the Script
Open the script (web_scraping_script.py) in PyCharm.
Run the script. Adjust it if necessary, e.g., updating the URL, credentials, or XPaths.
Project Structure
web_scraping_script.py: The main script for web scraping.
all_table_data.txt: The output file where JSON data will be saved.
