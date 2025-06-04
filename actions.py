import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionFetchProducts(Action):
    def name(self):
        return "action_fetch_products"

    def run(self, dispatcher, tracker, domain):
        query = tracker.latest_message.get("text")  # Capture user query

        # Call backend API to get products
        response = requests.post("http://localhost:5000/api/products", json={"query": query})

        if response.status_code == 200:
            data = response.json()

            if "products" in data and data["products"]:
                product_messages = []

                for product in data["products"]:
                    product_messages.append(
                        f"- **[{product['name']}]({product['visitUrl']})**\n"
                        f"  🔹 *Category:* {product['category']}\n"
                        f"  💰 *Price:* ${product['price']}\n"
                        f"  ⭐ *Rating:* {product['rating']}/5\n"
                    )

                dispatcher.utter_message("Here are some products that match your search:\n\n" + "\n".join(product_messages))
                dispatcher.utter_message("Would you like to filter by price, brand, or something else? Let me know!")
            else:
                dispatcher.utter_message("I couldn't find matching products. Maybe try refining your search?")
        else:
            dispatcher.utter_message("There was an issue fetching product details. Please try again later.")

        return []