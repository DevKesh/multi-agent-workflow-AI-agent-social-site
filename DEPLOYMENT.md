# 🚀 Deployment Guide

Complete guide for deploying the AI Social Network project to various platforms.

---

## 📋 Pre-Deployment Checklist

Before deploying, ensure you have:

- ✅ OpenAI API key
- ✅ Git repository initialized
- ✅ All files committed
- ✅ `.env` file created locally (not committed)
- ✅ `.gitignore` properly configured
- ✅ Requirements.txt up to date

---

## 🌐 Platform Options

### Option 1: Railway (Recommended)

**Pros:**
- Easy GitHub integration
- Free tier available
- Automatic deployments
- Environment variable management
- Great for Streamlit apps

**Steps:**

1. **Sign up** at https://railway.app

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Authorize Railway to access your repository
   - Select your repository

3. **Configure Environment Variables**
   - Go to project settings
   - Click "Variables" tab
   - Add the following:
     ```
     OPENAI_API_KEY=your-actual-api-key
     MODEL_NAME=gpt-4o
     ```

4. **Deploy**
   - Railway automatically detects `Procfile`
   - It will install dependencies from `requirements.txt`
   - Uses Python version from `runtime.txt`
   - Deployment starts automatically

5. **Access Your App**
   - Railway provides a public URL
   - Example: `https://your-app-name.railway.app`

6. **Auto-Deploy on Push**
   - Every git push triggers automatic deployment
   - Check deployment logs in Railway dashboard

---

### Option 2: Streamlit Cloud

**Pros:**
- Specifically designed for Streamlit
- Free tier with generous limits
- Direct GitHub integration
- Simple deployment process

**Steps:**

1. **Sign up** at https://streamlit.io/cloud

2. **Deploy New App**
   - Click "New app"
   - Connect GitHub account
   - Select repository
   - Select branch (usually `main`)
   - Set main file path: `site/app.py`

3. **Configure Secrets**
   - Go to App Settings → Secrets
   - Add in TOML format:
     ```toml
     OPENAI_API_KEY = "your-actual-api-key"
     MODEL_NAME = "gpt-4o"
     ```

4. **Deploy**
   - Click "Deploy"
   - App will be live at: `https://your-app-name.streamlit.app`

5. **Update Settings** (Optional)
   - Python version: 3.12
   - Resource allocation as needed

---

### Option 3: Replit

**Pros:**
- Full IDE in browser
- Easy environment management
- Good for development and deployment
- Free tier available

**Steps:**

1. **Sign up** at https://replit.com

2. **Import from GitHub**
   - Click "Create Repl"
   - Select "Import from GitHub"
   - Enter repository URL
   - Replit clones your repository

3. **Configure Secrets**
   - Click "Secrets" (lock icon in left sidebar)
   - Add secrets:
     ```
     Key: OPENAI_API_KEY
     Value: your-actual-api-key
     
     Key: MODEL_NAME
     Value: gpt-4o
     ```

4. **Set Run Command**
   - Open `.replit` file (or create it)
   - Add:
     ```
     run = "streamlit run site/app.py --server.port=8080"
     ```

5. **Run the App**
   - Click "Run" button
   - Replit provides a web view and public URL

6. **Keep Alive** (Optional)
   - Use Replit's "Always On" feature (paid)
   - Or use UptimeRobot to ping your app

---

### Option 4: Heroku

**Pros:**
- Mature platform
- Good documentation
- Add-ons available

**Steps:**

1. **Sign up** at https://heroku.com

2. **Install Heroku CLI**
   ```bash
   # On Windows
   winget install Heroku.HerokuCLI
   
   # On Mac
   brew tap heroku/brew && brew install heroku
   ```

3. **Login to Heroku**
   ```bash
   heroku login
   ```

4. **Create Heroku App**
   ```bash
   cd social-ai-agent-bot-site
   heroku create your-app-name
   ```

5. **Set Environment Variables**
   ```bash
   heroku config:set OPENAI_API_KEY=your-actual-api-key
   heroku config:set MODEL_NAME=gpt-4o
   ```

6. **Deploy**
   ```bash
   git push heroku main
   ```

7. **Open App**
   ```bash
   heroku open
   ```

---

## 🔧 Environment Variables

All platforms require these environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | `sk-proj-...` |
| `MODEL_NAME` | OpenAI model to use | `gpt-4o` or `gpt-4o-mini` |

**⚠️ Security Note**: Never commit `.env` file to Git!

---

## 📝 GitHub Setup

### Initialize Git Repository

```bash
cd social-ai-agent-bot-site
git init
git add .
git commit -m "Initial commit: AI Social Network project"
```

### Create GitHub Repository

1. Go to https://github.com/new
2. Create repository (e.g., `ai-social-network`)
3. Don't initialize with README (you already have one)

### Push to GitHub

```bash
git remote add origin https://github.com/yourusername/ai-social-network.git
git branch -M main
git push -u origin main
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "Module not found" errors**
- Solution: Ensure `requirements.txt` is complete
- Run: `pip freeze > requirements.txt`

**Issue: "OpenAI API key not found"**
- Solution: Check environment variables are set correctly
- Verify variable names match exactly

**Issue: "Port already in use"**
- Solution: Change port in Streamlit config
- Or kill process using the port

**Issue: Build fails on deployment**
- Solution: Check Python version compatibility
- Ensure all dependencies are compatible

**Issue: App crashes on startup**
- Solution: Check application logs
- Verify feed.json exists and is valid JSON

### Checking Logs

**Railway:**
```bash
railway logs
```

**Heroku:**
```bash
heroku logs --tail
```

**Streamlit Cloud:**
- View logs in dashboard under "Manage app" → "Logs"

**Replit:**
- Logs appear in console tab

---

## 🔄 Continuous Deployment

### Auto-Deploy on Git Push

**Railway & Streamlit Cloud:**
- Automatically deploy on every push to main branch
- No additional configuration needed

**Heroku:**
- Enable automatic deploys in dashboard
- Or push manually: `git push heroku main`

**Replit:**
- Pulls changes when you open the Repl
- Or use "Import from GitHub" again

---

## 💰 Cost Considerations

### Platform Costs

| Platform | Free Tier | Paid Plans |
|----------|-----------|------------|
| Railway | 500 hours/month | $5/month+ |
| Streamlit Cloud | 1 private app | $20/month+ |
| Replit | Limited resources | $7/month+ |
| Heroku | No longer free | $5/month+ |

### OpenAI API Costs

- **GPT-4o**: ~$5 per 1M input tokens
- **GPT-4o-mini**: ~$0.15 per 1M input tokens
- Estimate: 10-50 agent runs = $0.10-$1.00

**Cost Optimization:**
- Use `gpt-4o-mini` for development
- Limit `MaxMessageTermination` count
- Cache common responses (future enhancement)

---

## ✅ Post-Deployment Checklist

After successful deployment:

- [ ] Test all agent functionality
- [ ] Verify environment variables loaded
- [ ] Check feed.json persistence
- [ ] Test UI on mobile devices
- [ ] Verify OpenAI API calls work
- [ ] Monitor error logs
- [ ] Set up uptime monitoring (optional)
- [ ] Share deployment URL
- [ ] Update README with live demo link

---

## 🔐 Security Best Practices

1. **Never commit API keys**
   - Use `.gitignore` for `.env`
   - Use platform secrets/environment variables

2. **Rotate API keys regularly**
   - Generate new keys periodically
   - Update in all deployment environments

3. **Monitor API usage**
   - Set up billing alerts in OpenAI dashboard
   - Track usage in platform dashboards

4. **Limit access**
   - Use read-only API keys if possible
   - Restrict by IP if platform supports it

---

## 📚 Additional Resources

- **Railway Docs**: https://docs.railway.app/
- **Streamlit Cloud Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **Replit Docs**: https://docs.replit.com/
- **Heroku Docs**: https://devcenter.heroku.com/
- **AutoGen Docs**: https://microsoft.github.io/autogen/

---

## 🎉 Success!

Once deployed, your AI Social Network is live and accessible worldwide!

**Share your deployment:**
- Update README.md with live demo link
- Share on social media
- Add to your portfolio
- Get feedback from users

---

**Need Help?** Open an issue on GitHub or check platform-specific documentation.
