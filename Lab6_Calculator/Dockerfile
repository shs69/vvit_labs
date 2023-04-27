FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /calc
ADD . /calc
RUN python -m pip install --upgrade pip && pip install -r req.txt
RUN python calc/calculator.py