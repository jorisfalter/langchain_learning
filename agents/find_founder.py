import os
from dotenv import load_dotenv

import requests

load_dotenv()


def search_linkedin_profiles():
    """scrape information from LinkedIn profiles, 
    manually scrape the information from the linkedin profile"""



    api_endpoint = 'https://nubela.co/proxycurl/api/v2/search/person'
    # print(os.environ.get("PROXYCURL_API_KEY"))
    header_dic={"Authorization":f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    response=requests.get(
        api_endpoint,
        params={'country': 'NL', 'current_role_title': 'founder','page_size': 2},
                # 'enrich_profiles': 'enrich',},
        headers=header_dic,
        timeout=10
    )

    data = response.json()
    return data


if __name__ == "__main__":
    profile_data=search_linkedin_profiles(    )
    print(profile_data)


