from typing import Union
from app.calculate_points import calculate_points
from app.models import Receipt

from fastapi import FastAPI

import uuid
import hashlib


app = FastAPI()

receipts = {}  # To hold Receipt data. Key: receipt_id, Value: Receipt object


@app.get("/")
def read_root():
    return {"message": "This is the receipt proessor application. You can try out the API at localhost:8000/docs."}


@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    # Hash the receipt content
    receipt_hash = hashlib.md5(str(receipt).encode()).hexdigest()
    if receipt_hash not in receipts:
        receipts[receipt_hash] = receipt  # Store the receipt if it's new
    return {"id": receipt_hash}


@app.get("/receipts/{id}/points")
def get_points(id: str):
    if id not in receipts:
        return {"error": "No receipt found for that id"}, 404
    receipt = receipts[id]
    points = calculate_points(receipt)
    return {"points": points}
