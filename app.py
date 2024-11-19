import streamlit as st
import pandas as pd
import requests
import os
import openai
from openai import OpenAIError  # Updated import


SERP_API_KEY = os.getenv("SERP_API_KEY", "your-serp-api-key")  # Replace with your SerpAPI key
# --- API Keys (replace with your own keys) ---
openai.api_key = os.getenv("OPENAI_API_KEY", "your-openai-api-key")  # Replace with your OpenAI API key

# --- Utility Functions ---
def search_web(query):
    """Perform web search using SerpAPI."""
    try:
        params = {
            "q": query,
            "api_key": SERP_API_KEY,
        }
        response = requests.get("https://serpapi.com/search", params=params)
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error with SerpAPI request: {e}")
        return {"error": str(e)}

def extract_information(entity, result, prompt_template):
    """Extract specific information from search results using OpenAI."""
    try:
        prompt = prompt_template.format(entity=entity, search_results=result)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with "gpt-4" if you want to use GPT-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,  # Adjust for deterministic responses
            max_tokens=100
        )
        return response["choices"][0]["message"]["content"].strip()
    except openai.OpenAIError as e:
        return f"Error: {e}"


# --- Streamlit UI ---
st.title("AI Data Extraction Agent")
st.write("Upload a CSV file or link to a Google Sheet to extract structured information.")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
data = None

if uploaded_file:
    try:
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded Data Preview:")
        st.dataframe(data.head())
    except Exception as e:
        st.error(f"Error loading file: {e}")

# --- Query Template Input ---
if data is not None:
    selected_column = st.selectbox("Select the primary column for entities:", data.columns)
    query_template = st.text_input(
        "Enter your custom query template (e.g., 'Find the email address for {company}')"
    )
else:
    st.warning("Please upload a CSV file to proceed.")

# --- Run Search and Extraction ---
if st.button("Run Search"):
    if data is not None and selected_column and query_template:
        search_results = []  # Initialize results list

        for entity in data[selected_column]:
            try:
                # Format query and perform search
                formatted_query = query_template.format(company=entity)
                st.write(f"Searching for: {formatted_query}")
                search_result = search_web(formatted_query)

                # Extract information using OpenAI
                st.write("Extracting information...")
                extracted_info = extract_information(
                    entity, search_result, "Extract the email address of {entity} from the following data:\n{search_results}"
                )
                search_results.append({"Entity": entity, "Extracted Info": extracted_info})
            except Exception as e:
                st.error(f"Error processing entity '{entity}': {e}")

        # Display results
        if search_results:
            results_df = pd.DataFrame(search_results)
            st.write("Extraction Results:")
            st.dataframe(results_df)

            # Download results as CSV
            st.download_button(
                label="Download Results as CSV",
                data=results_df.to_csv(index=False),
                file_name="extracted_results.csv",
                mime="text/csv"
            )
        else:
            st.warning("No results were extracted. Please check your query and try again.")
    else:
        st.error("Please ensure a file is uploaded, a column is selected, and a query template is provided.")

# --- Error Handling and Debugging ---
if SERP_API_KEY == "your-serp-api-key":
    st.warning("SerpAPI key not set. Set it in the environment or replace the placeholder.")
if openai.api_key == "your-openai-api-key":
    st.warning("OpenAI API key not set. Set it in the environment or replace the placeholder.")
