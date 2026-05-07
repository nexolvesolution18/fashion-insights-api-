import sys

import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.recommender import generate_recommendation
from core.analyzer import analyze_data
from core.loader import load_csv
import json

def run_system(file_path) :
 responses = load_csv(file_path)
 result =  analyze_data(responses)
 if not responses :
        print('no data found ')
        exit()
 rec = generate_recommendation(result)
 return result,rec
 

def save_output(result , rec ) :
 with open("output.json", "w") as f:
    json.dump({
        "insights": result,
        "recommendation": rec
    } ,f, indent=4)

if __name__ == '__main__' :
  if len(sys.argv) < 2 :
        print('usage : python app/main.py')
        exit()
  file_path = sys.argv[1] 
  output_file = None
  if len(sys.argv) > 2 :
        output_file = sys.argv[2]
  try :
   result , rec = run_system(file_path)
  except Exception as e :
     print('error :', e)
     exit()
  print('\n --- INSIGHTS--- ')
  print(f'TOP STYLE : {result['top style']}')
  print(f'TOP SIZE : {result['top size']}')
  print(f'TOP SHOE SIZE : {result['top shoe size']}')
  save_output(result,rec)
  print('\n ---RECOMMENDATION---')
  print(rec)
 