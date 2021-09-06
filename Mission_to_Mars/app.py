{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bdc5ef2a-9e63-47b7-981a-d91dc39c246e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-d66ec6f8c01a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mflask\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mFlask\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrender_template\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mredirect\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mflask_pymongo\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mPyMongo\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mscrape_mars\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\web-scraping-challenge\\Mission_to_Mars\\scrape_mars.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m   {\n\u001b[0;32m      4\u001b[0m    \u001b[1;34m\"cell_type\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"code\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m    \u001b[1;34m\"execution_count\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m    \u001b[1;34m\"id\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"d2dae3fb\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m    \u001b[1;34m\"metadata\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import scrape_mars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d7a97db3-48d2-4c06-b130-1b2eec3ec821",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask_pymongo in c:\\users\\owner\\anaconda3\\python\\lib\\site-packages (2.3.0)\n",
      "Requirement already satisfied: PyMongo>=3.3 in c:\\users\\owner\\anaconda3\\python\\lib\\site-packages (from flask_pymongo) (3.12.0)\n",
      "Requirement already satisfied: Flask>=0.11 in c:\\users\\owner\\anaconda3\\python\\lib\\site-packages (from flask_pymongo) (1.1.2)\n",
      "Requirement already satisfied: Werkzeug>=0.15 in c:\\users\\owner\\anaconda3\\python\\lib\\site-packages (from Flask>=0.11->flask_pymongo) (1.0.1)\n",
      "Requirement already satisfied: Jinja2>=2.10.1 in c:\\users\\owner\\anaconda3\\python\\lib\\site-packages (from Flask>=0.11->flask_pymongo) (2.11.3)\n",
      "Requirement already satisfied: click>=5.1 in c:\\users\\owner\\anaconda3\\python\\lib\\site-packages (from Flask>=0.11->flask_pymongo) (7.1.2)\n",
      "Requirement already satisfied: itsdangerous>=0.24 in c:\\users\\owner\\anaconda3\\python\\lib\\site-packages (from Flask>=0.11->flask_pymongo) (1.1.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\owner\\anaconda3\\python\\lib\\site-packages (from Jinja2>=2.10.1->Flask>=0.11->flask_pymongo) (1.1.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install flask_pymongo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c0edccf-dc38-418e-b1a8-c07afeea3365",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install scra"
   ]
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
