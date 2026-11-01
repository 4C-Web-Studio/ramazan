FROM python:3.12-slim
WORKDIR /checks
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY module.py test_module.py ./
CMD ["python", "-m", "pytest", "test_module.py", "-v"]
