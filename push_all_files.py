#!/usr/bin/env python3
"""
Complete GitHub Push Script
Pushes ALL files from the current codebase to GitHub repository
"""

import asyncio
import os
import aiohttp
import base64
import logging
from datetime import datetime
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CompleteGitHubUploader:
    def __init__(self):
        self.github_token = os.getenv('GITHUB_TOKEN', '')
        self.repo_owner = os.getenv('GITHUB_REPO_OWNER', '')
        self.repo_name = os.getenv('GITHUB_REPO_NAME', '')
        self.branch = 'main'
        self.api_base = 'https://api.github.com'
        
        # Files/directories to skip (binary/large files and sensitive data)
        self.skip_patterns = [
            '.git',
            '__pycache__',
            '.cache',
            '.pythonlibs',
            '.uv',
            'node_modules',
            '*.pyc',
            '*.log',
            'patterns.db',
            'state.json',
            '.env'
        ]
        
        # Binary file extensions to handle differently
        self.binary_extensions = [
            '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico',
            '.pdf', '.zip', '.tar', '.gz', '.db', '.sqlite',
            '.bin', '.exe', '.dll', '.so'
        ]
    
    def should_skip_file(self, file_path):
        """Check if file should be skipped"""
        for pattern in self.skip_patterns:
            if pattern in file_path or file_path.endswith(pattern.replace('*', '')):
                return True
        return False
    
    def is_binary_file(self, file_path):
        """Check if file is binary"""
        _, ext = os.path.splitext(file_path.lower())
        return ext in self.binary_extensions
    
    async def upload_file(self, session, file_path, content, is_binary=False):
        """Upload a single file to GitHub"""
        try:
            if is_binary:
                content_b64 = base64.b64encode(content).decode()
            else:
                content_b64 = base64.b64encode(content.encode('utf-8')).decode()
            
            url = f"{self.api_base}/repos/{self.repo_owner}/{self.repo_name}/contents/{file_path}"
            
            # Check if file exists to get SHA
            sha = None
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        file_info = await response.json()
                        sha = file_info['sha']
            except:
                pass  # File doesn't exist yet
            
            # Prepare commit data
            commit_data = {
                'message': f'Update {file_path} - Complete AjxAI codebase push',
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

    async def push_all_files(self):
        """Push all files to GitHub"""
        
        # Validate configuration
        if not all([self.github_token, self.repo_owner, self.repo_name]):
            logger.error("❌ Missing GitHub configuration. Check GITHUB_TOKEN, GITHUB_REPO_OWNER, GITHUB_REPO_NAME")
            return False
        
        logger.info("🚀 Starting complete codebase push to GitHub...")
        logger.info(f"📁 Repository: {self.repo_owner}/{self.repo_name}")
        logger.info(f"🌿 Branch: {self.branch}")
        
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'AjxAI-Complete-Upload'
        }
        
        uploaded_count = 0
        failed_count = 0
        
        async with aiohttp.ClientSession(headers=headers, timeout=aiohttp.ClientTimeout(total=300)) as session:
            
            # Collect all files first
            all_files = []
            for root, dirs, files in os.walk('.'):
                # Filter out skip directories
                dirs[:] = [d for d in dirs if not any(skip in d for skip in self.skip_patterns)]
                
                for file in files:
                    file_path = os.path.join(root, file).replace('./', '').replace('\\', '/')
                    
                    if not self.should_skip_file(file_path):
                        all_files.append(file_path)
            
            logger.info(f"📊 Found {len(all_files)} files to upload")
            
            # Upload files in batches to avoid rate limiting
            batch_size = 10
            for i in range(0, len(all_files), batch_size):
                batch = all_files[i:i + batch_size]
                
                # Process batch
                for file_path in batch:
                    try:
                        if os.path.exists(file_path):
                            is_binary = self.is_binary_file(file_path)
                            
                            if is_binary:
                                with open(file_path, 'rb') as f:
                                    content = f.read()
                            else:
                                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                    content = f.read()
                            
                            success = await self.upload_file(session, file_path, content, is_binary)
                            if success:
                                uploaded_count += 1
                            else:
                                failed_count += 1
                        
                    except Exception as e:
                        logger.error(f"❌ Error processing {file_path}: {e}")
                        failed_count += 1
                
                # Small delay between batches
                if i + batch_size < len(all_files):
                    await asyncio.sleep(2)
                    logger.info(f"⏳ Processed {min(i + batch_size, len(all_files))}/{len(all_files)} files...")
        
        logger.info(f"✅ Upload complete!")
        logger.info(f"📊 Successfully uploaded: {uploaded_count} files")
        if failed_count > 0:
            logger.warning(f"⚠️  Failed uploads: {failed_count} files")
        logger.info(f"🔗 View at: https://github.com/{self.repo_owner}/{self.repo_name}")
        
        return uploaded_count > 0

async def main():
    """Main function"""
    uploader = CompleteGitHubUploader()
    success = await uploader.push_all_files()
    return success

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)