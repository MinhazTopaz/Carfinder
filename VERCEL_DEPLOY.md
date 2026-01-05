# Vercel Deployment Guide for CarFinder Frontend

## 🔷 Deploy Frontend to Vercel

### Prerequisites
- GitHub account
- Vercel account (sign up at https://vercel.com)
- Railway API deployed (see RAILWAY_DEPLOY.md)

### Step 1: Update API URL

Before deploying, update `index.html` with your Railway API URL:

```javascript
// Change this line in index.html:
const API_BASE_URL = 'http://localhost:8000';

// To your Railway URL (get from Railway dashboard):
const API_BASE_URL = 'https://your-app-name.railway.app';
```

### Step 2: Create vercel.json

This file is already created for you. It configures Vercel to serve your HTML file.

### Step 3: Deploy to Vercel

#### Option A: Using Vercel Dashboard (Easiest)

1. Go to https://vercel.com/dashboard
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository
4. Vercel will auto-detect the project
5. Click **"Deploy"**

#### Option B: Using Vercel CLI

```powershell
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
vercel
```

### Step 4: Configure CORS

Update `api.py` on Railway to allow your Vercel domain:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-app.vercel.app",  # Your Vercel domain
        "http://localhost:8000"  # Keep for local testing
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Commit and push - Railway will auto-deploy the update.

### Step 5: Test Your Live Site

Visit your Vercel URL (e.g., `your-app.vercel.app`)
- Search for cars
- Check that it connects to your Railway API
- Verify results appear correctly

## 🎉 You're Live!

Your website: `https://your-app.vercel.app`
Your API: `https://your-app.railway.app`

## 💰 Pricing

Vercel Free Tier includes:
- **Unlimited deployments**
- **100 GB bandwidth/month**
- **Custom domains**
- **Automatic HTTPS**

## 🔧 Troubleshooting

### CORS Errors
Make sure your Railway API allows your Vercel domain in CORS settings

### API Not Connecting
1. Check Railway API is running: `https://your-app.railway.app/api/health`
2. Verify API_BASE_URL in `index.html` is correct
3. Check browser console for errors

### Changes Not Showing
Vercel caches aggressively:
1. Hard refresh: `Ctrl + Shift + R` (Windows) or `Cmd + Shift + R` (Mac)
2. Or redeploy from Vercel dashboard

## 🚀 Custom Domain (Optional)

1. Go to your project in Vercel
2. Click **"Settings"** → **"Domains"**
3. Add your custom domain
4. Update DNS settings as instructed
5. Vercel handles HTTPS automatically

## 📝 Environment Variables (If Needed)

If you need to make API_BASE_URL configurable:

1. In Vercel Dashboard → **"Settings"** → **"Environment Variables"**
2. Add: `API_BASE_URL` = `https://your-app.railway.app`
3. Update `index.html` to use it (requires build step)

## 🔄 Automatic Deployments

Vercel automatically deploys when you push to GitHub:
- **main branch** → Production
- **other branches** → Preview deployments

## 🔗 Useful Links

- Vercel Dashboard: https://vercel.com/dashboard
- Vercel Docs: https://vercel.com/docs
- Your Site: Check Vercel dashboard for URL

---

Happy deploying! 🚀
