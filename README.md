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

The Kijiji data model is relatively simple and is contained within a single python object: Kijiji(). The simplicity of this object makes the majority of is processes self explanatory from internal documentation. That being said there are two main key methods who's processes should be described:

#### 1. The href parser method: Kijiji.href_parser(href)

#### 2. The page to dataframe method: Kijiji.page_to_dataframe(url)


