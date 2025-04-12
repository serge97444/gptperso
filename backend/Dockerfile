FROM python:3.11
WORKDIR /app
ENV MODULE_NAME=app
ADD requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY src .
EXPOSE 8080
CMD ["uvicorn" , "app:app" , "--host", "0.0.0.0","--port","8080"]