#

import requests, os, bs4

url = 'http://xkcd.com'         # starting url
os.makedirs('xkcd', exist_ok=True ) # stores comics in xkcd
while not url.endswith('#'):

# Download the page
    print('Downloading page %s.....' %url)    
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # find the URL of the comic image
    comicElems = soup.select('#comic img')
    if comicElems == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElems[0].get('src')

# Download the image.
        print('Downloading image %s.....' %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

# Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')    
        for chunk in res.iter_content(10000):
            imageFile.write(chunk)
        imageFile.close()    

# Getting the previous button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done')    