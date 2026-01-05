"""Base scraper class with common functionality."""

from abc import ABC, abstractmethod
from typing import List
import requests
from bs4 import BeautifulSoup
import time

from models import CarListing


class BaseScraper(ABC):
    """Abstract base class for all car listing scrapers."""
    
    def __init__(self):
        """Initialize the scraper with common settings."""
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.timeout = 10
        
    @abstractmethod
    def search(self, make: str, model: str, location: str = None) -> List[CarListing]:
        """
        Search for car listings.
        
        Args:
            make: Car make (e.g., 'Honda', 'Toyota')
            model: Car model (e.g., 'Civic', 'Camry')
            location: Optional location filter
            
        Returns:
            List of CarListing objects
        """
        pass
    
    @abstractmethod
    def get_source_name(self) -> str:
        """Return the name of the source website."""
        pass
    
    def fetch_page(self, url: str) -> BeautifulSoup:
        """
        Fetch and parse a webpage.
        
        Args:
            url: URL to fetch
            
        Returns:
            BeautifulSoup object of the parsed page
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def delay(self, seconds: float = 1.0):
        """Add delay between requests to be respectful to servers."""
        time.sleep(seconds)
