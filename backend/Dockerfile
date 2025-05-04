FROM python:3.11
# WORKDIR /user/llms
# COPY ../../llms .
WORKDIR /user/mygpt/backend
ENV MODULE_NAME=backend
ADD requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY src .
COPY app.py .
EXPOSE 8080


CMD ["uvicorn" , "app:app" , "--host", "0.0.0.0","--port","8080","--reload"]