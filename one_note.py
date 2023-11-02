import logging
import os

import requests


logger = logging.getLogger()


async def create_one_note_page(page_name: str, content: str) -> bool:
    access_token = await _get_access_token()
    if access_token:

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        create_note_url = 'https://graph.microsoft.com/v1.0/me/onenote/pages'

        note_content = {
            'title': page_name,
            'content': f'<p>{content}</p>'
        }

        response = requests.post(create_note_url, headers=headers, json=note_content)

        if response.status_code == 201:
            return True
        logger.error(f'Failed to create OneNote page. {response.text}')
        return False

    else:
        logger.error('Failed to obtain an OneNote access token.')
        return False


async def _get_access_token() -> str:
    client_id = os.getenv('ONE_NOTE_CLIENT_ID')
    client_secret = os.getenv('ONE_NOTE_CLIENT_SECRET')
    tenant_id = os.getenv('ONE_NOTE_TENANT_ID')
    scope = 'https://graph.microsoft.com/.default'
    resource = 'https://graph.microsoft.com'

    auth_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/token'

    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': scope,
        'resource': resource
    }

    response = requests.post(auth_url, data=payload)
    return response.json().get('access_token')
