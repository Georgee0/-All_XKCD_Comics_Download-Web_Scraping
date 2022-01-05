# -All_XKCD_Comics_Download-Web_Scraping

Here’s what your program does:

1. Loads the XKCD home page
2. Saves the comic image on that page
3. Follows the Previous Comic link
4. Repeats until it reaches the first comic

This means your code will need to do the following:

1. Download pages with the requests module.
2. Find the URL of the comic image for a page using Beautiful Soup.Web Scraping 287
3. Download and save the comic image to the hard drive with
iter_content().
4. Find the URL of the Previous Comic link, and repeat.
