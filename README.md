
# Rasa E-Commerce Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Rasa](https://img.shields.io/badge/Rasa-3.x-5A17EE?logo=rasa)](https://rasa.com/docs/)
[![React](https://img.shields.io/badge/React-18+-61DAFB?logo=react&logoColor=white)](https://react.dev/)

AI-driven conversational assistant for e-commerce workflows.  
Built on **Rasa 3.x** for intent classification and dialogue management, with a **React** frontend and **Node.js** middleware.

---

## Core Capabilities

- Order tracking via validated IDs  
- Product and inventory lookup  
- Return / refund flow automation  
- Payment and shipping inquiries  
- Context-aware multi-turn conversations  

---

## Tech Stack

| Layer | Technologies |
|-------|---------------|
| NLP / AI | Rasa Open Source 3.x, spaCy |
| Frontend | React 18+ |
| Backend | Node.js, Express |
| Language | Python 3.8+ |

---

## Quick Start

```bash
git clone <repo-url>
cd rasa-ecommerce-assistant

# Python environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup
cd src && npm install && cd ..

# Train and launch
rasa train
rasa run --enable-api --port 5005 &
rasa run actions --port 5055 &
cd src && npm start
````

---

## Intents & Entities

**Intents:**
`track_order`, `return_policy`, `product_search`, `shipping_info`, `payment_methods`

**Entities:**
`order_id`, `product_name`, `shipping_type`, `payment_method`

---

## Directory Layout

```
rasa-ecommerce-assistant/
├── actions/          # Custom Python actions
├── data/             # NLU data, stories, rules
├── models/           # Trained Rasa models
├── src/              # React client
├── config.yml        # Rasa pipeline & policies
├── domain.yml        # Intents, entities, slots, responses
├── endpoints.yml     # Action server configuration
└── requirements.txt  # Python dependencies
```

---

## Benchmarks

* Response latency < 200 ms
* Intent accuracy ≥ 95%
* ~50 concurrent sessions (test environment)

---

## License

MIT © Contributors

