import json
import boto3
import os
import uuid 

def lambda_handler(event, context):
    # Initialize the Lex runtime client
    lex_client = boto3.client('lexv2-runtime')
    # Extract the user's message from the event
    responseMsg = lex_client.recognize_text(
        botId="WEUXLJFSDJ",
        botAliasId="TSTALIASID",
        localeId='en_US',  
        sessionId = "test_session",
        text=event["messages"][0]['unstructured']['text']
        )
    print(responseMsg)
        
    
    message = ""
    for mess in responseMsg['messages']:
        message += mess['content']
        message += "\n"

    return {
        'statusCode': 200,
        'messages': [{'type': 'unstructured', 'unstructured': {'text': message }}]
    }
    
    
