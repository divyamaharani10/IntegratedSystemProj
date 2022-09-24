FROM python:3.9.1
WORKDIR /divyamaharani/Documents/GitHub/IntegratedSystemProj
ADD . /divyamaharani/Documents/GitHub/IntegratedSystemProj
CMD ["python", "test.py"]
