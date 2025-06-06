# Setup project "LOAN AMOUNT PREDICTION"

## Virtual environment :
Linux :
* `python3 -m venv .venv`

MacOS-Windows
* `python -m venv .venv`

## Activate Virtual environment :
Windows : 
* `.venv\Scripts\activate`
  
macOS/Linux : 
* `source .venv/bin/activate`

## Dependencies :

* Make sure you're in the project directory
* Install dependencies : `pip install -r requirements.txt`
* Alternatively, you can install the libraries yourself by reading requierements.txt file

## Start streamlit (front)
`streamlit run app.py`


## Start fastAPI (back)
`uvicorn api:app --host 127.0.0.1 --port 9500 --reload`

[Documentation de l'api](http://127.0.0.1:9500/docs)

## Generate and Train a model from csv
 `python3 train_model_exemple.py`

## Execute test
`pytest api_test.py`