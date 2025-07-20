# Getting Started

This page will help you get HomeBikeManager up and running in minutes.

## Requirements
- Python 3.8+
- Git
- (Optional) Docker

## Setup Steps

1. **Clone the repository**
   ```sh
   git clone https://github.com/dannycab/HomeBikeManager.git
   cd HomeBikeManager
   ```
2. **Create a virtual environment**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the app**
   ```sh
   python app.py
   ```

## Using Docker (Optional)

1. **Build and run the Docker image**
   ```sh
   docker build -t homebikemanager .
   docker run -p 5000:5000 homebikemanager
   ```

---

For more advanced setup, see the [full documentation](https://dannycab.github.io/HomeBikeManager/).
