# 🚗 CarFinder - Now Web-Friendly! 

## What's New?

Your CarFinder script has been transformed into a **web-friendly API** that can be used to build websites, mobile apps, or integrate with other services!

## 📁 New Files Created

1. **api.py** - FastAPI web server with RESTful endpoints
2. **index.html** - Beautiful web interface to search for cars
3. **start_api.py** - Quick start script to launch the API
4. **test_api.py** - Test suite to verify everything works
5. **API_README.md** - Comprehensive API documentation
6. **SETUP_GUIDE.md** - Step-by-step setup instructions
7. **requirements.txt** - Updated with web framework dependencies

## 🚀 Getting Started (3 Easy Steps)

### Step 1: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 2: Start the API Server
```powershell
python start_api.py
```

### Step 3: Open the Web Interface
Open `index.html` in your web browser and start searching for cars!

## 🌟 Features

### REST API Endpoints
- **GET /api/search** - Search for cars across multiple websites
- **GET /api/health** - Check if the API is running
- **GET /api/sources** - Get list of supported car websites
- **GET /docs** - Interactive API documentation

### Web Interface
- Clean, modern design with gradient backgrounds
- Real-time search across Kijiji, AutoTrader, and Facebook Marketplace
- Filter by make, model, and location
- View statistics (total listings, count per source)
- Responsive card layout for listings
- Direct links to original listings
- Loading states and error handling

### API Features
- **JSON responses** - Easy to integrate with any programming language
- **CORS enabled** - Can be called from web browsers
- **Parallel scraping** - Fast results by scraping sites simultaneously
- **Auto-generated docs** - Swagger UI at `/docs`
- **Type validation** - Pydantic models ensure data quality

## 💻 How to Use the API

### From JavaScript (Web)
```javascript
fetch('http://localhost:8000/api/search?make=Honda&model=Civic')
  .then(response => response.json())
  .then(data => {
    console.log(`Found ${data.total_count} cars`);
    data.listings.forEach(car => {
      console.log(`${car.year} ${car.make} ${car.model} - ${car.price}`);
    });
  });
```

### From Python
```python
import requests

response = requests.get('http://localhost:8000/api/search', params={
    'make': 'Toyota',
    'model': 'Camry',
    'location': 'Toronto'
})

data = response.json()
for car in data['listings']:
    print(f"{car['title']} - {car['price']}")
```

### From Command Line (curl)
```powershell
curl "http://localhost:8000/api/search?make=Ford&model=F-150"
```

## 📊 Example Response

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
      "description": "Well maintained..."
    }
  ]
}
```

## 🔍 What You Can Build With This

1. **Car Shopping Website** - Let users search and compare cars
2. **Price Tracker** - Monitor car prices over time
3. **Mobile App** - Build iOS/Android apps that consume this API
4. **Slack/Discord Bot** - Get car alerts in chat
5. **Email Notifications** - Alert when new cars match criteria
6. **Data Analysis** - Analyze car market trends
7. **Comparison Tools** - Compare prices across different sites

## 🧪 Testing

Run the test suite to verify everything is working:
```powershell
python test_api.py
```

This will test all endpoints and show you the results.

## 📖 Documentation

- **SETUP_GUIDE.md** - Quick setup instructions
- **API_README.md** - Complete API documentation
- **http://localhost:8000/docs** - Interactive API playground (when server is running)

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework
- **Uvicorn** - ASGI server for running the API
- **Pydantic** - Data validation and serialization
- **BeautifulSoup4** - Web scraping
- **Selenium** - JavaScript-enabled scraping

## 🎨 Customization

### Change the Frontend
Edit `index.html` to customize:
- Colors and styling (CSS in `<style>` section)
- Layout and components (HTML structure)
- Behavior (JavaScript functions)

### Add New API Endpoints
Edit `api.py` to add more endpoints:
```python
@app.get("/api/custom-endpoint")
async def custom_endpoint():
    return {"message": "Your custom data"}
```

### Modify CORS Settings
For production, update allowed origins in `api.py`:
```python
allow_origins=["https://yourdomain.com"]
```

## 🚀 Deployment

### Local Development
```powershell
uvicorn api:app --reload
```

### Production
```powershell
uvicorn api:app --host 0.0.0.0 --port 8000 --workers 4
```

### Deploy to Cloud

**Frontend (`index.html`):**
- Vercel - Perfect for static hosting
- Netlify - Great for static sites
- GitHub Pages - Free static hosting
- Cloudflare Pages - Fast CDN hosting

**Backend API (`api.py`):**
- Railway - Easy Python deployment, free tier
- Render - Great for Python APIs, free tier
- Fly.io - Good for containerized apps
- DigitalOcean App Platform - Simple deployment
- AWS EC2 - Full control
- Google Cloud Run - Containerized deployment
- Heroku - Classic choice (paid)

## ⚠️ Important Notes

1. **Rate Limiting** - Consider adding rate limiting in production
2. **Caching** - Cache results to reduce scraping load
3. **Error Handling** - The API handles errors gracefully
4. **Website Changes** - Scrapers may need updates if target sites change
5. **Legal** - Ensure compliance with website terms of service

## 🤝 Original CLI Still Works!

The original command-line interface is still available:
```powershell
python carfinder.py Honda Civic --location Toronto
```

## 📝 Summary

You now have:
- ✅ REST API for car searching
- ✅ Beautiful web interface
- ✅ JSON responses for easy integration
- ✅ Auto-generated API documentation
- ✅ Test suite
- ✅ Production-ready code
- ✅ Both CLI and web versions

## 🎯 Next Steps

1. **Try it out**: Run `python start_api.py` and open `index.html`
2. **Explore the docs**: Visit http://localhost:8000/docs
3. **Build something**: Use the API to create your own car search tool
4. **Customize**: Modify the frontend to match your style
5. **Deploy**: Put it online for others to use

---

Need help? Check the documentation files or the interactive API docs at `/docs` when the server is running!

Happy car hunting! 🚗💨
