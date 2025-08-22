#!/usr/bin/env python3
"""
Script to create and configure a Hugging Face Space for Classical CV project
"""

import requests
import json
import os
from pathlib import Path

def create_hf_space(api_token, username, space_name, repo_url):
    """
    Create a new Hugging Face Space using the API
    """
    
    # HF API endpoint
    api_url = "https://huggingface.co/api/spaces"
    
    # Headers with authentication
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    # Space configuration
    space_config = {
        "name": space_name,
        "owner": username,
        "sdk": "gradio",
        "sdkVersion": "4.0.0",
        "pythonVersion": "3.10",
        "hardware": "cpu-basic",
        "license": "mit",
        "title": "Classical Computer Vision Algorithms",
        "description": "Interactive web interface for testing classical computer vision algorithms",
        "tags": ["computer-vision", "opencv", "gradio", "algorithms"],
        "private": False
    }
    
    try:
        # Create the space
        response = requests.post(api_url, headers=headers, json=space_config)
        
        if response.status_code == 201:
            print(f"✅ Successfully created Space: {username}/{space_name}")
            print(f"🌐 Space URL: https://huggingface.co/spaces/{username}/{space_name}")
            return True
        else:
            print(f"❌ Failed to create Space: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error creating Space: {e}")
        return False

def setup_github_integration(api_token, username, space_name, github_repo):
    """
    Set up GitHub integration for automatic deployment
    """
    
    # HF API endpoint for space settings
    api_url = f"https://huggingface.co/api/spaces/{username}/{space_name}/settings"
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    # GitHub integration settings
    github_config = {
        "github_repo": github_repo,
        "auto_deploy": True,
        "branch": "main"
    }
    
    try:
        response = requests.patch(api_url, headers=headers, json=github_config)
        
        if response.status_code == 200:
            print(f"✅ Successfully configured GitHub integration")
            print(f"🔗 Connected to: {github_repo}")
            return True
        else:
            print(f"❌ Failed to configure GitHub integration: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error configuring GitHub integration: {e}")
        return False

def main():
    """
    Main function to set up HF Space with GitHub integration
    """
    
    print("🚀 Setting up Hugging Face Space for Classical CV Project")
    print("=" * 60)
    
    # Configuration - Update these values
    HF_API_TOKEN = input("Enter your Hugging Face API token: ").strip()
    HF_USERNAME = input("Enter your Hugging Face username: ").strip()
    SPACE_NAME = input("Enter Space name (e.g., classical-cv-algorithms): ").strip()
    GITHUB_REPO = input("Enter GitHub repo URL (e.g., hxriharan/classical-cv): ").strip()
    
    if not all([HF_API_TOKEN, HF_USERNAME, SPACE_NAME, GITHUB_REPO]):
        print("❌ All fields are required!")
        return
    
    print("\n📋 Configuration:")
    print(f"HF Username: {HF_USERNAME}")
    print(f"Space Name: {SPACE_NAME}")
    print(f"GitHub Repo: {GITHUB_REPO}")
    print(f"Full Space URL: https://huggingface.co/spaces/{HF_USERNAME}/{SPACE_NAME}")
    
    confirm = input("\nProceed with this configuration? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ Setup cancelled")
        return
    
    print("\n🔄 Creating Hugging Face Space...")
    if create_hf_space(HF_API_TOKEN, HF_USERNAME, SPACE_NAME, GITHUB_REPO):
        print("\n🔄 Setting up GitHub integration...")
        if setup_github_integration(HF_API_TOKEN, HF_USERNAME, SPACE_NAME, GITHUB_REPO):
            print("\n🎉 Setup completed successfully!")
            print(f"\n📝 Next steps:")
            print(f"1. Push your code to GitHub: git push origin main")
            print(f"2. HF Space will automatically deploy from your GitHub repo")
            print(f"3. Monitor deployment at: https://huggingface.co/spaces/{HF_USERNAME}/{SPACE_NAME}")
            print(f"4. Your app will be available at: https://huggingface.co/spaces/{HF_USERNAME}/{SPACE_NAME}")
        else:
            print("\n⚠️ Space created but GitHub integration failed")
    else:
        print("\n❌ Failed to create Space")

if __name__ == "__main__":
    main() 