import requests

from app.core.config import settings
from app.custom_exception.ti_automation_exception import TIAutpmationException


def backend_query_request(request: dict) -> dict:
    """
    Function to prepare backend query request
    """
    response = requests.post(
        settings.BACKEND_API_URL,
        headers={"x-api-key": settings.BACKEND_API_TOKEN},
        json=request,
        timeout=180,
    )

    if response.ok:
        return response.json()

    raise TIAutpmationException(
        message=f"Backend API request failed with response: {response.text}"
    )
