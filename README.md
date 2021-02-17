### Price Tracker
---

- This script scrapes a given website for whatever information you need to store and analyse, but it is optimized to do it for product prices
<br>

- The **database** is composed by a list of *products* and the *last time it was modified*
<br>

- For each **product** is stored its *name*, the *lowest registered price* and a list of all websites to get the data from (called *info*)
<br>

- The *info* is composed by the website *name* and its *scrapping data*
<br>

- **Scrapping data** is the information needed for access the website and find the needed information. It is composed by website *url*, *tag* (div, span ...), *attribute* (class, id ...) and the *value* of the attribute

- This information can be found using the developer tools `ctrl+shift+i`
<br>

- To run the program its simply by typing `python main.py` this *updates the price of all products*, but it can be used some **arguments** to manipulate the database, such as :

| Command | Arguments | Functionality                                               |
|:-------:|-----------|-------------------------------------------------------------|
| -p  | None | Prints the default database |
| -pn | \<filename\> | Prints the database with the pathname \<filename\> |
| -up | None | Updates and Prints the default database | 
| -fr | None | Force resents the database (doesn't save a copy of the old one) |
| -r  |  \<filename\> | Resets the database storing the old one at \<filename\> 
| -rp | \<ProductName\> | Removes the product named \<ProductName\> from the database \<ProductName\> |
| -ri | \<ProductName\> \<InfoName\> | Removes the info named \<InfoName\> from the product named \<ProductName\> stored at the database | 
| -ap | \<ProductName\> | Adds a product whose name is \<ProductName\> to the database |
| -ai | \<ProductName\> \<InfoName\> | Add new info to the product with the name \<ProductName\> |
| -as | \<ProductName\> \<InfoName\> \<url\> \<tag\> \<attr\> \<val\> | Links the scrapping data to the info \<InfoName\> |

A web scraper that aims to track the price variation of a given product

