#!/usr/bin/env python3
"""
GitHub Code Push Script
Pushes the current codebase to GitHub repository
"""

import asyncio
import logging
from utils.github_backup import GitHubBackup

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def main():
    """Push current code to GitHub repository"""
    backup = GitHubBackup()
    
    logger.info("🚀 Starting GitHub code push...")
    
    # Validate configuration
    if not backup.validate_config():
        logger.error("❌ GitHub configuration is invalid")
        logger.error("Please check your GITHUB_TOKEN, GITHUB_REPO_OWNER, and GITHUB_REPO_NAME secrets")
        return False
    
    logger.info(f"📁 Repository: {backup.repo_owner}/{backup.repo_name}")
    logger.info(f"🌿 Branch: {backup.branch}")
    
    # Push source code
    success = await backup.push_source_code(
        commit_message="Updated AjxAI Trading Platform with responsive navigation - Full codebase sync"
    )
    
    if success:
        logger.info("✅ Code successfully pushed to GitHub!")
        logger.info(f"🔗 View at: https://github.com/{backup.repo_owner}/{backup.repo_name}")
    else:
        logger.error("❌ Failed to push code to GitHub")
        
    return success

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)