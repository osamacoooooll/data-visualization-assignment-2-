FROM python:3.9-slim
WORKDIR /app
COPY sender.py .
COPY ip_addresses.csv .
RUN pip install requests
CMD ["python", "sender.py"]
