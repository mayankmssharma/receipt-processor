FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# Run tests
RUN pytest /code/app/test_calculate_points.py

# Run the application 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]