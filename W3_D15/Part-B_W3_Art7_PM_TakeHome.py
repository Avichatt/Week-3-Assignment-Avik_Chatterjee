"""
Part B — Stretch Problem (30%)

Research BCNF (Boyce-Codd Normal Form). 
Find or create a schema that is in 3NF but violates BCNF. 
Show the violation and the decomposition to BCNF. 
When is it acceptable to leave a schema in 3NF instead of decomposing to BCNF?
"""


  
# Boyce‑Codd Normal Form (BCNF)

**Definition**  
BCNF is a stronger version of the Third Normal Form (3NF).  
A relation is in BCNF if, for every non‑trivial functional dependency \(X \to Y\), \(X\) is a superkey.

---

## 1. Schema in 3NF but Violating BCNF
**Example: University Tutoring Database**

**Table:**  
```
Tutoring(student_id, subject, tutor_id)
```

**Functional Dependencies (FDs):**
1. {student_id, subject} → tutor_id  
   (A student takes a subject from a specific tutor)  
2. tutor_id → subject  
   (Each tutor teaches only one subject)

**Candidate Keys:**
- {student_id, subject}  
- {student_id, tutor_id} (since tutor_id implies subject)

**Why it is in 3NF:**  
- For FD 2 (tutor_id → subject), the attribute `subject` is part of a candidate key ({student_id, subject}).  
- In 3NF, a dependency \(X \to Y\) is allowed if \(Y\) is a prime attribute (part of a candidate key). This condition is satisfied here.

**Why it violates BCNF:**  
- In BCNF, for FD 2 (tutor_id → subject), `tutor_id` must be a superkey.  
- But `tutor_id` alone is **not** a superkey (it doesn’t determine `student_id`).  
- Therefore, the schema fails BCNF.

---

## 2. Decomposition to BCNF
To fix this, decompose into two tables:

1. **TutorSubject(tutor_id, subject)**  
   - Primary key: tutor_id  
2. **StudentTutor(student_id, tutor_id)**  
   - Primary key: {student_id, tutor_id}

Now both tables are in BCNF because the determinants (`tutor_id` and `{student_id, tutor_id}`) are superkeys.

---

## 3. When is it Acceptable to Stay in 3NF?
- Decomposing to BCNF can sometimes cause **loss of dependency preservation**.  
- In the original schema, FD {student_id, subject} → tutor_id was preserved.  
- After decomposition, enforcing this FD requires a **join** across tables.  
- If dependency preservation is more critical for performance and integrity than eliminating redundancy, developers may choose to keep the schema in 3NF.

---


