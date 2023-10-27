from datetime import datetime
import re
from math import ceil
from app.models import Receipt


def calculate_points(receipt: Receipt):
    points = 0

    # Rule: One point for every alphanumeric character in the retailer name
    retailer_name = receipt.retailer
    points += sum(c.isalnum() for c in retailer_name)

    # Rule: 50 points if the total is a round dollar amount with no cents
    total = float(receipt.total)
    if total.is_integer():
        points += 50

    # Rule: 25 points if the total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # Rule: 5 points for every two items on the receipt
    num_items = len(receipt.items)
    points += (num_items // 2) * 5

    # Rule: If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer.
    for item in receipt.items:
        description_length = len(item.shortDescription.strip())
        if description_length % 3 == 0:
            item_points = ceil(float(item.price) * 0.2)
            points += item_points

    # Rule: 6 points if the day in the purchase date is odd
    purchase_date = datetime.strptime(receipt.purchaseDate, '%Y-%m-%d').day
    if purchase_date % 2 == 1:
        points += 6

    # Rule: 10 points if the time of purchase is after 2:00pm and before 4:00pm
    purchase_time = datetime.strptime(receipt.purchaseTime, '%H:%M').time()
    after_2_pm = purchase_time >= datetime.strptime('14:00', '%H:%M').time()
    before_4_pm = purchase_time <= datetime.strptime('15:59', '%H:%M').time()
    if after_2_pm and before_4_pm:
        points += 10

    return points