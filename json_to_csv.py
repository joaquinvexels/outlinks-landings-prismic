# Import JSON Prismic file and convert to CSV for Screaming Frog

## Import libraries
import json
import csv
import os

# Get list of JSON files
json_files = [f for f in os.listdir('./JSON') if f.endswith('.json')]

for json_file in json_files:
    # Open JSON file
    with open('./JSON/' + json_file) as json_data:
        # Load JSON data
        data = json.load(json_data)
        with open('data.csv', 'a') as csv_file:
            if 'uid' in data and 'lang' in data:
                # Create CSV file
                writer = csv.writer(csv_file)
                url = ''
                if data['lang'] == 'es-es':
                    url = "https://es.vexels.com/" + data['uid'] + "/"
                elif data['lang'] == 'en-us':    
                    url = "https://www.vexels.com/" + data['uid'] + "/"
                elif data['lang'] == 'pt-br':    
                    url = "https://br.vexels.com/" + data['uid'] + "/"
                elif data['lang'] == 'de-de':
                    url = "https://de.vexels.com/" + data['uid'] + "/"
                
                writer.writerow([url])