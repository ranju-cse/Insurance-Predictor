#use python:3.11-slim
FROM python:3.11-slim
#set working directory
WORKDIR /app

#Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy rest of application code
COPY . .

#Expose the appplication port
EXPOSE 8000

#command to start FastAPI application
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
