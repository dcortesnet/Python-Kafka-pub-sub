from fastapi import FastAPI, Request, HTTPException
import json
from datetime import datetime
import uuid

app = FastAPI()

@app.post("/messages")
async def publish_message(request: Request):
    try:
        body = (await request.body()).decode('utf-8')
        data = json.loads(body)
        message = {
            "id": uuid.uuid4(),
            "message": data['message'],
            "date": datetime.now()
        }        
        
        print(f"Publishing an Event using Kafka to: {data['message']}");
        return { "detail": "Publishing an Event using Kafka successful" }
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid request body")
    except:
        raise HTTPException(status_code=500, detail="Internal Server error")
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)