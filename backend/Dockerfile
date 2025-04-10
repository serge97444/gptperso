FROM python:3.11
WORKDIR /app
ENV MODULE_NAME=app
ADD requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 80
CMD ["gunicorn" , "app:app" , "--host", "0.0.0.0","--port","80"]