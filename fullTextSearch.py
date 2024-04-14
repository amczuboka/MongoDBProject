
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import time
uri = ""

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db= client["363Phase2"]
jobCol = db["job"]

# text to search for in the job description
search_term = "python"

try:
    # Without index
    regex_pattern = r"{}".format(search_term) # search for whole word
    results = jobCol.find({"job_description": {"$regex": regex_pattern, "$options": "i"}})
    print(results.explain())

    # Perform the search with text index (jobCol.create_index([("job_description", "text")], name="job_description_text_index", default_language='english'))
    results2 = jobCol.find({"$text": {"$search": search_term, "$caseSensitive": False}})
    print(results2.explain())

except Exception as e:
    print(e)

    