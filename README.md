# ETL Data Models
This repository is a collection of various data models that I have written for use in other data pipelines and database normalization processes. These data models span a wide range of applications and are refrenced in many of my other ETL projects. I have simply aggregated them here for convenience.

The main purpose of this repository is for me to document the processes of each data model and how they were integrated into my data pipelines as a way of ensuring that I am able to return to and maintain my pipelines

## Table of Contents
* [Online Real Estate Listings Data Models](https://github.com/MatthewTe/ETL-Data-Models/blob/master/README.md#online-real-estate-data-models)


## Online Real Estate Data Models
Most of these data models revolve around the extraction of raw data from online Real Estate listings websites. These models were used to build the main database used in the [Real Estate Listings Data Pipeline](https://github.com/MatthewTe/Public-Real-Estate-Listings-Data-Pipeline).

### Kijiji.ca Listings Data Model
[Kijiji.ca](https://www.kijiji.ca) is a canadian online store where users can post listings for item the wish to sell. There are many Real Estate listings from users attempting to sell or rent Real Estate. This model was built as a means of extracting raw data directly from Kijiji's public Real Estate listings data based on common python webscraping packages such as Beautiful Soup and requests.

#### Kijiji Webpage Structure
A Kijiji listings page is structured as such:
![Image Not Found](https://github.com/MatthewTe/ETL-Data-Models/blob/master/resources/Kijiji%20listings%20example.PNG "Example of a Kijiji Real Estate listings page")


With each individual listing having a listings page in the format shown below, navigated to via an embeded href link within the titles of each listing on the listings page shown above:

![Image Not Found](https://github.com/MatthewTe/ETL-Data-Models/blob/master/resources/Kijiji%20Individual%20Listing%20example.PNG "Example of an individual listings page")

The Kijiji data model is relatively simple and is contained within a single python object: Kijiji(). The simplicity of this object makes the majority of is processes self explanatory from internal documentation. That being said there is one unorthodox processes should be described:

#### *The href parser method: Kijiji.href_parser(href)

The in-depth function of the href method can be understood by reading the internal method documentation. The main goal of the method is to extract the key raw data about an individual listing given a link to its main page. The raw data it extracts are:
* Address
* Price
* Number of Bedrooms
* Number of Bathrooms
* Size in SquareFeet

The Address and Price data are self explanatory and are nested within easily searchable html tags with bs4. The issue arrises with the remaining three data points. A user must enter a price and an address to post a listing, making web scraping very simple. The remaining attributes are optional and can be posted with no specific order within the relevant attribute tags. This can complicate scraping as the orders of each attribute may change or not be there at all. Preventing the text from a specific attribute containter to simply be scraped and assinged to a variable as is the case with Address for example.

The method solves this problem in the following way:

```python
# Number of Beds, Bathrooms and Square Feet:
        attribute_tags = soup.findAll('dt', {'class': 'attributeLabel-240934283'})
        attribute_values = soup.findAll('dd', {'class': 'attributeValue-2574930263'})

        # Creating a dictionary that will store the various attributes independent
        # of there listing order on the website:
        attributes_dict = {}

        # Itterative loop appending attribute data to attributes_dict:
        counter = 0 # Counter to track attribute_values in loop
        for attribute in attribute_tags:

            attribute_instance = {attribute.text : attribute_values[counter].text}

            counter = counter + 1

            # adding values to main dict:
            attributes_dict.update(attribute_instance)
```

By building a dictionary that stores the attribute values and assigns them to attribute keys in the unqiue order that they are scraped from each page ensures that a change in attribute order from page to page does not create errors with webscraping as each attribute is stored based on its current order and the values can be retrived using the dict keys.     
