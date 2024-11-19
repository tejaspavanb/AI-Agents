# AI Data Extraction Agent

An AI-powered data extraction tool that retrieves and processes information for specified entities from web sources. This project is designed as part of an assessment for an AI internship. It combines custom queries, automated web searches, and language model-based parsing to provide structured data in a user-friendly dashboard.

## Features

- **File Upload & Google Sheets Connection**: Upload a CSV file or connect to a Google Sheet for data input.
- **Custom Query Input**: Define queries with placeholders to retrieve specific information for each entity.
- **Automated Web Search**: Use SerpAPI (or similar) to fetch information for each entity.
- **LLM-Based Parsing**: Integrate with OpenAI GPT-4 to extract structured data from search results.
- **Data Display & Download**: View extracted information in a table format and download results as a CSV.

## Project Overview

The AI Data Extraction Agent allows users to:

1. Upload a dataset (CSV or Google Sheets).
2. Input a custom query to search for information on each entity in the selected column.
3. Automatically retrieve and parse relevant information using APIs.
4. Download the extracted data for further analysis.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [API Configuration](#api-configuration)
- [Project Structure](#project-structure)
- [Demo](#demo)


## Setup

### Prerequisites

- Python 3.7 or above
- API keys for SerpAPI, OpenAI (GPT-4), and Google Sheets API

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tejaspavanb/AI-Agents.git
   cd AI-Agents
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Define your API keys in environment variables. Create a `.env` file or export them directly in your environment:
   ```bash
   export SERP_API_KEY="your-serp-api-key"
   export OPENAI_API_KEY="your-openai-api-key"
   export GOOGLE_CREDENTIALS='your-google-credentials-json'
   ```

   - **SERP_API_KEY**: API key for SerpAPI.
   - **OPENAI_API_KEY**: API key for OpenAI GPT-4.
   - **GOOGLE_CREDENTIALS**: JSON credentials for Google Sheets API (used for connecting to Google Sheets).

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **File Upload or Google Sheets Connection**:
   - Upload a CSV file with entity data or provide a link to a Google Sheet.
   - Preview the data and select the main column containing entity names.

2. **Define Custom Query**:
   - Enter a query template with placeholders (e.g., "Find the email address for {company}").
   - The agent will replace `{company}` with each entity name in the selected column.

3. **Retrieve Information**:
   - Click on "Run Search" to perform the web search and data extraction.
   - View the extracted results in a table format.

4. **Download Results**:
   - Download the final extracted data as a CSV file.

## Technologies Used

- **Frontend & UI**: Streamlit
- **Data Handling**: pandas, Google Sheets API
- **Web Search API**: SerpAPI (or alternative search/scraper API)
- **Language Model**: OpenAI GPT-3.5
- **Backend**: Python

## API Configuration

### SerpAPI

Sign up on [SerpAPI](https://serpapi.com/) and obtain an API key. This is used to perform automated searches for each entity.

### OpenAI GPT-4

Sign up on [OpenAI](https://platform.openai.com/) and obtain an API key. This key allows the application to access GPT-4, which processes and extracts information from web search results.

### Google Sheets API

1. Enable the Google Sheets API from the [Google Cloud Console](https://console.cloud.google.com/).
2. Download the JSON credentials file and set up the credentials as an environment variable.

## Project Structure

```
ai_data_extraction_agent/
│
├── app.py                 # Main application code (Streamlit app)
├── README.md              # Project documentation
|── requirements.txt       # List of dependencies
```

## Demo

1. **Watch the Walkthrough**:
   - [Loom video link] (https://www.loom.com/share/bcbc0313ea0742268b0d0dd41083acc2?sid=7ba7953c-154d-4e40-a298-b97ddeb3e301)

