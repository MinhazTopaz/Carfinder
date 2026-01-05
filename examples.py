"""
Examples demonstrating how to use the CarFinder API programmatically.

You can use the CarFinderAggregator class directly in your Python code
instead of using the command-line interface.
"""

from aggregator import CarFinderAggregator


def example_basic_search():
    """Example: Basic search for a car make and model."""
    print("Example 1: Basic Search")
    print("-" * 60)
    
    aggregator = CarFinderAggregator()
    listings = aggregator.search(make="Honda", model="Civic")
    
    print(f"Found {len(listings)} total listings")
    for listing in listings[:3]:  # Show first 3
        print(f"- {listing.title} from {listing.source}")
    print()


def example_search_with_location():
    """Example: Search with location filter."""
    print("Example 2: Search with Location")
    print("-" * 60)
    
    aggregator = CarFinderAggregator()
    listings = aggregator.search(
        make="Toyota",
        model="Camry",
        location="Toronto"
    )
    
    print(f"Found {len(listings)} listings in Toronto area")
    print()


def example_sequential_search():
    """Example: Sequential search (useful for debugging)."""
    print("Example 3: Sequential Search")
    print("-" * 60)
    
    aggregator = CarFinderAggregator()
    listings = aggregator.search(
        make="Ford",
        model="F-150",
        parallel=False  # Run scrapers one at a time
    )
    
    print(f"Found {len(listings)} listings")
    print()


def example_filter_by_source():
    """Example: Filter results by source."""
    print("Example 4: Filter by Source")
    print("-" * 60)
    
    aggregator = CarFinderAggregator()
    all_listings = aggregator.search(make="Mazda", model="3")
    
    # Filter to only Kijiji results
    kijiji_listings = [l for l in all_listings if l.source == "Kijiji Autos"]
    print(f"Found {len(kijiji_listings)} listings on Kijiji")
    
    # Filter to only AutoTrader results
    autotrader_listings = [l for l in all_listings if l.source == "AutoTrader"]
    print(f"Found {len(autotrader_listings)} listings on AutoTrader")
    print()


def example_custom_processing():
    """Example: Custom processing of results."""
    print("Example 5: Custom Processing")
    print("-" * 60)
    
    aggregator = CarFinderAggregator()
    listings = aggregator.search(make="BMW", model="3 Series")
    
    # Process results - e.g., filter by year
    recent_cars = []
    for listing in listings:
        if listing.year and int(listing.year) >= 2020:
            recent_cars.append(listing)
    
    print(f"Found {len(recent_cars)} cars from 2020 or newer")
    
    # Extract just the URLs
    urls = [listing.url for listing in listings if listing.url]
    print(f"Extracted {len(urls)} URLs")
    print()


if __name__ == "__main__":
    print("="*60)
    print("CarFinder API Examples")
    print("="*60)
    print()
    
    # Note: These examples will work when you have internet access
    # and the scrapers can successfully fetch data
    
    print("Note: Examples require internet access to fetch real data.")
    print("In a sandboxed environment, these may return no results.")
    print()
    
    example_basic_search()
    example_search_with_location()
    example_sequential_search()
    example_filter_by_source()
    example_custom_processing()
    
    print("="*60)
    print("Examples complete!")
    print("="*60)
