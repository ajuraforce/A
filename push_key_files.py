#!/usr/bin/env python3
"""
GitHub Key Files Push Script
Pushes important files to GitHub repository in smaller batches
"""

import asyncio
import os
import aiohttp
import base64
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GitHubUploader:
    def __init__(self):
        self.github_token = os.getenv('GITHUB_TOKEN', '')
        self.repo_owner = os.getenv('GITHUB_REPO_OWNER', '')
        self.repo_name = os.getenv('GITHUB_REPO_NAME', '')
        self.branch = 'main'
        self.api_base = 'https://api.github.com'
    
    async def upload_file(self, session, file_path, content):
        """Upload a single file to GitHub"""
        try:
            content_b64 = base64.b64encode(content.encode('utf-8')).decode()
            
            url = f"{self.api_base}/repos/{self.repo_owner}/{self.repo_name}/contents/{file_path}"
            
            # Check if file exists to get SHA
            sha = None
            async with session.get(url) as response:
                if response.status == 200:
                    file_info = await response.json()
                    sha = file_info['sha']
            
            # Prepare commit data
            commit_data = {
                'message': f'Update {file_path} - AjxAI Trading Platform',
                'content': content_b64,
                'branch': self.branch
            }
            
            if sha:
                commit_data['sha'] = sha
            
            # Upload file
            async with session.put(url, json=commit_data) as response:
                if response.status in [200, 201]:
                    logger.info(f"✅ Uploaded: {file_path}")
                    return True
                else:
                    error_text = await response.text()
                    logger.error(f"❌ Failed to upload {file_path}: {response.status} - {error_text}")
                    return False
                    
        except Exception as e:
            logger.error(f"❌ Error uploading {file_path}: {e}")
            return False

    async def push_key_files(self):
        """Push key files to GitHub"""
        # Define important files to upload
        key_files = [
            'app.py',
            'config.json',
            'permissions.json',
            'replit.md',
            'requirements.txt',
            'utils/github_backup.py',
            'static/js/dashboard-react.js',
            'static/js/portfolio.js',
            'static/js/analysis.js',
            'static/js/trades.js',
            'static/js/alerts.js',
            'static/js/screening.js',
            'static/js/backtesting.js',
            'static/js/community.js',
            'static/js/settings.js',
            'templates/dashboard.html',
            'templates/alerts.html',
            'templates/trades.html',
            'templates/portfolio.html',
            'templates/analysis.html',
            'templates/screening.html',
            'templates/backtesting.html',
            'templates/community.html',
            'templates/settings.html'
        ]
        
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'AjxAI-Trading-Platform'
        }
        
        uploaded_count = 0
        
        async with aiohttp.ClientSession(headers=headers) as session:
            for file_path in key_files:
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        success = await self.upload_file(session, file_path, content)
                        if success:
                            uploaded_count += 1
                        
                        # Small delay to avoid rate limiting
                        await asyncio.sleep(0.5)
                        
                    except Exception as e:
                        logger.error(f"❌ Error reading {file_path}: {e}")
                else:
                    logger.warning(f"⚠️  File not found: {file_path}")
        
        return uploaded_count

async def main():
    """Main function"""
    uploader = GitHubUploader()
    
    logger.info("🚀 Starting GitHub key files upload...")
    logger.info(f"📁 Repository: {uploader.repo_owner}/{uploader.repo_name}")
    
    uploaded_count = await uploader.push_key_files()
    
    if uploaded_count > 0:
        logger.info(f"✅ Successfully uploaded {uploaded_count} files to GitHub!")
        logger.info(f"🔗 View at: https://github.com/{uploader.repo_owner}/{uploader.repo_name}")
    else:
        logger.error("❌ No files were uploaded")
    
    return uploaded_count > 0

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)