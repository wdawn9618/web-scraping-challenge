{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2dae3fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "import time as tm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e43d4aa9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def init_browser():\n",
    "    executable_path = {'executable_path': \"C:/Windows/chromedriver\"}\n",
    "    return Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0561e976",
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_info():\n",
    "    browser = init_browser()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3349a446",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18d07d72",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "tm.sleep(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e970027d",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9874add4",
   "metadata": {},
   "outputs": [],
   "source": [
    "soup.select('div')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e0b336f",
   "metadata": {},
   "outputs": [],
   "source": [
    "info = soup.find('li', class_='slide')\n",
    "contents = info.find_all('div', class_=\"content_title\")\n",
    "\n",
    "\n",
    "for content in contents:\n",
    "        news_title = content.text.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ecac8ade",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(news_title)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d81f37c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "info = soup.find('li', class_='slide')\n",
    "contents = info.find('div', class_='article_teaser_body')\n",
    "\n",
    "for content in contents:\n",
    "    news_paragraph = contents.text.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d95d6779",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(news_paragraph)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b1ef96a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "featured_image_url = 'https://spaceimages-mars.com/image/featured/mars3.jpg'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b1196d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_facts = 'https://galaxyfacts-mars.com/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "166e9313",
   "metadata": {},
   "outputs": [],
   "source": [
    "table = pd.read_html(mars_facts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdbd0519",
   "metadata": {},
   "outputs": [],
   "source": [
    "tab_df = table[0]\n",
    "tab_df = tab_df.rename(columns={1:'Mars', 0:' '})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b480e843",
   "metadata": {},
   "outputs": [],
   "source": [
    "tab_html = tab_df.to_html()\n",
    "tab_df.to_html('mars_table.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60f62269",
   "metadata": {},
   "outputs": [],
   "source": [
    "astro_url = 'https://marshemispheres.com/'\n",
    "browser.visit(astro_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51f57775",
   "metadata": {},
   "outputs": [],
   "source": [
    "use_html = browser.html\n",
    "\n",
    "soup2 = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "tm.sleep(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d5ad364",
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_images = [\n",
    "    {\"title\": \"Cerberus Hemisphere\", \"img_url\": \"https://marshemispheres.com/images/full.jpg\"},\n",
    "    {\"title\": \"Schiaparelli Hemisphere\", \"img_url\": \"https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg\"},\n",
    "    {\"title\": \"Syrtis_Major Hemisphere\", \"img_url\": \"https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg\"},\n",
    "    {\"title\": \"Valles_Marineris Hemisphere\", \"img_url\": \"https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg\"},\n",
    "]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2e24a90b",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-3-c78dfabef7a2>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-3-c78dfabef7a2>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    image_list = soup.find_all('a', class = 'itemLink product-item')\u001b[0m\n\u001b[1;37m                                    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "image_list = soup.find_all('a', class = 'itemLink product-item')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7d3f1fde",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-2-456592521cb2>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-2-456592521cb2>\"\u001b[1;36m, line \u001b[1;32m2\u001b[0m\n\u001b[1;33m    hrefs_list = list(set(hrefs_list))\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    " hrefs_list = [item.get('href') for item in field_item]\n",
    "    hrefs_list = list(set(hrefs_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8949e42-d782-49ae-bd8c-f8c4657529ea",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
