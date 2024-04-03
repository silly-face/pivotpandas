# Databricks notebook source
import pandas as pd
from texts import presentation
from presentationtools import printt, show_image
from typing import Optional
import numpy as np
from time import sleep

# COMMAND ----------

printt(presentation['WELCOME'])
show_image(presentation["panda_img"])

# COMMAND ----------
printt(presentation["FUNFACT"])


# COMMAND ----------
printt(presentation["OUTLINE"])

# COMMAND ----------
printt(presentation["PIVOT"])
sleep(5)
show_image(presentation["pivot_gif"])


# COMMAND ----------
def create_daily_json_for_trend_analyzer(df: pd.DataFrame, metrics_to_send: list[dict], granularity: Optional[str] = None) -> pd.DataFrame:
    """
    Function to create the daily json for the creative data. This is input for the line chart within the cards.
    The function looks slow, but so far it is the fastest way to create the daily json and seems to perform well enough.

    Input:
        df: pd.DataFrame
        metrics_to_send: list, The metrics that are being send to the frontend. Should be created from Metric class.
        granularity: str, The granularity (e.g. per day / week / ...) If None, it will use the default granularity of the dataset.

    Returns:
        output: dict with format
         {
            'id1': {
                'metric1': [{'date': '2021-01-01', 'value': 10}, ...],
                'metric2': [{'date': '2021-01-01', 'value': 20}, ...],
                ...
            },
            'id2': {
                'metric1': [{'date': '2021-01-01', 'value': 10}, ...],
                'metric2': [{'date': '2021-01-01', 'value': 20}, ...],
                ...
            },
            ...
    """

    # the group_metrics are the ones that are not derived by division
    group_metrics = [metric['name']for metric in metrics_to_send if metric.get('denominator') is None]
    metric_names = [metric['name'] for metric in metrics_to_send]

    # Group daily values to a set granularity
    #df, _ = group_dataframe(df=df, date_column='date', group_cols=['id'],
    #                        target_columns=group_metrics, force_freq=granularity)

    df = df.groupby(['id', 'date'])[group_metrics].sum().reset_index()

    #df = add_metrics_for_trend_analyzer(dataset=df, metrics_to_send=metrics_to_send)

    links = df.id.unique()
    
    printt("Before pivot:")
    print(f"{df}\n\n")

    pivot = df.fillna(0).pivot_table(index='date', columns='id', values=metric_names, aggfunc=np.mean)
    
    sleep(2)
    printt("After pivot:")
    print(f"{pivot}\n\n")
    
    pivot = pivot.swaplevel(axis=1)

    sleep(2)
    printt("After swaplevel:")
    print(pivot)

    final_result = {}
    for link_id in links:
        result = {}
        item = pivot[link_id]
        for col in metric_names:
            result[col] = [{'date': idx, 'value': item[col][idx]} for idx in item.index]
        final_result[link_id] = result

    return final_result
# COMMAND ----------
metrics_to_send = [
    {'name': 'metric1'},
    {'name': 'metric2'}
]

data = {
    'id': ['id1', 'id1', 'id1', 'id2', 'id2', 'id2'],
    'date': ['2021-01-01', '2021-01-02', '2021-01-03']*2,
    'metric1': [10, 20, 30, 40, 50, 60],
    'metric2': [20, 40, 60, 80, 100, 120]
}

df = pd.DataFrame(data)
# COMMAND ----------
create_daily_json_for_trend_analyzer(df, metrics_to_send)
# COMMAND ----------
printt(presentation["WHERE"])
sleep(5)
show_image(presentation["where_gif"])
# COMMAND ----------
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 17, 35, 12]
})

# COMMAND ----------
df['adult'] = np.where(df['age'] >= 18)
df

# COMMAND ----------
df['adult'] = np.where(df['age'] >= 18, 1, 0)
df
# COMMAND ----------
df['age_group'] = np.where(df['age'] >= 18, 'adult', 'minor')
df
# COMMAND ----------
printt(presentation["MUTABLE_DEFAULTS"])


# COMMAND ----------
def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart

user1_cart = add_to_cart("Apple")
print("User 1 Cart:", user1_cart)  

# COMMAND ----------
user2_cart = add_to_cart("Cookies")
print("User 2 Cart:", user2_cart) 
# COMMAND ----------
def add_to_cart(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
# COMMAND ----------
