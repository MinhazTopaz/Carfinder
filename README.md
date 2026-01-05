# CarFinder

A multi-site car listing aggregator that searches for vehicles across multiple platforms including Kijiji Autos, AutoTrader, and Facebook Marketplace.

## Features

- 🔍 Search multiple car listing websites simultaneously
- 🚗 Filter by make and model
- 📍 Optional location filtering
- 🚀 Parallel scraping for faster results
- 📊 Organized results by source

## Supported Websites

- **Kijiji Autos** - Full support for car listings
- **AutoTrader** - Full support for car listings
- **Facebook Marketplace** - Limited support (requires JavaScript rendering for full functionality)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MinhazTopaz/Carfinder.git
cd Carfinder
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Search

Search for a car by make and model:

```bash
python carfinder.py Honda Civic
```

### Search with Location

Add location filtering:

```bash
python carfinder.py Toyota Camry --location Toronto
```

### Sequential Mode

Run scrapers one at a time (useful for debugging):

```bash
python carfinder.py Ford F-150 --sequential
```

## Command Line Options

```
python carfinder.py <make> <model> [options]

Positional arguments:
  make                  Car make (e.g., Honda, Toyota, Ford)
  model                 Car model (e.g., Civic, Camry, F-150)

Optional arguments:
  -h, --help           Show help message
  --location, -l       Location to search in
  --sequential, -s     Run scrapers sequentially instead of in parallel
```

## Examples

```bash
# Search for Honda Civic
python carfinder.py Honda Civic

# Search for Toyota Camry in Toronto
python carfinder.py Toyota Camry --location Toronto

# Search for Ford F-150 in British Columbia
python carfinder.py Ford F-150 --location "British Columbia"

# Search for Mazda 3 (sequential mode)
python carfinder.py Mazda 3 --sequential
```

## Project Structure

```
Carfinder/
├── carfinder.py              # Main CLI application
├── aggregator.py             # Aggregator combining all scrapers
├── models.py                 # Data models for car listings
├── base_scraper.py           # Base scraper class
├── kijiji_scraper.py         # Kijiji Autos scraper
├── autotrader_scraper.py     # AutoTrader scraper
├── facebook_scraper.py       # Facebook Marketplace scraper
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## How It Works

1. **Input**: You provide a car make and model (e.g., "Honda Civic")
2. **Parallel Scraping**: The aggregator sends requests to multiple websites simultaneously
3. **Data Extraction**: Each scraper extracts relevant information:
   - Title
   - Price
   - Year
   - Mileage
   - Location
   - URL
   - Description
4. **Results**: All listings are combined and displayed organized by source

## Important Notes

### Web Scraping Considerations

- **Respectful Scraping**: The scrapers include delays between requests to avoid overloading servers
- **Terms of Service**: Always check and comply with each website's Terms of Service
- **Rate Limiting**: Heavy usage may result in temporary IP blocks
- **Structure Changes**: Websites may change their HTML structure, requiring scraper updates

### Facebook Marketplace

Facebook Marketplace heavily relies on JavaScript for rendering content. The current implementation provides basic structure but may return limited or no results. For full Facebook Marketplace support, consider:

1. Using Selenium or Playwright for JavaScript rendering
2. Implementing proper authentication
3. Handling dynamic content loading

## Future Enhancements

- [ ] Add more car listing websites
- [ ] Implement Selenium support for JavaScript-heavy sites
- [ ] Add filtering by price range, year, mileage
- [ ] Export results to CSV/JSON
- [ ] Web interface using Flask or FastAPI
- [ ] Database storage for historical price tracking
- [ ] Email notifications for new listings
- [ ] Advanced search filters (transmission, fuel type, etc.)

## Troubleshooting

### No results returned

- Some websites require JavaScript rendering (especially Facebook)
- Website structure may have changed
- Try using the `--sequential` flag to see detailed error messages
- Check your internet connection

### Rate limiting / blocked requests

- Add delays between searches
- Use a VPN or different IP address
- Check if the website has an official API

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is provided as-is for educational purposes. Please respect the Terms of Service of all websites you scrape.

## Disclaimer

This tool is for educational and personal use only. Users are responsible for complying with all applicable laws and website Terms of Service. The developers are not responsible for any misuse of this tool.