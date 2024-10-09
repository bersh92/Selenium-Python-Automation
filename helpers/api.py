import os
import requests
from bs4 import BeautifulSoup
import json

class Api:
    session = None
    access_token = None

    @staticmethod
    def _login_and_get_token():
        Api.session = requests.Session()
        Api.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"
        })

        login_page_url = 'https://admin_portnov-trials712.orangehrmlive.com/auth/login'
        login_page_response = Api.session.get(login_page_url, verify=False)
        if login_page_response.status_code != 200:
            return None

        soup = BeautifulSoup(login_page_response.text, 'html.parser')
        csrf_token = soup.find('input', attrs={'name': 'login[_csrf_token]'})
        if not csrf_token:
            return None

        csrf_token = csrf_token['value']
        login_url = "https://admin_portnov-trials712.orangehrmlive.com/auth/validateCredentials"
        login_data = {
            "login[_csrf_token]": csrf_token,
            "txtUsername": os.getenv('USERNAME_TEST'),
            "txtPassword": os.getenv('PASSWORD')
        }
        login_response = Api.session.post(login_url, data=login_data)
        if login_response.status_code == 200:
            token_url = "https://admin_portnov-trials712.orangehrmlive.com/core/getLoggedInAccountToken"
            token_response = Api.session.get(token_url, verify=False)
            if token_response.ok:
                Api.access_token = token_response.json()['token']['access_token']
            else:
                return None
        else:
            return None

    @staticmethod
    def add_candidate_recruitment_section(first_name, last_name, applied_date, email):
        if Api.session is None or Api.access_token is None:
            Api._login_and_get_token()

        if Api.access_token is None:
            print("Access token is not available. Please check login credentials.")
            return

        url = "https://admin_portnov-trials712.orangehrmlive.com/api/recruitment/candidates"
        headers = {
            "Authorization": f"Bearer {Api.access_token}",
            "Content-Type": "application/json"
        }
        data = {
            "firstName": first_name,
            "lastName": last_name,
            "appliedDate": applied_date,
            "email": email
        }
        response = Api.session.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 201:
            print("Candidate created successfully.")
            print("Response:", response.json())
        else:
            print("Failed to create candidate.")
            print("Status code:", response.status_code)
            print("Response:", response.text)

# Example usage (in a test environment):
# Api.create_candidate("John", "Doe", "2024-05-13", "john.dodfdfe@example.com")
