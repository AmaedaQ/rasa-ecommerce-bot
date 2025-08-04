
# Rasa E-commerce Assistant

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Rasa 3.x](https://img.shields.io/badge/Rasa-3.x-green.svg)](https://rasa.com/docs/)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://reactjs.org/)

## Overview

An AI-powered chatbot for e-commerce platforms built using the Rasa framework. Handles customer queries related to order tracking, product information, and general support through natural language conversations.

## Features

- Order tracking with ID validation
- Product search and inventory checking
- Return and refund policy assistance
- Payment and shipping information
- Context-aware and intent-based conversation flows

## Tech Stack

- **AI/NLP**: Rasa Open Source 3.x, spaCy
- **Frontend**: React.js (18+)
- **Backend**: Node.js + Express
- **Language**: Python 3.8+

## Setup Instructions

```bash
# Clone the repository
git clone <repo-url>
cd rasa-ecommerce-assistant

# Python environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install Python dependencies
pip install -r requirements.txt

# Install frontend dependencies
cd src
npm install
cd ..

# Train and run the assistant
rasa train
rasa run --enable-api --port 5005 &
rasa run actions --port 5055 &
cd src
npm start
````

## Supported Intents

* `track_order`: Track orders by order ID
* `return_policy`: Provide return/refund details
* `product_search`: Discover available products
* `shipping_info`: Offer shipping and delivery details
* `payment_methods`: List accepted payment options

## Entity Recognition

* Order IDs
* Product names
* Shipping types
* Payment methods

## Project Structure

```
rasa-ecommerce-assistant/
├── actions/            # Custom action code
├── data/               # NLU training data, stories, and rules
├── models/             # Trained Rasa models
├── src/                # React frontend
├── config.yml          # Rasa pipeline and policies
├── domain.yml          # Intents, entities, slots, responses
├── endpoints.yml       # Action server and tracker store config
└── requirements.txt    # Python dependencies
```

## Performance Metrics

* Response latency: < 200ms
* Intent classification accuracy: 95%+
* Handles up to 50 concurrent users (test environment)

## License

This project is licensed under the MIT License.


