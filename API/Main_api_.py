import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI , File ,UploadFile
from app.main import run_system
app = FastAPI()
@app.get('/')
def home():
    return{'message' : 'API is working boss!!'}

#route1
@app.get('/analyze')
def analyze(file_path : str) :
    result , rec = run_system(file_path)
    return {'INSIGHTS': result,
            "RECOMMENDATION" : rec}
#route2 
@app.post('/analyze-file' )
def analyze_file(file : UploadFile= File(...)) :
    if not file.filename.endswith('.csv') :
        return {'error' : ' not CSV file'}
    file_path = f'temp_{file.filename}'
    try : 
     with open(file_path , 'wb') as f :
        f.write(file.file.read())
    
     result , rec = run_system(file_path)
    finally :
       if  os.path.exists(file_path) :
        os.remove(file_path)
    try :
       result , rec = run_system(file_path)
    except Exception as e :
     os.remove(file_path)
     return{'error': str(e)}
    os.remove(file_path)
    return { 'INSIGHTS': result,
            "RECOMMENDATION" : rec
    }