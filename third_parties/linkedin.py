import os
import requests
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool=False):
    """scrape information from LinkedIn profiles, 
    manually scrape the information from the linkedin profile"""

    if mock:
        linkedin_profile_url="https://gist.githubusercontent.com/jorisfalter/dec36a8e44b00e47f38e1876de810bbe/raw/da484a8c2a1a158acecbb2534ad37eb62a795534/gistfile1.txt"
        response=requests.get(
            linkedin_profile_url,
            timeout=10
        )
    else:
        api_endpoint='https://nubela.co/proxycurl/api/v2/linkedin'
        # print(os.environ.get("PROXYCURL_API_KEY"))
        header_dic={"Authorization":f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response=requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10
        )

    data = response.json()
    return data


if __name__ == "__main__":
    profile_data=scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/jorisfalter", mock=True
    )
    pprint(profile_data)

    
    


