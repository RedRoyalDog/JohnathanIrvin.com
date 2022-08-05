FROM python:3.10.5 as base
WORKDIR /app
COPY website/ requirements.txt ./website/
RUN pip install -r website/requirements.txt
ENV FLASK_ENV=development
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "website:app"]
