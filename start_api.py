"""
Simple script to start the CarFinder API server
"""

import uvicorn

if __name__ == "__main__":
    print("Starting CarFinder API server...")
    print("API Documentation will be available at: http://localhost:8000/docs")
    print("Open index.html in your browser to use the web interface")
    print("\nPress CTRL+C to stop the server\n")
    
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
