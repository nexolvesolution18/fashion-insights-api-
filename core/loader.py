import csv
def load_csv(file_path) :
    responses = []
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file) 
        for row in reader :
            response = {'style' : row.get('style'),
                        'size' : row.get('size'),
                        'shoe_size' : row.get('shoe_size')}
            responses.append(response)
    return responses