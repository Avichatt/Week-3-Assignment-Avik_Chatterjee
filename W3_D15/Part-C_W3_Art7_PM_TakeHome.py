"""
Part C — Interview Ready (20%)

Q1 — What update anomalies arise in a denormalised database? Give a concrete e-commerce example.
Q2 (Design) — Design a schema that: (a) maintains current product price, (b) records price history with timestamps, (c) is in 3NF.
Q3 — Given ACID violation scenario: 'Two users simultaneously try to book the last hotel room.' 
Which ACID property is at risk and how does the database prevent double-booking?
"""

def answer_part_c():
    print("=== PART C: Interview Ready ===")
    
    print("\nQ1: Update Anomalies in Denormalized Databases")
    print("Update anomalies occur when data is redundant, and updating one piece of data requires multiple updates "
          "across many rows. If one row is missed, the database becomes inconsistent.")
    print("Example: An 'Orders' table that includes 'CustomerAddress'. If a customer moves, the system must update "
          "every single historical order row for that customer. If some rows are missed, the customer has different "
          "addresses for the same UserID in the system.")

    print("\nQ2: Design for Product Price and History (3NF)")
    print("To maintain the current price and history while keeping it in 3NF, we use two tables:")
    print("1. PRODUCTS (ProductID, Name, Description, CurrentPrice, LastUpdated)")
    print("   - Stores the 'current' state for fast lookup.")
    print("2. PRICE_HISTORY (HistoryID, ProductID, OldPrice, EffectiveDate)")
    print("   - Stores every price change. ProductID is a Foreign Key to Products.")
    print("Normalization check: Every non-key attribute depends only on the primary key. "
          "Splitting history from active status prevents the 'Repeating Groups' anomaly.")

    print("\nQ3: ACID Violation (Double-Booking)")
    print("The property at risk is **ISOLATION**.")
    print("Without isolation, two transactions might read the status 'Available' simultaneously and both "
          "proceed to 'Booked', even if only one room exists (a 'Lost Update' or 'Race Condition').")
    print("Prevention:")
    print("Modern databases prevent this using 'Concurrency Control' mechanisms, specifically 'Locking' "
          "or 'Optimistic Concurrency Control'.")
    print("1. Pessimistic Locking: Transaction A locks the row until it's done. Transaction B must wait.")
    print("2. Transaction Levels: Setting isolation levels to 'Serializable' ensures transactions produce "
          "the same result as if they were executed one after another.")

if __name__ == "__main__":
    answer_part_c()
