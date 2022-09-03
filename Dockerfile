FROM python:3.11.0rc1-slim-bullseye
LABEL maintainer="prakash"
COPY . /
WORKDIR /src
ENV FLASK_APP=app.py
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]