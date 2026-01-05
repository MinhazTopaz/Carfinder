"""
FastAPI Web API for CarFinder

This API provides endpoints to search for car listings across multiple websites.

Usage:
    uvicorn api:app --reload

Endpoints:
    GET /api/search - Search for car listings
    GET /api/health - Health check endpoint
    GET /docs - Interactive API documentation
"""

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
from aggregator import CarFinderAggregator
from models import CarListing

# Create FastAPI app
app = FastAPI(
    title="CarFinder API",
    description="Search for car listings across multiple websites (Kijiji, AutoTrader, Facebook Marketplace)",
    version="1.0.0"
)

# Add CORS middleware to allow requests from web browsers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models for API responses
class CarListingResponse(BaseModel):
    """Response model for a single car listing."""
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

    class Config:
        from_attributes = True


class SearchResponse(BaseModel):
    """Response model for search results."""
    total_count: int
    by_source: dict
    listings: List[CarListingResponse]


class HealthResponse(BaseModel):
    """Response model for health check."""
    status: str
    version: str


# Initialize aggregator
aggregator = CarFinderAggregator()


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information."""
    return {
        "message": "CarFinder API",
        "version": "1.0.0",
        "documentation": "/docs",
        "endpoints": {
            "search": "/api/search?make=Honda&model=Civic&location=Toronto",
            "health": "/api/health"
        }
    }


@app.get("/api/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return HealthResponse(status="healthy", version="1.0.0")


@app.get("/api/search", response_model=SearchResponse, tags=["Search"])
async def search_cars(
    make: str = Query(..., description="Car make (e.g., Honda, Toyota, Ford)"),
    model: str = Query(..., description="Car model (e.g., Civic, Camry, F-150)"),
    location: Optional[str] = Query(None, description="Location to search in (optional)"),
    parallel: bool = Query(True, description="Run scrapers in parallel for faster results")
):
    """
    Search for car listings across multiple websites.
    
    This endpoint searches Kijiji, AutoTrader, and Facebook Marketplace
    for cars matching the specified make and model.
    
    Parameters:
    - **make**: Car make (required)
    - **model**: Car model (required)
    - **location**: Location filter (optional)
    - **parallel**: Whether to run scrapers in parallel (default: true)
    
    Returns:
    - List of car listings with details including title, price, year, mileage, location, and URL
    """
    try:
        # Perform search
        listings = aggregator.search(
            make=make,
            model=model,
            location=location,
            parallel=parallel
        )
        
        # Convert to response models
        listing_responses = [
            CarListingResponse(
                title=listing.title,
                price=listing.price,
                year=listing.year,
                make=listing.make,
                model=listing.model,
                mileage=listing.mileage,
                location=listing.location,
                url=listing.url,
                source=listing.source,
                description=listing.description
            )
            for listing in listings
        ]
        
        # Count by source
        by_source = {}
        for listing in listings:
            source = listing.source
            by_source[source] = by_source.get(source, 0) + 1
        
        return SearchResponse(
            total_count=len(listing_responses),
            by_source=by_source,
            listings=listing_responses
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error searching for listings: {str(e)}"
        )


@app.get("/api/sources", tags=["Info"])
async def get_sources():
    """Get list of available scraping sources."""
    return {
        "sources": [
            {
                "name": scraper.get_source_name(),
                "description": f"Scraper for {scraper.get_source_name()}"
            }
            for scraper in aggregator.scrapers
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
