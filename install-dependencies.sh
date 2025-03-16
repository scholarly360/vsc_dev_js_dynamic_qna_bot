sudo apt-get update && sudo apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && sudo rm -rf /var/lib/apt/lists/*
python -m pip install --no-cache-dir Flask python-dotenv
