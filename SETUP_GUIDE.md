# 🚗 CarFinder Web API - Quick Setup Guide

## Step 1: Install Dependencies

Open PowerShell in this directory and run:

```powershell
pip install -r requirements.txt
```

This will install:
- FastAPI (web framework)
- Uvicorn (ASGI server)
- Pydantic (data validation)
- Plus all existing dependencies

## Step 2: Start the API Server

Option A - Using the start script:
```powershell
python start_api.py
```

Option B - Using uvicorn directly:
```powershell
uvicorn api:app --reload
```

## Step 3: Access the Application

Once the server is running, you have several options:

### 1. Web Interface (Recommended for beginners)
- Open `index.html` in your web browser
- Enter car make and model
- Click "Search Cars"

### 2. Interactive API Documentation
- Visit: http://localhost:8000/docs
- Try the API directly from your browser
- See all available endpoints and parameters

### 3. Direct API Access
Open a new PowerShell window and test with curl:
```powershell
curl "http://localhost:8000/api/search?make=Honda&model=Civic"
```

Or use a tool like Postman, Insomnia, or your web browser.

## Example Usage

### From Web Browser
1. Go to http://localhost:8000/docs
2. Click on `/api/search` endpoint
3. Click "Try it out"
4. Fill in:
   - make: `Honda`
   - model: `Civic`
   - location: `Toronto` (optional)
5. Click "Execute"

### From JavaScript
```javascript
fetch('http://localhost:8000/api/search?make=Toyota&model=Camry')
  .then(response => response.json())
  .then(data => console.log(data));
```

### From Python
```python
import requests
response = requests.get('http://localhost:8000/api/search', 
                       params={'make': 'Ford', 'model': 'F-150'})
print(response.json())
```

## What You Get

The API returns JSON with:
- **total_count**: Number of listings found
- **by_source**: Count of listings per website (Kijiji, AutoTrader, Facebook)
- **listings**: Array of car listings with details:
  - title
  - price
  - year
  - make/model
  - mileage
  - location
  - url (link to the listing)
  - source (which website)

## Troubleshooting

### Port Already in Use
If port 8000 is busy, use a different port:
```powershell
uvicorn api:app --reload --port 8080
```

### CORS Errors in Browser
The API is configured to allow all origins. If you still get CORS errors, make sure:
1. The API server is running
2. You're using the correct URL (http://localhost:8000)

### Import Errors
Make sure you installed all requirements:
```powershell
pip install -r requirements.txt
```

## Next Steps

- Read the full documentation in `API_README.md`
- Customize the `index.html` frontend
- Deploy to a production server
- Add authentication if needed
- Implement caching for better performance

## Stopping the Server

Press `CTRL + C` in the terminal where the server is running.

---

For more details, see `API_README.md`
