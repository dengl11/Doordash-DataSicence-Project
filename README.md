# Doordash Data Science Project
> Li Deng  08.08.2019  

Github: https://github.com/dengl11/Doordash-DataSicence-Project
- From there you can see my step-by-step implementation
- Will make it private after being reviewed by Doordash engineers

## Part 1
1. Model
Using a simple **linear regression** model in *sklearn*

2. Model Evaluation
Train-test split the historical data, and compute MSE

3. Data Preprocessing
	- compute the generated column `delivery_seconds` from  `actual_deliverty_time`  and `created_at` 
	- remove the entries where `actual_deliverty_time` or `created_at` is `nan`
	- label-encode the categorical column `store_primary_category` (a better way is to use one-hot encoding)
	- choose the features used for training, and remove other columns
	- fill `nan`  with the **mode** in categorical columns, **median** in numerical columns

4. Finding
From the coefficients of the linear regression model:

```
num_distinct_items                                : 15.03
total_items                                       : -4.89
total_onshift_dashers                             : -2.47
total_outstanding_orders                          : 2.33
total_busy_dashers                                : -1.93
estimated_order_place_duration                    : 0.96
store_primary_category                            : 0.76
max_item_price                                    : 0.11
estimated_store_to_consumer_driving_duration      : 0.10
min_item_price                                    : 0.02
subtotal                                          : 0.01
```

- `num_distinct_items ` is the dominant t factor for delivery time; the more `num_distinct_items `, the longer the delivery time, which makes sense;
- `total_onshift_dashers` is also important; the more dashers on shift, the shorter delivery time, which also makes sense
- `total_outstanding_orders `: is also important; the more outstanding orders to deal with, the longer the delivery time



## Part 2
Output dataframe to `./output/predictions.tsv`


## If I have more time…
- Further debug to catch out potential bugs
