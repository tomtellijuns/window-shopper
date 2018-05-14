FROM python:2

WORKDIR /usr/src/app

# Download dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Launch
COPY . .
CMD [ "python", "./persist.py" ]
