# 1. Use Python base image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy everything
COPY . .

# 4. Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. Expose port
EXPOSE 8000

# 6. Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
