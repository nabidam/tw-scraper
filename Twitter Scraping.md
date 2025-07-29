- ([ref](https://github.com/JustAnotherArchivist/snscrape/issues/1057)) The Twitter scrapers have been broken for a long while. Almost everything requires authentication now, which won't be implemented. See [#996](https://github.com/JustAnotherArchivist/snscrape/issues/996) and [#1037](https://github.com/JustAnotherArchivist/snscrape/issues/1037).
- To add, X.com page HTML is dynamic and complex making parsing scraped content very difficult. So, the best approach to scrape Twitter is to use a headless browser and capture background requests that download the Tweet and user data.
	- Playwright
	- Scrapfly
- rebuild scraping posts:

install python packages:
```bash
pip install playwright jmespath scrapfly-sdk
```
then you should install playwright browser files:
```bash
playwright install
```
maybe it got error:
```bash
some missing .so files (dependencies)
```
in my system it misses these packages (because it is Arch and Arch is not supported officially by Playwright):
- libicudata.so.66
- libicui18n.so.66
- libicuuc.so.66
- libwebp.so.6
- libffi.so.7
the solution was installing `libffi7` through AUR, but other packages is not in aur or any arch-based repo. so we can install them from their .deb sources (from ubuntu).
```bash
wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu66_66.1-2ubuntu2_amd64.deb
dpkg-deb -x libicu66_66.1-2ubuntu2_amd64.deb .

wget http://archive.ubuntu.com/ubuntu/pool/main/libw/libwebp/libwebp6_0.6.1-2_amd64.deb
dpkg-deb -x libwebp6_0.6.1-2_amd64.deb .

cp ./usr/lib/x86_64-linux-gnu/libicu*.so.66* .  
cp ./usr/lib/x86_64-linux-gnu/libwebp.so.6* .  
cp ./usr/lib/x86_64-linux-gnu/libwebp.so.6* .

# then you should export the path as LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/playwright-libs:$LD_LIBRARY_PATH

# for making it persistant
echo 'export LD_LIBRARY_PATH=$HOME/playwright-libs:$LD_LIBRARY_PATH' >> ~/.zshrc
```

then you can run `playwright install` and it would install chromium core.

for setting proxy on pw you can do like this:
```python
browser = pw.chromium.launch(headless=False, proxy={
	"server": "http://127.0.0.1:2080"
})
```

also you may want to increase timeout value:
```python
context.set_default_timeout(60000) # in milisecond
```

- Use 3rd party tools: [Apify](https://apify.com/apidojo/twitter-scraper-lite), [Apify](https://apify.com/apidojo/tweet-scraper) 