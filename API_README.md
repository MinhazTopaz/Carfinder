# CarFinder Web API

A RESTful API that searches for car listings across multiple websites (Kijiji, AutoTrader, and Facebook Marketplace) and provides JSON responses for easy integration with web applications.

## 🚀 Quick Start

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the API

Start the API server:
```bash
uvicorn api:app --reload
```

The API will be available at `http://localhost:8000`

### Using the Web Interface

1. Start the API server (as shown above)
2. Open `index.html` in your web browser
3. Enter car make, model, and optional location
4. Click "Search Cars" to see results

## 📚 API Documentation

### Interactive Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints

#### 1. Search for Cars
```
GET /api/search
```

**Query Parameters:**
- `make` (required): Car make (e.g., "Honda", "Toyota", "Ford")
- `model` (required): Car model (e.g., "Civic", "Camry", "F-150")
- `location` (optional): Location to search in
- `parallel` (optional): Run scrapers in parallel (default: true)

**Example Request:**
```bash
curl "http://localhost:8000/api/search?make=Honda&model=Civic&location=Toronto"
```

**Example Response:**
```json
{
  "total_count": 15,
  "by_source": {
    "Kijiji": 8,
    "AutoTrader": 5,
    "Facebook Marketplace": 2
  },
  "listings": [
    {
      "title": "2020 Honda Civic Sport",
      "price": "$22,500",
      "year": "2020",
      "make": "Honda",
      "model": "Civic",
      "mileage": "35,000 km",
      "location": "Toronto, ON",
      "url": "https://www.kijiji.ca/...",
      "source": "Kijiji",
      "description": "Well maintained Honda Civic..."
    }
  ]
}
```

#### 2. Health Check
```
GET /api/health
```

**Example Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

#### 3. Get Available Sources
```
GET /api/sources
```

**Example Response:**
```json
{
  "sources": [
    {
      "name": "Kijiji",
      "description": "Scraper for Kijiji"
    },
    {
      "name": "AutoTrader",
      "description": "Scraper for AutoTrader"
    }
  ]
}
```

## 🌐 Web Integration Examples

### JavaScript/Fetch API

```javascript
async function searchCars(make, model, location = null) {
    let url = `http://localhost:8000/api/search?make=${encodeURIComponent(make)}&model=${encodeURIComponent(model)}`;
    
    if (location) {
        url += `&location=${encodeURIComponent(location)}`;
    }
    
    const response = await fetch(url);
    const data = await response.json();
    
    return data;
}

// Usage
searchCars('Honda', 'Civic', 'Toronto')
    .then(data => {
        console.log(`Found ${data.total_count} listings`);
        data.listings.forEach(car => {
            console.log(`${car.year} ${car.make} ${car.model} - ${car.price}`);
        });
    });
```

### jQuery

```javascript
$.ajax({
    url: 'http://localhost:8000/api/search',
    data: {
        make: 'Toyota',
        model: 'Camry',
        location: 'Vancouver'
    },
    success: function(data) {
        console.log('Found ' + data.total_count + ' cars');
        // Process results
    }
});
```

### Python Requests

```python
import requests

response = requests.get('http://localhost:8000/api/search', params={
    'make': 'Ford',
    'model': 'F-150',
    'location': 'Calgary'
})

data = response.json()
print(f"Found {data['total_count']} listings")

for car in data['listings']:
    print(f"{car['year']} {car['make']} {car['model']} - {car['price']}")
```

## 🔧 Configuration

### CORS (Cross-Origin Resource Sharing)

The API is configured to allow requests from any origin. For production, update the CORS settings in `api.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Replace with your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Custom Port

Run the API on a different port:
```bash
uvicorn api:app --reload --port 8080
```

### Production Deployment

For production deployment:
```bash
uvicorn api:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📦 Response Models

### CarListingResponse
```json
{
  "title": "string",
  "price": "string | null",
  "year": "string | null",
  "make": "string",
  "model": "string",
  "mileage": "string | null",
  "location": "string | null",
  "url": "string",
  "source": "string",
  "description": "string | null"
}
```

### SearchResponse
```json
{
  "total_count": "integer",
  "by_source": {
    "source_name": "integer"
  },
  "listings": ["CarListingResponse"]
}
```

## 🚨 Error Handling

The API returns standard HTTP status codes:

- `200 OK`: Successful request
- `422 Unprocessable Entity`: Invalid parameters
- `500 Internal Server Error`: Server error during scraping

Example error response:
```json
{
  "detail": "Error searching for listings: Connection timeout"
}
```

## 💡 Tips

1. **Performance**: Use `parallel=true` (default) for faster results
2. **Caching**: Consider implementing caching for frequently searched queries
3. **Rate Limiting**: Add rate limiting in production to prevent abuse
4. **Logging**: Monitor API logs for errors and usage patterns

## 🔗 Links

- Original CLI tool: `carfinder.py`
- Web demo: `index.html`
- API documentation: http://localhost:8000/docs

## 📝 License

Same as the main CarFinder project.
