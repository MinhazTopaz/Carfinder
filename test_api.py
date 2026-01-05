"""
Test script to verify the CarFinder API is working correctly.

Run this after starting the API server to test all endpoints.
"""

import requests
import json

API_BASE = "http://localhost:8000"

def test_root():
    """Test the root endpoint."""
    print("Testing root endpoint...")
    try:
        response = requests.get(f"{API_BASE}/")
        print(f"✓ Root endpoint: {response.status_code}")
        print(f"  Response: {response.json()['message']}")
        return True
    except Exception as e:
        print(f"✗ Root endpoint failed: {e}")
        return False

def test_health():
    """Test the health check endpoint."""
    print("\nTesting health endpoint...")
    try:
        response = requests.get(f"{API_BASE}/api/health")
        data = response.json()
        print(f"✓ Health check: {response.status_code}")
        print(f"  Status: {data['status']}")
        print(f"  Version: {data['version']}")
        return True
    except Exception as e:
        print(f"✗ Health check failed: {e}")
        return False

def test_sources():
    """Test the sources endpoint."""
    print("\nTesting sources endpoint...")
    try:
        response = requests.get(f"{API_BASE}/api/sources")
        data = response.json()
        print(f"✓ Sources endpoint: {response.status_code}")
        print(f"  Available sources: {len(data['sources'])}")
        for source in data['sources']:
            print(f"    - {source['name']}")
        return True
    except Exception as e:
        print(f"✗ Sources endpoint failed: {e}")
        return False

def test_search():
    """Test the search endpoint."""
    print("\nTesting search endpoint...")
    print("  (This may take a while as it actually scrapes websites...)")
    try:
        response = requests.get(
            f"{API_BASE}/api/search",
            params={
                'make': 'Honda',
                'model': 'Civic',
                'parallel': True
            }
        )
        data = response.json()
        print(f"✓ Search endpoint: {response.status_code}")
        print(f"  Total listings found: {data['total_count']}")
        print(f"  Breakdown by source:")
        for source, count in data['by_source'].items():
            print(f"    - {source}: {count}")
        
        if data['listings']:
            print(f"\n  Sample listing:")
            sample = data['listings'][0]
            print(f"    Title: {sample['title']}")
            print(f"    Price: {sample['price']}")
            print(f"    Source: {sample['source']}")
            print(f"    URL: {sample['url'][:60]}...")
        
        return True
    except Exception as e:
        print(f"✗ Search endpoint failed: {e}")
        return False

def test_api_docs():
    """Test that API documentation is accessible."""
    print("\nTesting API documentation...")
    try:
        response = requests.get(f"{API_BASE}/docs")
        print(f"✓ API docs accessible: {response.status_code}")
        print(f"  Visit: {API_BASE}/docs")
        return True
    except Exception as e:
        print(f"✗ API docs failed: {e}")
        return False

def main():
    """Run all tests."""
    print("="*60)
    print("CarFinder API Test Suite")
    print("="*60)
    print("\nMake sure the API server is running first!")
    print("Start it with: python start_api.py")
    print("="*60)
    
    results = []
    
    # Run tests
    results.append(("Root", test_root()))
    results.append(("Health", test_health()))
    results.append(("Sources", test_sources()))
    results.append(("API Docs", test_api_docs()))
    results.append(("Search", test_search()))
    
    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print("="*60)
    print(f"Results: {passed}/{total} tests passed")
    print("="*60)
    
    if passed == total:
        print("\n🎉 All tests passed! The API is working correctly.")
        print(f"\nNext steps:")
        print(f"  1. Open index.html in your browser to use the web interface")
        print(f"  2. Visit {API_BASE}/docs for interactive API documentation")
        print(f"  3. Start building your car search website!")
    else:
        print("\n⚠️  Some tests failed. Check the errors above.")
        print("Make sure the API server is running: python start_api.py")

if __name__ == "__main__":
    main()
