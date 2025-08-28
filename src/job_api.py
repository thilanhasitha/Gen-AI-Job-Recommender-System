
from apify_client import ApifyClient
import os
from dotenv import load_dotenv
load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))



## fetch linkedin jobs based on search query and location
def fetch_linkedin_jobs(search_query, location='Sri Lanka', rows=60):
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

# fetch naukri jobs based on search query and location
def fetch_naukri_jobs(search_query, location="Sri Lanka", rows=60):
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


# Fetch and print Actor results from the run's dataset (if there are any)
# for item in client.dataset(run["defaultDatasetId"]).iterate_items():
#     print(item)
