FROM blazemeter/selenium-framework

WORKDIR /code
COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . /code

CMD ["tests/test_purchase_tickets.py"]