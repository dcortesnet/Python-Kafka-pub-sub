from fastapi import FastAPI, Request, HTTPException
import json
import uvicorn
from datetime import datetime
import uuid
from kafka import KafkaProducer

app = FastAPI()
name_topic = "message_topic"
kafka_producer = KafkaProducer(bootstrap_servers="localhost:9092")

@app.post("/messages")
async def messages(request: Request):
    try:
        body = (await request.body()).decode('utf-8')
        data = json.loads(body)
        
        if "message" not in data:
            raise HTTPException(status_code=400, detail="The message property is required")
        
        message = {
            "id": str(uuid.uuid4()),
            "message": data['message'],
            "date": str(datetime.now())
        }
        kafka_producer.send(name_topic, value=json.dumps(message).encode('utf-8'))
        print(f"Publishing an Event using Kafka to: {data['message']}");
        return { "detail": "Publishing an Event using Kafka successful" }
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid request body")
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server error")
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)