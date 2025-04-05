import json
import requests  # External dependency, needs to be listed in requirements.txt

def lambda_handler(event, context):
    try:
        # Example API request
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        data = response.json()
        
        # Log or process the API data
        print(data)
        
        return {
            'statusCode': 200,
            'body': json.dumps('Data fetched successfully')
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to fetch data')
        }
