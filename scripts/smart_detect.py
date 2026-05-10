import re
import sys

def detect_platform(url):
    url = url.lower()
    patterns = {
        'youtube': r'(youtube\.com|youtu\.be)',
        'instagram': r'instagram\.com',
        'twitter': r'(twitter\.com|x\.com)',
        'telegram': r't\.me',
        'aparat': r'aparat\.com',
        'spotify': r'spotify\.com',
        'soundcloud': r'soundcloud\.com',
        'reddit': r'reddit\.com',
        'tiktok': r'tiktok\.com',
        'webpage': r'^https?://[^\s]+$'
    }
    for platform, pattern in patterns.items():
        if re.search(pattern, url):
            print(platform)
            return
    print('direct')

if __name__ == "__main__":
    detect_platform(sys.argv[1])
