from typing import Union
from app.calculate_points import calculate_points
from app.models import Receipt

from fastapi import FastAPI

import uuid

app = FastAPI()

receipts = {}  # To hold Receipt data. Key: receipt_id, Value: Receipt object


@app.get("/")
def read_root():
    return {"message": "This is the receipt proessor application. You can try out the API at localhost:8000/docs."}


@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    receipt_id = str(uuid.uuid4())  # Generate unique id for receipt
    receipts[receipt_id] = receipt  # Store receipt
    return {"id": receipt_id}


@app.get("/receipts/{id}/points")
def get_points(id: str):
    if id not in receipts:
        return {"error": "No receipt found for that id"}, 404
    receipt = receipts[id]
    points = calculate_points(receipt)
    return {"points": points}
