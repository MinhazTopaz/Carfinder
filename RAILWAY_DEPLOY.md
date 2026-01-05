# Railway Deployment Guide for CarFinder API

## 🚂 Deploy to Railway in 5 Minutes

### Prerequisites
- GitHub account
- Railway account (sign up at https://railway.app)

### Step 1: Push to GitHub

Make sure your code is pushed to GitHub:

```powershell
git add .
git commit -m "Add Railway deployment config"
git push origin main
```

### Step 2: Deploy to Railway

1. Go to https://railway.app
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your `Carfinder` repository
5. Railway will automatically detect it's a Python project
6. Click **"Deploy"**

### Step 3: Configure Environment (Optional)

If you need environment variables:
1. Go to your project in Railway
2. Click on **"Variables"**
3. Add any needed variables

### Step 4: Get Your API URL

1. Go to **"Settings"** tab in Railway
2. Click **"Generate Domain"** under **Networking**
3. Copy your domain (e.g., `your-app.railway.app`)

### Step 5: Update Your Frontend

Update `index.html` to use your Railway API URL:

Find this line in `index.html`:
```javascript
const API_BASE_URL = 'http://localhost:8000';
```

Change it to:
```javascript
const API_BASE_URL = 'https://your-app.railway.app';
```

### Step 6: Deploy Frontend to Vercel

1. Go to https://vercel.com
2. Import your GitHub repository
3. Vercel will auto-detect `index.html`
4. Deploy!

## 🎉 You're Live!

Your API will be running at: `https://your-app.railway.app`
- API Docs: `https://your-app.railway.app/docs`
- Health Check: `https://your-app.railway.app/api/health`

## 💰 Pricing

Railway offers:
- **$5/month free credit** (hobby plan)
- **Pay-as-you-go** after free credit
- **Sleep after 30 min inactivity** (free tier)

## 🔧 Troubleshooting

### Build Fails
Check Railway logs in the **"Deployments"** tab

### Port Issues
Railway automatically sets `$PORT` - the Procfile handles this

### Dependencies Not Installing
Make sure `requirements.txt` is up to date:
```powershell
pip freeze > requirements.txt
```

### Selenium Issues
Railway doesn't support Selenium easily. Consider:
- Removing `FacebookMarketplaceScraper` for Railway
- Using a headless browser service
- Or deploying to a platform with browser support

## 📝 Files Created for Railway

- `Procfile` - Tells Railway how to run your app
- `railway.json` - Railway configuration
- `runtime.txt` - Specifies Python version

## 🔗 Useful Links

- Railway Dashboard: https://railway.app/dashboard
- Railway Docs: https://docs.railway.app
- Your API: Check Railway dashboard for URL

## 🚀 Next Steps After Deployment

1. Test your API: `https://your-app.railway.app/api/health`
2. Update CORS in `api.py` to allow your Vercel domain
3. Deploy `index.html` to Vercel
4. Share your car finder with the world!

---

Need help? Check Railway logs or Railway Discord community!
