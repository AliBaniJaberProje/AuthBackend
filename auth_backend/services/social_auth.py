import requests
from typing import Optional

def verify_google_token(google_token: str) -> Optional[dict]:
    try:
        res = requests.get("https://www.googleapis.com/oauth2/v3/userinfo", headers={"Authorization": f"Bearer {google_token}"})
        if res.status_code == 200:
            return res.json()
        return None
    except Exception:
        return None

def verify_facebook_token(facebook_token: str) -> Optional[dict]:
    try:
        url = f"https://graph.facebook.com/me?fields=id,name,email&access_token={facebook_token}"
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        return None
    except Exception:
        return None
