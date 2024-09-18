from datetime import datetime

class BookDeliveryService:
    def __init__(self):
        self.orders = {}
        self.customers = {
            '1': {'name': 'Alice', 'address': '123 Wonderland'},
            '2': {'name': 'Bob', 'address': '456 Nowhere'}
        }

    def create_order(self, customer_id, book_ids):
        """Create new order."""
        order_id = len(self.orders) + 1
        self.orders[order_id] = {
            'customer_id': customer_id,
            'book_ids': book_ids,
            'date': datetime.now().isoformat()
        }
        return order_id

    def get_order(self, order_id):
        """Get order for ID."""
        return self.orders.get(order_id, "Order not found")

    def get_customer(self, customer_id):
        """Get information about client."""
        return self.customers.get(customer_id, "Customer not found")

if __name__ == "__main__":
    service = BookDeliveryService()

    order_id = service.create_order('1', ['book1', 'book2'])
    print(f"Order created with ID: {order_id}")

    order = service.get_order(order_id)
    print(f"Order details: {order}")

    customer = service.get_customer('1')
    print(f"Client details: {customer}")
