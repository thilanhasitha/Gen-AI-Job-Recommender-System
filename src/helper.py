import fitz # PyMuPDF
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
        uploaded_file (str): The path to the PDF file.
        
    Returns:
        str: The extracted text.
    """
      
      doc = fitz.open(uploaded_file.read(),filetype="pdf")
      text=""
      for page in doc:
            text+=page.get_text()
      return text

def ask_openai(prompt, max_tokens=500):
    """
    Sends a prompt to the OpenAI API and returns the response.
    
    Args:
        prompt (str): The prompt to send to the OpenAI API.
        max_tokens (int): The maximum number of tokens in the response.
        
    Returns:
        str: The response from the OpenAI API.
    """ 

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content

## fetch linkedin jobs based on search query and location
def fetch_linkedin_jobs(search_query, location='Sri Lanka', rows=50):
    # Prepare the Actor input
    run_input = {
        "title": search_query,
        "location": location,
        "rows": rows,
        # "companyName": ["Google", "Microsoft"],
        # "companyId": ["76987811", "1815218"],
        # "publishedAt": "",
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        },
    }

    # Run the Actor and wait for it to finish
    run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs


# # Fetch and print Actor results from the run's dataset (if there are any)
# for item in client.dataset(run["defaultDatasetId"]).iterate_items():
#     print(item)

## fetch naukri jobs based on search query and location
def fetch_naukri_jobs(search_query, location="Sri Lanka", rows=50):
    # Prepare the Actor input
    run_input = {
        # "searchUrls": ["https://www.naukri.com/it-jobs"],
        # "maxItems": 30,
        # "proxyConfiguration": { "useApifyProxy": False },
        "keywords": search_query,
        "maxjobs": rows,          # use the function parameter instead of hardcoding 60
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
        "location": location      # include location too
    }

    # Run the Actor and wait for it to finish
    run = apify_client.actor("wsrn5gy5C4EDeYCcD").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())

    return jobs


# # Fetch and print Actor results from the run's dataset (if there are any)
# for item in client.dataset(run["defaultDatasetId"]).iterate_items():
#     print(item)


