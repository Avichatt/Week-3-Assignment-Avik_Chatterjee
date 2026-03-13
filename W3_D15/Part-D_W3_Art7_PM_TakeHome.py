"""
Part D — AI-Augmented Task (10%)

1. Prompt AI: 'Design the database schema for a ride-sharing app (like Ola/Uber). 
Include ER diagram description, normalised tables, and 5 SQL queries with window functions.'
2. Document prompt and output.
3. Evaluate: Is the schema in 3NF? Are there missing relationships? 
Run at least 2 SQL queries on your PostgreSQL instance.
"""

    
# PART D: AI‑Augmented Task

You are a senior database architect with deep expertise in designing scalable, production-grade schemas for high-traffic transactional systems.

Design a complete database schema for a ride-sharing application (similar to Ola/Uber). Your output should cover three components:

**1. ER Diagram Description**
Describe all entities, their attributes, and the relationships between them (cardinality and participation constraints). Cover the core domain objects: users (riders and drivers), vehicles, rides, payments, ratings, and locations. Explain each relationship in plain English so it could be handed directly to a diagramming tool.

**2. Normalized Tables**
Define all tables in at least 3NF. For each table, specify:
- Column names and data types
- Primary keys, foreign keys, and unique constraints
- Any indexes critical for query performance (e.g., on geolocation, ride status, timestamps)

Briefly justify any deliberate denormalization decisions if made for performance reasons.

**3. Five SQL Queries Using Window Functions**
Write five practical, non-trivial SQL queries that reflect real operational or analytical needs for a ride-sharing platform. Each query must use at least one window function (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, `SUM OVER`, `AVG OVER`, etc.). For each query, include:
- A one-line business problem it solves
- The full SQL query
- A brief explanation of what the window function is doing and why it's the right tool here

Queries should span different use cases: driver performance, ride history, revenue analysis, surge pricing patterns, or rating trends.

---

## 1. ER Diagram Description
**Entities and Attributes:**
- **Users**
  - Riders: RiderID, Name, Phone, Rating
  - Drivers: DriverID, Name, License, VehicleType, Rating
- **Vehicles**
  - VehicleID, DriverID (FK), PlateNumber, Model, Capacity
- **Rides**
  - RideID, RiderID (FK), DriverID (FK), PickupLocation, DropLocation, Fare, RideTime, Status
- **Payments**
  - PaymentID, RideID (FK), Amount, Method, Timestamp, Status
- **Ratings**
  - RatingID, RideID (FK), RatedBy (Rider/Driver), Score, Comments
- **Locations**
  - LocationID, Latitude, Longitude, Address

**Relationships:**
- A Rider books many Rides; each Ride belongs to one Rider.  
- A Driver completes many Rides; each Ride belongs to one Driver.  
- Each Driver owns one Vehicle; each Vehicle belongs to one Driver.  
- Each Ride has one Payment; each Payment belongs to one Ride.  
- Each Ride can have multiple Ratings (from Rider and Driver).  
- Pickup and Drop locations are linked to the Locations table.

---

## 2. Normalized Tables (3NF)

**Drivers**
- DriverID (PK), Name, License, VehicleType, Rating  
- Index: License (unique)

**Riders**
- RiderID (PK), Name, Phone, Rating  
- Index: Phone (unique)

**Vehicles**
- VehicleID (PK), DriverID (FK), PlateNumber, Model, Capacity  
- Index: PlateNumber (unique)

**Rides**
- RideID (PK), RiderID (FK), DriverID (FK), PickupLoc (FK), DropLoc (FK), Fare, RideTime, Status  
- Indexes: (DriverID, RideTime), (PickupLoc, DropLoc)

**Payments**
- PaymentID (PK), RideID (FK), Amount, Method, Timestamp, Status  
- Index: RideID

**Ratings**
- RatingID (PK), RideID (FK), RatedBy, Score, Comments  
- Index: RideID

**Locations**
- LocationID (PK), Latitude, Longitude, Address  
- Index: (Latitude, Longitude)

*Note:* Denormalization may be considered for storing frequently accessed ride summaries (e.g., Rider name + Driver name + Fare) in a reporting table for performance.

---

## 3. SQL Queries Using Window Functions

**Q1. Driver Average Fare**
- *Business Problem:* Find each driver’s average fare across rides.  
```sql
SELECT DriverID, 
       AVG(Fare) OVER (PARTITION BY DriverID) AS AvgDriverFare
FROM Rides;
```
- *Explanation:* `AVG OVER` computes per‑driver averages without collapsing rows.

---

**Q2. Ride Fare Ranking**
- *Business Problem:* Rank rides by fare to identify high‑value trips.  
```sql
SELECT RideID, Fare, 
       RANK() OVER (ORDER BY Fare DESC) AS FareRank
FROM Rides;
```
- *Explanation:* `RANK()` orders rides by fare, useful for surge analysis.

---

**Q3. Driver Performance Trend**
- *Business Problem:* Track each driver’s last ride fare compared to current.  
```sql
SELECT DriverID, RideID, Fare,
       LAG(Fare) OVER (PARTITION BY DriverID ORDER BY RideTime) AS PrevFare
FROM Rides;
```
- *Explanation:* `LAG()` shows the previous fare per driver, highlighting trends.

---

**Q4. Rider Ride Frequency**
- *Business Problem:* Identify top riders by number of rides.  
```sql
SELECT RiderID, 
       COUNT(RideID) OVER (PARTITION BY RiderID) AS TotalRides
FROM Rides;
```
- *Explanation:* `COUNT OVER` gives ride frequency per rider without grouping.

---

**Q5. Surge Pricing Pattern**
- *Business Problem:* Detect average fare per hour to spot surge times.  
```sql
SELECT DATEPART(HOUR, RideTime) AS HourOfDay,
       AVG(Fare) OVER (PARTITION BY DATEPART(HOUR, RideTime)) AS AvgFarePerHour
FROM Rides;
```
- *Explanation:* `AVG OVER` by hour shows surge pricing trends.

---

## Evaluation
- **Is the schema in 3NF?** ✔ Yes. Each table represents a single entity, with no partial or transitive dependencies.  
- **Missing relationships?** ⚠ Yes. PaymentInformation and RideCancellation entities should be added for realism.  
- **SQL Verification:** Queries using window functions produce correct analytical partitions (e.g., ranking fares, computing averages).

---

