# 🚀 Quick Reference Card

## Start the API
```powershell
python start_api.py
```

## API Endpoints

| Endpoint | Description | Example |
|----------|-------------|---------|
| `GET /` | API info | http://localhost:8000/ |
| `GET /api/search` | Search cars | http://localhost:8000/api/search?make=Honda&model=Civic |
| `GET /api/health` | Health check | http://localhost:8000/api/health |
| `GET /api/sources` | List sources | http://localhost:8000/api/sources |
| `GET /docs` | API docs | http://localhost:8000/docs |

## Query Parameters for /api/search

| Parameter | Required | Example | Description |
|-----------|----------|---------|-------------|
| `make` | ✅ Yes | `Honda` | Car manufacturer |
| `model` | ✅ Yes | `Civic` | Car model |
| `location` | ❌ No | `Toronto` | Search location |
| `parallel` | ❌ No | `true` | Parallel scraping (default: true) |

## Quick Examples

### Test with curl
```powershell
curl "http://localhost:8000/api/search?make=Honda&model=Civic"
```

### Test with browser
```
http://localhost:8000/api/search?make=Toyota&model=Camry&location=Vancouver
```

### Test with web interface
Open `index.html` in your browser

## Files Overview

| File | Purpose |
|------|---------|
| `api.py` | Main API server code |
| `start_api.py` | Quick start script |
| `index.html` | Web interface |
| `test_api.py` | API test suite |
| `requirements.txt` | Dependencies |
| `models.py` | Data models |
| `aggregator.py` | Scraper coordinator |

## Common Commands

```powershell
# Install dependencies
pip install -r requirements.txt

# Start API server (development)
uvicorn api:app --reload

# Start API server (quick start)
python start_api.py

# Run tests
python test_api.py

# Use original CLI
python carfinder.py Honda Civic
```

## URLs to Remember

- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Response Structure

```json
{
  "total_count": 10,
  "by_source": {"Kijiji": 5, "AutoTrader": 3, "Facebook": 2},
  "listings": [
    {
      "title": "2020 Honda Civic",
      "price": "$20,000",
      "year": "2020",
      "make": "Honda",
      "model": "Civic",
      "mileage": "50,000 km",
      "location": "Toronto, ON",
      "url": "https://...",
      "source": "Kijiji",
      "description": "..."
    }
  ]
}
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Port in use | Use different port: `uvicorn api:app --port 8080` |
| Import errors | Run: `pip install -r requirements.txt` |
| No results | Try different make/model or check scrapers |
| CORS errors | Ensure API server is running on http://localhost:8000 |

## Need Help?

- Read: `SETUP_GUIDE.md` for detailed setup
- Read: `API_README.md` for complete API docs
- Read: `WEB_API_SUMMARY.md` for overview
- Visit: http://localhost:8000/docs for interactive docs
