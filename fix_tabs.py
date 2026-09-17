import os
from bs4 import BeautifulSoup
import glob

def process_html_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        modified = False
        
        # Remove search box
        for div in soup.find_all('div', class_='search-wrapper'):
            div.decompose()
            modified = True
            
        # Remove shopping cart wrappers
        for div in soup.find_all('div', class_='shopping-cart-wrapper'):
            div.decompose()
            modified = True
            
        # Remove my account wrappers (login/register)
        for div in soup.find_all('div', class_='my-account-wrapper'):
            div.decompose()
            modified = True
            
        # Remove specific menu items
        menu_items = ['سبد خرید', 'پرداخت', 'حساب کاربری من', 'ورود/ثبت نام', 'ورود']
        for li in soup.find_all('li', class_='menu-item'):
            text = li.get_text(strip=True)
            if any(item in text for item in menu_items):
                li.decompose()
                modified = True
                
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
                
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    html_files = glob.glob('**/*.html', recursive=True)
    print(f"Found {len(html_files)} HTML files. Processing...")
    
    for filepath in html_files:
        process_html_file(filepath)
        
    print("Finished processing HTML files.")

if __name__ == '__main__':
    main()
