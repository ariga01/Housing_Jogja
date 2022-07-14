# _**Housing Market Analysis in Yogyakarta**_

## About This Project

The needs for shelter is extremely important. In order to fulfill this need, people are willing the extra miles to get it. This project is intended to give people insight about the housing market in Yogyakarta. This include possible factors that push the price, area with cheaper price, variance in price, and calculation of price/ salary ratio for certain area.

## Objective

- Find the factors affecting house price
- Show area's median price
- Find interesting insight out of the data

## Workflow

- Webscrape the data from certain site
- Clean the data
- Process and analyze the data
- Make visualization in Tableau

## Discussion

For this project, I use data from the following location:

- Yogyakarta City
- Sleman Regency
- Bantul Regency
- Gunung Kidul Regency
- Kulon Progo Regency

Yogyakarta Province is divided into 5 areas as outline above. In order to maximize the search result, separate areas' links are needed because the way OLX query their data from the database. If we use one link, that is for Yogyakarta Province, the end results will be extremely limited.

The raw data contain so much dirty data, and we need extensive cleaning for this. For now, we can only get basic cleaning in python and make specific cleaning in Tableau, for key metrics such as minimum value.

During visualization process, I need to exclude few outliers data to make the data more normal. Usually, the reason why the data may contain outliers is because faulty data is still being included in the final process.

## Results

After analyzing the data, I concluded that:

- Certain location in Depok has the highest median price/m2 compared to other location
- Even under one location, price/m2 may vary quite aggresively
- The price for housing extremely high considering the average salary in Yogyakarta
- Selective location picking can be extremely crucial for average worker in Yogyakarta
