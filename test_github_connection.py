#!/usr/bin/env python3
"""
Test GitHub Connection
Tests if GitHub credentials are working correctly
"""

import asyncio
import os
import aiohttp
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_github_connection():
    """Test GitHub API connection with stored credentials"""
    token = os.getenv('GITHUB_TOKEN', '')
    repo_owner = os.getenv('GITHUB_REPO_OWNER', '')
    repo_name = os.getenv('GITHUB_REPO_NAME', '')
    
    if not all([token, repo_owner, repo_name]):
        logger.error("Missing GitHub credentials")
        return False
    
    logger.info(f"Testing connection to {repo_owner}/{repo_name}")
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'AjxAI-Trading-Platform'
    }
    
    async with aiohttp.ClientSession(headers=headers) as session:
        # Test repository access
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
        
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    repo_info = await response.json()
                    logger.info(f"✅ Repository access confirmed: {repo_info['full_name']}")
                    logger.info(f"📝 Description: {repo_info.get('description', 'No description')}")
                    logger.info(f"🔒 Private: {repo_info['private']}")
                    return True
                elif response.status == 404:
                    logger.error("❌ Repository not found - check repository name")
                elif response.status == 401:
                    logger.error("❌ Authentication failed - check GitHub token")
                else:
                    logger.error(f"❌ API error: {response.status}")
                    text = await response.text()
                    logger.error(f"Response: {text}")
        
        except Exception as e:
            logger.error(f"❌ Connection error: {e}")
    
    return False

if __name__ == "__main__":
    success = asyncio.run(test_github_connection())
    exit(0 if success else 1)