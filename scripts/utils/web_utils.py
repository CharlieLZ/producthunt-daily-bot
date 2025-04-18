import requests
from typing import Optional
from bs4 import BeautifulSoup

def fetch_og_image(url: str) -> str:
    """
    Get the Open Graph image URL of a web page
    
    Args:
        url: web page URL
    
    Returns:
        str: Open Graph image URL, returns empty string if not found
    """
    try:
        response = safe_request(url)
        if response and response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            og_image = soup.find("meta", property="og:image")
            if og_image and og_image.get("content"):
                return og_image["content"]
    except Exception as e:
        print(f"Failed to get og:image: {url}, error: {e}")
    return ""

def safe_request(
    url: str, 
    method: str = "GET", 
    headers: Optional[dict] = None, 
    timeout: int = 10, 
    **kwargs
) -> Optional[requests.Response]:
    """
    Safe HTTP request wrapper
    
    Args:
        url: request URL
        method: request method, default is "GET"
        headers: request headers
        timeout: timeout in seconds
        **kwargs: other parameters passed to requests
    
    Returns:
        Optional[requests.Response]: response object, returns None if request fails
    """
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            timeout=timeout,
            **kwargs
        )
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {url}, error: {e}")
        return None

def make_request_with_retry(
    url: str,
    method: str = "GET",
    max_retries: int = 3,
    retry_delay: int = 1,
    **kwargs
) -> Optional[requests.Response]:
    """
    HTTP request with retry mechanism
    
    Args:
        url: request URL
        method: request method, default is "GET"
        max_retries: maximum number of retries
        retry_delay: retry delay in seconds
        **kwargs: other parameters passed to requests
    
    Returns:
        Optional[requests.Response]: response object, returns None if all retries fail
    """
    from time import sleep
    
    for attempt in range(max_retries):
        response = safe_request(url, method=method, **kwargs)
        if response is not None:
            return response
        
        if attempt < max_retries - 1:  # If not the last attempt
            sleep(retry_delay)
            print(f"Retry request {attempt + 1}/{max_retries}: {url}")
    
    return None

def parse_html(html_content: str, parser: str = 'html.parser') -> BeautifulSoup:
    """
    Parse HTML content
    
    Args:
        html_content: HTML string
        parser: BeautifulSoup parser type
    
    Returns:
        BeautifulSoup: parsed BeautifulSoup object
    """
    return BeautifulSoup(html_content, parser)