import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from openai import OpenAI
from apify_client import ApifyClient

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)
apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.

    Args:
        uploaded_file (str or file-like): File path or uploaded file object.

    Returns:
        str: The extracted text.
    """
    if isinstance(uploaded_file, str):  # if it's a file path
        doc = fitz.open(uploaded_file)
    else:  # if it's a file-like object (e.g. Streamlit)
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text()
    return text


def ask_openai(prompt, max_tokens=500):
    """
    Sends a prompt to the OpenAI API and returns the response.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def fetch_linkedin_jobs(search_query, location="Sri Lanka", rows=50):
    """
    Fetch jobs from LinkedIn using Apify actor.
    """
    run_input = {
        "title": search_query,
        "location": location,
        "rows": rows,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        },
    }
    run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs


def fetch_naukri_jobs(search_query, location="Sri Lanka", rows=50):
    """
    Fetch jobs from Naukri.com using Apify actor.
    """
    run_input = {
        "keywords": search_query,
        "maxjobs": rows,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
        "location": location,
    }
    run = apify_client.actor("wsrn5gy5C4EDeYCcD").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs
