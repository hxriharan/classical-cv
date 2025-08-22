# Hugging Face Spaces + GitHub Integration Setup

This guide will help you set up automatic deployment from your GitHub repository to Hugging Face Spaces using API tokens.

## Prerequisites

1. **GitHub Account** with your repository
2. **Hugging Face Account** at [huggingface.co](https://huggingface.co)
3. **Git** installed and configured

## Method 1: Automated Setup Script

### Step 1: Create Hugging Face API Token

1. Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Click "New token"
3. Configure:
   - **Name**: `classical-cv-deployment`
   - **Role**: Write
   - **Expiration**: No expiration (or set as needed)
4. Click "Generate token"
5. **Copy the token** (you won't see it again!)

### Step 2: Run the Setup Script

```bash
# Install required package
pip install requests

# Run the setup script
python create_hf_space.py
```

The script will prompt you for:
- **HF API Token**: The token you just created
- **HF Username**: Your Hugging Face username
- **Space Name**: `classical-cv-algorithms` (or your preference)
- **GitHub Repo**: `hxriharan/classical-cv` (your repo)

### Step 3: Verify Setup

1. Check your HF Spaces: [huggingface.co/spaces](https://huggingface.co/spaces)
2. Your Space should appear with GitHub integration enabled
3. Push to GitHub: `git push origin main`
4. Monitor deployment at your Space URL

## Method 2: Manual Setup

### Step 1: Create HF Space

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Configure:
   - **Owner**: Your username
   - **Space name**: `classical-cv-algorithms`
   - **Space SDK**: Gradio
   - **Space hardware**: CPU (free tier)
   - **License**: MIT
4. Click "Create Space"

### Step 2: Configure GitHub Integration

1. Go to your Space settings
2. Find "Repository" section
3. Click "Connect to GitHub"
4. Authorize HF to access your GitHub
5. Select your repository: `hxriharan/classical-cv`
6. Set branch to `main`
7. Enable "Auto-deploy"

## Method 3: GitHub Actions (Recommended)

### Step 1: Add GitHub Secrets

1. Go to your GitHub repository
2. Click "Settings" → "Secrets and variables" → "Actions"
3. Add these secrets:
   - **`HF_TOKEN`**: Your Hugging Face API token
   - **`HF_USERNAME`**: Your Hugging Face username

### Step 2: Push the Workflow

The `.github/workflows/deploy-to-hf.yml` file is already created. Just push it:

```bash
git add .github/workflows/deploy-to-hf.yml
git commit -m "Add GitHub Actions workflow for HF deployment"
git push origin main
```

### Step 3: Monitor Deployment

1. Go to your GitHub repository
2. Click "Actions" tab
3. You should see the deployment workflow running
4. Check your HF Space for the deployed app

## Repository Structure for HF Spaces

Your repository should have this structure:

```
classical-cv/
├── app.py                    # Main application (required)
├── requirements.txt          # Dependencies (required)
├── README.md                # Space description
├── algorithms/              # Algorithm modules
│   ├── __init__.py
│   ├── image_processing.py
│   ├── edge_detection.py
│   ├── feature_detection.py
│   ├── segmentation.py
│   └── object_detection.py
├── .github/workflows/       # GitHub Actions
│   └── deploy-to-hf.yml
└── .gitignore              # Git ignore file
```

## Configuration Files

### app.py (Main Entry Point)
```python
# Your Gradio app code here
import gradio as gr
# ... rest of your code

if __name__ == "__main__":
    demo.launch()
```

### requirements.txt
```
gradio>=4.0.0
opencv-python>=4.8.0
numpy>=1.24.0
Pillow>=10.0.0
matplotlib>=3.7.0
scikit-image>=0.21.0
```

## Troubleshooting

### Common Issues

1. **Build Failures**
   - Check HF Space logs
   - Verify all dependencies in `requirements.txt`
   - Ensure `app.py` exists and runs locally

2. **Import Errors**
   - Make sure all algorithm modules are included
   - Check file paths and imports

3. **GitHub Integration Issues**
   - Verify API token permissions
   - Check repository access settings
   - Ensure branch name matches

### Debug Steps

1. **Test Locally First**
   ```bash
   python app.py
   ```

2. **Check HF Space Logs**
   - Go to your Space settings
   - View build and runtime logs

3. **Verify GitHub Actions**
   - Check Actions tab in GitHub
   - Review workflow logs

## Benefits of This Setup

### Automatic Deployment
- **Push to GitHub** → **Automatic HF deployment**
- **No manual uploads** required
- **Version control** integration

### Continuous Integration
- **Test on every push**
- **Automatic dependency installation**
- **Build verification**

### Professional Workflow
- **Git-based development**
- **Automated testing**
- **Easy rollbacks**

## Monitoring and Maintenance

### HF Space Dashboard
- **Usage statistics**
- **Performance metrics**
- **Error logs**

### GitHub Actions
- **Deployment history**
- **Build status**
- **Test results**

### Updates
- **Push changes to GitHub**
- **Automatic redeployment**
- **Zero downtime updates**

## Security Best Practices

1. **API Token Security**
   - Store tokens as GitHub secrets
   - Use minimal required permissions
   - Rotate tokens regularly

2. **Repository Security**
   - Use private repos if needed
   - Review access permissions
   - Monitor for unauthorized access

3. **Dependency Security**
   - Keep dependencies updated
   - Use specific versions
   - Monitor for vulnerabilities

## Support Resources

- **HF Spaces Docs**: [docs.huggingface.co/hub/spaces](https://docs.huggingface.co/hub/spaces)
- **GitHub Actions**: [docs.github.com/en/actions](https://docs.github.com/en/actions)
- **Gradio Docs**: [gradio.app/docs](https://gradio.app/docs)
- **Community**: HF Discord and GitHub Discussions

## Example URLs

Once deployed, your resources will be available at:

- **HF Space**: `https://huggingface.co/spaces/YOUR_USERNAME/classical-cv-algorithms`
- **GitHub Repo**: `https://github.com/hxriharan/classical-cv`
- **GitHub Actions**: `https://github.com/hxriharan/classical-cv/actions`

Replace `YOUR_USERNAME` with your actual Hugging Face username. 