FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -U "nextcord[voice]" "requests"

COPY . .

CMD [ "python", "./main.py" ]
