import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import csv

base_url = 'https://internshala.com/internships/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

def scrape_internshala(search_query = "python" , location = "" , pages = 1):

    internships = []

    print(f"Searching for '{search_query}' internships...")
    print(f"Location: {location if location else 'All India'}")
    print(f"Pages to scrape: {pages}\n")

    for page in range(1, pages+1):
        print(f"Scraping page {page} .....")

        if page == 1:
            url = f"{base_url}/{search_query}-internship"
        else:
            url = f"{base_url}/{search_query}-internship/page-{page}"

        if location:
            url += f"/{location}"

        try:
            response = requests.get(url , headers = headers)

            if response.status_code != 200:
                print(f"❌ Error: Got status code {response.status_code}")
                continue

            soup = BeautifulSoup(response.text , 'lxml')

            cards = soup.find_all('div' , class_ = 'internship_meta duration_meta')

            if not cards:
                print(f"No internships found on page {page}")
                continue
            print(f"✅ Found {len(cards)} internships on page {page}")

            for card in cards:
                try:
                    internship = extract_internship_data(card)
                    if internship:
                        internships.append(internship)
                except Exception as e:
                    print(f"Error extracting internship: {e}")
                    continue
            time.sleep(2)

        except Exception as e:
            print(f"❌ Error scraping page {page}: {e}")
            continue
    
    print(f"\n✅ Total internships scraped: {len(internships)}")
    return internships

def extract_internship_data(card):
    
    try:
        title_tag = card.find('h3')  
        title = title_tag.text.strip() if title_tag else "N/A"
        
        company_tag = card.find('p', class_='company-name')
        company = company_tag.text.strip() if company_tag else "N/A"
        
        location_tag = card.find('div', class_='row-1-item locations')
        location = location_tag.text.strip() if location_tag else "N/A"
        
        stipend_tag = card.find('span', class_='stipend')
        stipend = stipend_tag.text.strip() if stipend_tag else "Unpaid"

        duration_tag = card.find('div' , class_='row-1-item')
        duration = duration_tag.text.strip() if duration_tag else "N/A"

        skill_tag = card.find('div' , class_='job_skills')
        skills = skill_tag.text.strip().replace('\n', ', ') if skill_tag else "N/A"

        link_tag = card.find('a')
        link = "https://internshala.com" + link_tag.get('href') if link_tag else "N/A"
        
        
        internship = {
            'type': 'Internship',
            'title': title,
            'company': company,
            'location': location,
            'salary': stipend,
            'experience': 'Fresher',
            'duration': duration,
            'link': link,
            'skills':skills,
            'source': 'Internshala'
        }
        
        return internship
        
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None
    
def save_to_csv(internships, filename = "internships.csv"):
    
    if not internships:
        print("No data to save!")
        return
    
    print(f"\n Saving to {filename}...")
    
    
    fieldnames = ['type', 'title', 'company', 'location', 'salary', 
                  'experience', 'duration', 'skills' , 'link', 'source']
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            
            writer.writeheader()
            
            
            for internship in internships:
                writer.writerow(internship)
        
        print(f"✅ Successfully saved {len(internships)} internships to {filename}")
        
    except Exception as e:
        print(f"❌ Error saving to CSV: {e}")

def main():

    print("\n" + "="*60)
    print(" INTERNSHALA SCRAPER ")
    print("="*60 + "\n")
    
    # Configuration
    search_query = "python"
    location = ""
    pages = 7
    filename = input("Enter the output CSV filename (or press Enter for default): ")    
    internships = scrape_internshala(search_query, location, pages)
    
    if internships:
        save_to_csv(internships, filename)
    else:
        print("\nNo internships found!")
    
    print("\n✅ Scraping complete!")

if __name__ == "__main__":
    main()

