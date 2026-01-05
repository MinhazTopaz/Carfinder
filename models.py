"""Data models for car listings."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class CarListing:
    """Represents a car listing from any source."""
    
    title: str
    price: Optional[str]
    year: Optional[str]
    make: str
    model: str
    mileage: Optional[str]
    location: Optional[str]
    url: str
    source: str
    description: Optional[str] = None
    
    def to_dict(self):
        """Convert to dictionary for API responses."""
        return {
            'title': self.title,
            'price': self.price,
            'year': self.year,
            'make': self.make,
            'model': self.model,
            'mileage': self.mileage,
            'location': self.location,
            'url': self.url,
            'source': self.source,
            'description': self.description
        }
    
    def __str__(self):
        """String representation of the car listing."""
        parts = [
            f"\n{'='*60}",
            f"Source: {self.source}",
            f"Title: {self.title}",
            f"Make: {self.make} | Model: {self.model}",
        ]
        
        if self.year:
            parts.append(f"Year: {self.year}")
        if self.price:
            parts.append(f"Price: {self.price}")
        if self.mileage:
            parts.append(f"Mileage: {self.mileage}")
        if self.location:
            parts.append(f"Location: {self.location}")
        
        parts.append(f"URL: {self.url}")
        
        if self.description:
            desc_preview = self.description[:150] + "..." if len(self.description) > 150 else self.description
            parts.append(f"Description: {desc_preview}")
        
        parts.append('='*60)
        
        return '\n'.join(parts)
