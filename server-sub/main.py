from fastapi import FastAPI, HTTPException
import uvicorn
from kafka import KafkaConsumer
import json
import threading

app = FastAPI()
name_topic = "message_topic"

messages_storage = []

def kafka_consumer_thread():
    consumer = KafkaConsumer(
        name_topic,
        group_id='my-group', # Grupo de consumidores
        bootstrap_servers="localhost:9092",
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        json_message = message.value       
        print("Received JSON message:", json_message)
        messages_storage.append(json_message)

kafka_thread = threading.Thread(target=kafka_consumer_thread)
kafka_thread.daemon = True
kafka_thread.start()

@app.get("/messages")
def messages():
    try:
        return { "messages": messages_storage }    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server error")
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)