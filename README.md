# 🔍 Internshala Scraper

A Python web scraper that automatically extracts internship listings from Internshala, including job titles, companies, locations, stipends, required skills, and application links. Export to CSV for easy filtering and analysis.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

## 📋 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Output Format](#output-format)
- [Troubleshooting](#troubleshooting)
- [Limitations](#limitations)
- [License](#license)
- [Contact](#contact)

## ✨ Features

- 🔍 **Automated Scraping** - Extract hundreds of internships in seconds
- 📄 **Multi-page Support** - Scrape across multiple pages with pagination
- 📊 **CSV Export** - Save structured data for easy analysis
- 🎯 **Comprehensive Data** - Title, company, location, stipend, skills, links
- ⚡ **Fast & Efficient** - Respectful delays to avoid overloading servers
- 🛡️ **Error Handling** - Robust error management for reliable scraping
- 📈 **Summary Statistics** - View top companies, locations, and compensation
- 🎨 **Clean Output** - Formatted console output with progress indicators

### Data Extracted

For each internship:
- ✅ Job Title
- ✅ Company Name
- ✅ Location
- ✅ Stipend/Salary
- ✅ Required Skills
- ✅ Application Link

## 🎬 Demo

```
============================================================
🚀 INTERNSHALA SCRAPER
============================================================

🔍 Searching for 'python' internships...
📍 Location: All India
📄 Pages to scrape: 5

Scraping page 1...
✅ Found 40 internships on page 1

✅ Total internships scraped: 200

💾 Saving to internshala_python_20250104.csv...
✅ Successfully saved 200 internships
```

## 🚀 Installation

### Prerequisites
- Python 3.7+
- pip

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/KushalJain-00/internshala-scraper.git
   cd internshala-scraper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper**
   ```bash
   python Internshala_Scraper.py
   ```

## 📖 Usage

### Basic Usage

```bash
python Internshala_Scraper.py
```

Enter filename when prompted or press Enter for auto-generated name.

### Customize Search

Edit configuration in `Internshala_Scraper.py`:

```python
search_query = "python"      # "data-analyst", "web-development", etc.
location = ""                # "" for all, or "mumbai", "bangalore"
pages = 7                    # Number of pages (40 results per page)
```

## 📊 Output Format

CSV with columns:
- type, title, company, location, salary, experience, duration, skills, link, source

Example:
```csv
type,title,company,location,salary,skills
Internship,Python Developer,TCS,Mumbai,₹10000/mo,"Python, Django, SQL"
```

## 🔧 Troubleshooting

**No internships found:**
- Try different search query
- Check internet connection
- Verify Internshala is accessible

**Import errors:**
```bash
pip install requests beautifulsoup4 lxml pandas
```

**Rate limiting:**
- Wait a few minutes
- Don't reduce the 2-second delay

## ⚠️ Limitations

- Duration field shows "N/A" (HTML structure limitation)
- Requires internet connection
- May break if Internshala updates website
- Use responsibly - respect rate limits

## 🛠️ Technology Stack

- Python 3.7+
- Requests - HTTP requests
- BeautifulSoup4 - HTML parsing
- lxml - XML/HTML parser
- CSV - Data export

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 👨‍💻 Contact

**Kushal Jain**
- GitHub: [@KushalJain-00](https://github.com/KushalJain-00)
- LinkedIn: [Kushal Jain](https://www.linkedin.com/in/kushal-jain-855293376)
- Email: harshilkushal100@gmail.com

## ⭐ Support

Star this repo if helpful! Report bugs via [issues](https://github.com/KushalJain-00/internshala-scraper/issues).

---

**Happy Job Hunting!** 🎯
