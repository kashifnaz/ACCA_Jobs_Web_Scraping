# ACCA Jobs Web Scraping

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Dependencies](https://img.shields.io/badge/Dependencies-Requests%2C%20BeautifulSoup%2C%20Pandas-brightgreen)

## Description

ACCA Jobs Web Scraping is a Python script that allows you to scrape job details from the first 10 pages of job listings in three major cities of Pakistan: Karachi, Lahore, and Islamabad. The script utilizes popular libraries like Requests, BeautifulSoup, and Pandas to gather job information from a job listing website and store it in an Excel file for easy analysis and reference.

## Features

- Web scraping of job details from multiple pages.
- Filters and collects job data from Karachi, Lahore, and Islamabad.
- Organizes job information into an Excel file for easy access and analysis.

## How to Use

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/kashifnaz/ACCA_Jobs_Web_Scraping.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ACCA_Jobs_Web_Scraping
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:

   ```bash
   python main.py
   ```

5. The script will start scraping job listings and store the data in an Excel file named `acca_jobs.xlsx`.

## Dependencies

- [Requests](https://pypi.org/project/requests/): For making HTTP requests to the job listing website.
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/): For parsing HTML content and extracting relevant job information.
- [Pandas](https://pypi.org/project/pandas/): For data manipulation and exporting the data to an Excel file.

## Example Output

The script will generate an Excel file (`acca_jobs.xlsx`) containing job details such as job title, company name, location, and more for the specified cities.

## Disclaimer

This script is provided for educational and informational purposes only. Please be respectful and responsible when scraping websites, and make sure to review and comply with the website's terms of service and policies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
