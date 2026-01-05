"""Scraper for Kijiji Autos."""

import re
from typing import List, Optional
from urllib.parse import quote
from base_scraper import BaseScraper
from models import CarListing


class KijijiScraper(BaseScraper):
    """Scraper for Kijiji Autos car listings."""
    
    def __init__(self):
        """Initialize the Kijiji scraper."""
        super().__init__()
        self.base_url = "https://www.kijiji.ca"
    
    def get_source_name(self) -> str:
        """Return the name of the source website."""
        return "Kijiji Autos"
    
    def search(self, make: str, model: str, location: str = None) -> List[CarListing]:
        """
        Search for car listings on Kijiji.
        
        Args:
            make: Car make
            model: Car model
            location: Optional location (defaults to Ontario)
            
        Returns:
            List of CarListing objects
        """
        listings = []
        
        # Build search query
        search_query = f"{make} {model}"
        encoded_query = quote(search_query)
        
        # Use location if provided, otherwise default to broad search
        location_path = location.lower().replace(" ", "-") if location else "ontario"
        
        # Construct Kijiji URL for cars & vehicles
        url = f"{self.base_url}/b-cars-vehicles//{encoded_query}/k0c174l0"
        
        print(f"Searching Kijiji: {url}")
        
        soup = self.fetch_page(url)
        if not soup:
            return listings
        
        # Find all listing items (Kijiji uses specific class names)
        # Note: This is a simplified implementation. Actual Kijiji scraping may need
        # more sophisticated parsing or may require handling JavaScript-rendered content
        listing_items = soup.find_all('div', class_='search-item')
        
        if not listing_items:
            # Try alternative selector
            listing_items = soup.find_all('div', {'class': lambda x: x and 'listing' in x.lower()})
        
        for item in listing_items[:20]:  # Limit to first 20 results
            try:
                listing = self._parse_listing(item)
                if listing:
                    listings.append(listing)
            except Exception as e:
                print(f"Error parsing Kijiji listing: {e}")
                continue
        
        print(f"Found {len(listings)} listings on Kijiji")
        return listings
    
    def _parse_listing(self, item) -> Optional[CarListing]:
        """
        Parse a single listing item.
        
        Args:
            item: BeautifulSoup element containing listing data
            
        Returns:
            CarListing object or None if parsing fails
        """
        # Extract title
        title_elem = item.find('a', class_='title')
        if not title_elem:
            title_elem = item.find('a')
        
        if not title_elem:
            return None
        
        title = title_elem.get_text(strip=True)
        url = title_elem.get('href', '')
        if url and not url.startswith('http'):
            url = self.base_url + url
        
        # Extract price
        price_elem = item.find('div', class_='price')
        if not price_elem:
            price_elem = item.find('span', class_='price')
        price = price_elem.get_text(strip=True) if price_elem else "Contact for price"
        
        # Extract location
        location_elem = item.find('div', class_='location')
        if not location_elem:
            location_elem = item.find('span', class_='location')
        location = location_elem.get_text(strip=True) if location_elem else None
        
        # Extract description
        desc_elem = item.find('div', class_='description')
        description = desc_elem.get_text(strip=True) if desc_elem else None
        
        # Try to extract year from title
        year = self._extract_year(title)
        
        # Create listing object
        # Note: make and model are passed as parameters, not extracted from page
        return CarListing(
            title=title,
            price=price,
            year=year,
            make="",  # Will be set by aggregator
            model="",  # Will be set by aggregator
            mileage=None,  # Could be extracted from description
            location=location,
            url=url,
            source=self.get_source_name(),
            description=description
        )
    
    def _extract_year(self, text: str) -> str:
        """Extract year from text (simple pattern matching)."""
        # Look for 4-digit year (1990-2099)
        match = re.search(r'\b(19\d{2}|20\d{2})\b', text)
        return match.group(1) if match else None
