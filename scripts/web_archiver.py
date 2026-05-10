import sys
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def save_as_mhtml(url, output_dir, wait_seconds=8):
    os.makedirs(output_dir, exist_ok=True)
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    
    if os.path.exists('/usr/bin/chromium-browser'):
        chrome_options.binary_location = '/usr/bin/chromium-browser'
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        print(f"🌐 Loading: {url}")
        driver.get(url)
        time.sleep(int(wait_seconds))
        
        mhtml = driver.execute_cdp_cmd('Page.captureSnapshot', {})
        
        domain = url.split('/')[2].replace('.', '_')
        timestamp = int(time.time())
        filename = f"{domain}_{timestamp}.mhtml"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(mhtml)
        
        print(f"✅ Saved: {filepath}")
        print(f"📦 Size: {len(mhtml) // 1024} KB")
        
        info_path = os.path.join(output_dir, f"{domain}_{timestamp}_info.txt")
        with open(info_path, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Date: {time.ctime(timestamp)}\n")
            f.write(f"File: {filename}\n")
        
        return filepath
    except Exception as e:
        print(f"❌ Error: {e}")
        return None
    finally:
        driver.quit()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python archiver.py <URL> <output_dir> [wait_seconds]")
        sys.exit(1)
    save_as_mhtml(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '8')
