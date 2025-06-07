# Description
The aim of this project is to use a trained model to predict the amount of a loan based on parameters supplied by the user.

## Virtual environment

Linux :
```bash
python3 -m venv .venv
```

MacOS-Windows
```bash
python -m venv .venv
```

## Activate Virtual environment :
Windows : 
```bash
.venv\Scripts\activate
```

macOS/Linux : 
```bash
source .venv/bin/activate
```

## Dependencies :

* Make sure you're in the project directory
* Install dependencies : `pip install -r requirements.txt`
* Alternatively, you can install the libraries yourself by reading requierements.txt file

### Structure : 
```
.
├── api.py
├── api_test.py
├── app.py
├── data.csv
├── logs.txt
├── model.pkl
├── notebook.ipynb
├── preprocessor.pkl
├── README.md
├── requirements.txt
└── train_model_exemple.py
```

## Start streamlit (front)
```batch 
streamlit run app.py
```

## Start fastAPI (back)
```batch 
uvicorn api:app --host 127.0.0.1 --port 9500 --reload
```

[Documentation de l'api](http://127.0.0.1:9500/docs)

## Generate and Train a model from csv
```batch 
python3 train_model_exemple.py
```

## Execute test
```batch 
pytest api_test.py
```

## Run project with docker
```batch
docker compose up --build
```