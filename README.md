# Python 3.5+ Apache Kafka Pub/Sub ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Basic flow of event publish and subscribe model
using Apache Kafka
The project consists of 2 services, one for publications and the other for consumers.

# Endpoints

| Service | Method | Endpoint | body | Description
|:--------|:--------|:--------|:--------| :--------|
|`Service pub` | POST |http://localhost:8000/messages | {message: "Hello world"} | Create new resource
|`Service sub` | GET | http://localhost:8001/messages |  | Get all resources

## Team

Developed by Diego Cortés

* dcortes.net@gmail.com
