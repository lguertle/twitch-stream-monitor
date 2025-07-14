import requests
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def get_access_token(client_id, client_secret):
    """Generate token and use it directly without storing in secrets"""
    try:
        logger.info("🔑 Retrieved CLIENT_ID and CLIENT_SECRET from secrets")
        
        url = "https://id.twitch.tv/oauth2/token"
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        }
        
        logger.info("🔄 Requesting new access token...")
        response = requests.post(url, data=data, timeout=10)
        
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data["access_token"]
            expires_in = token_data["expires_in"]
            
            logger.info("✅ Successfully generated access token!")
            logger.info(f"⏰ Token expires in: {expires_in} seconds ({expires_in/3600:.1f} hours)")
            
            return access_token
        else:
            logger.error(f"❌ Failed to generate token: {response.status_code}")
            return None
            
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        return None

def twitch_api_request(url, client_id, access_token, params=None):
    """Generic Twitch API GET request with error handling"""
    headers = {
        "Client-Id": client_id,
        "Authorization": f"Bearer {access_token}"
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"❌ HTTP error for URL {url}: {http_err}")
    except Exception as e:
        logger.error(f"❌ API request failed: {e}")
    return []