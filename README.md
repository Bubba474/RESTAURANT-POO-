# 🍽️ Restaurant Management System  

A Python project applying Object-Oriented Programming (OOP) to manage restaurants.  
Features include restaurant registration, listing, review management (1–5 scale with average calculation), and status control (active/inactive).  

---

## ✨ Features  
- Register restaurants with name and category.  
- List restaurants in a formatted table showing:  
  - Name  
  - Category  
  - Average rating  
  - Status (active/inactive)  
- Manage customer reviews (1–5) with automatic average calculation.  
- Toggle restaurant status between active and inactive.  

---

## 🔧 Object-Oriented Structure  
- **`Restaurant` Class** – Handles restaurant data, status, and reviews.  
- **`Review` Class** – Represents a customer review (reviewer and rating).  

---

## 📚 Example Usage  

```python
from avaliacao import Avaliacao
from restaurante import Restaurante

# Creating restaurants
restaurant1 = Restaurante("Sabor Mineiro", "Brazilian")
restaurant2 = Restaurante("Sushi House", "Japanese")

# Activating a restaurant
restaurant1.alternar_estado()

# Adding reviews
restaurant1.receber_avaliacao("Ana", 5)
restaurant1.receber_avaliacao("Carlos", 4)

# Listing all restaurants
Restaurante.listar_restaurantes()
