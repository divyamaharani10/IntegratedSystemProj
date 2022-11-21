FROM python:3.9.1
WORKDIR /divyamaharani/Documents/GitHub/IntegratedSystemProj
COPY requirements.txt /divyamaharani/Documents/GitHub/IntegratedSystemProj/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /divyamaharani/Documents/GitHub/IntegratedSystemProj
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
