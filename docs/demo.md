# Demo Conversation

Below is a sample conversation with the Clothing Store AI Agent.

---

```text
🛍️  Clothing AI Agent
Type 'exit' or 'quit' to leave.

You: Hi
Agent: Hello! How can I assist you today?

You: Show me red dresses under 1500 INR in size M
Agent: Here are some red dresses under 1500 INR in size M:

1. Red Summer Dress (PROD001) - 1299 INR
   Lightweight cotton dress perfect for summer outings.

Would you like to see more details or add one to your cart?

You: Add PROD001 to my cart
Agent: Added Red Summer Dress (PROD001) to your cart. Would you like to continue shopping or view your cart?

You: Show my cart
Agent: Here's your cart:

1. Red Summer Dress (PROD001)
   - Size: M
   - Color: red
   - Quantity: 1
   - Price: 1299 INR

Total: 1299 INR

You: Recommend something to go with it
Agent: Based on your red dress, here are some suggestions:

1. Black Pumps (PROD015) - 1899 INR
2. Silver Statement Earrings (PROD019) - 499 INR

Would you like to add any of these to your cart?

You: I'm 5'10", 75kg, broad shoulders. What size shirt should I buy?
Agent: Based on height 5'10", weight 75kg, and a broad build, we recommend size L for shirt.

You: Plan a wedding guest outfit under 5000 INR
Agent: Here's a wedding guest outfit under 5000 INR:

1. Green Embroidered Kurta (PROD007) - 2199 INR
2. Beige Chinos (PROD018) - 1399 INR
3. Black Pumps (PROD015) - 1899 INR
4. Silver Statement Earrings (PROD019) - 499 INR

Total: 4996 INR

You: Checkout, I'm Aarav Sharma in Mumbai
Agent: Thank you, Aarav Sharma! Your order has been placed.

Order Summary:
- Order ID: A1B2C3D4
- Items: Red Summer Dress (PROD001)
- Total: 1299 INR
- Status: confirmed

You: exit
Agent: Goodbye!
```

---

## Notes

- The agent remembers context like budget and cart contents across turns.
- Off-topic questions are politely redirected.
- Every tool result is validated through Pydantic models.
