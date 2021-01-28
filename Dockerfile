FROM python:3.8
RUN mkdir /code

RUN apt-get update && apt-get install -y --no-install-recommends \
		uuid-dev \
	    postgresql postgresql-contrib \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /code
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt


#COPY . .
