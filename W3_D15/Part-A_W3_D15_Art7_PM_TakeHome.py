"""
Part A — IIT-GN Assignment Template (40%)

1. Design ER diagram for an online food delivery app with 5+ entities. Include cardinality for all relationships.
2. Normalise a provided flat table (OrderFacts.csv on LMS) to 3NF. Show each step.
3. Write relational algebra expressions for 5 queries on your schema.
4. Map 3 Pandas operations (merge, groupby+agg, filter) to their relational algebra equivalents.
"""

    

# PART A: IIT‑GN Assignment

## 1. ER Diagram Design (Online Food Delivery) with 5+ Entities

**Entities and Cardinalities:**
- **USERS (UserID, Name, Email, Phone)**  
  Relationship: Places (1 to M) ORDERS  

- **RESTAURANTS (RestID, Name, Address, Rating)**  
  Relationship: Receives (1 to M) ORDERS  

- **ORDERS (OrderID, UserID, RestID, RiderID, TotalPrice, Status, CreatedAt)**  
  Relationship: Contains (1 to M) ORDER_ITEMS  

- **ORDER_ITEMS (ItemID, OrderID, DishName, Quantity, UnitPrice)**  
  Relationship: Belongs To (M to 1) ORDERS  

- **DELIVERY_RIDERS (RiderID, Name, Phone, VehicleReq)**  
  Relationship: Delivers (1 to M) ORDERS  

---

## 2. Normalisation to 3NF (Assuming theoretical `OrderFacts` table)

**Step 0 (Un-normalized Flat Table):**  
```
OrderFacts(OrderID, OrderDate, UserID, UserName, UserAddress, RestID, RestName, RestAddress, 
           ItemID, ItemName, ItemQty, ItemPrice)
```

**Step 1 (1NF - Remove repeating groups):**  
- Separate multi-valued items into distinct rows per item.  
- `(OrderID, ItemID)` becomes the composite primary key.

**Step 2 (2NF - Remove partial dependencies):**  
- Items shouldn't depend purely on part of the primary key.  
- Separate order-level and item-level data:  
  - Orders(OrderID, OrderDate, UserID, UserName, UserAddress, RestID, RestName, RestAddress)  
  - OrderItems(OrderID, ItemID, ItemName, ItemQty, ItemPrice)

**Step 3 (3NF - Remove transitive dependencies):**  
- Non-key attributes cannot depend on other non-key attributes.  
- Final tables:  
  - Users(UserID, UserName, UserAddress)  
  - Restaurants(RestID, RestName, RestAddress)  
  - Orders(OrderID, OrderDate, UserID, RestID)  
  - Items(ItemID, ItemName, ItemPrice)  
  - OrderItems(OrderID, ItemID, ItemQty)  

*Note:* ItemPrice moved to `Items` if price is standard, or kept in `OrderItems` if historical purchase price is needed.

---

## 3. Relational Algebra Expressions for 5 Queries

- **Q1. Find all users named 'Alice':**  
  \(\sigma_{Name='Alice'}(USERS)\)

- **Q2. Get names of all Restaurants:**  
  \(\pi_{Name}(RESTAURANTS)\)

- **Q3. Find all OrderIDs placed by UserID = 101:**  
  \(\pi_{OrderID}(\sigma_{UserID=101}(ORDERS))\)

- **Q4. Get Names of users who ordered from Restaurant 'Spice Grill':**  
  \(\pi_{USERS.Name}(USERS \bowtie (\sigma_{Name='Spice Grill'}(RESTAURANTS) \bowtie ORDERS))\)

- **Q5. Find items ordered in OrderID = 500:**  
  \(\pi_{DishName, Quantity}(\sigma_{OrderID=500}(ORDER_ITEMS))\)

---

## 4. Pandas to Relational Algebra Mappings

- **Filter:**  
  `df[df['age'] > 20]` → \(\sigma_{age>20}(R)\)

- **Select columns:**  
  `df[['id', 'name']]` → \(\pi_{id, name}(R)\)

- **Merge:**  
  `pd.merge(df1, df2, on='id')` → Natural Join \((R \bowtie S)\) or Theta Join \((R \bowtie_{R.id=S.id} S)\)

---

