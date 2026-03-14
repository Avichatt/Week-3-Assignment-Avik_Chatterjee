"""
Day 17 · AM Session · Take-Home Assignment
Part A: Concept Application — Student Grade Analytics Engine
"""

import numpy as np

# 1. Create a 200x8 random grade matrix (scores 0-100, integer, seed=2026)
np.random.seed(2026)
grades = np.random.randint(0, 101, size=(200, 8))

# 2. Calculate averages
student_averages = np.mean(grades, axis=1)
course_averages = np.mean(grades, axis=0)
overall_avg = np.mean(grades)
overall_std = np.std(grades)

print(f"Per-course averages (before curve):\n{np.round(course_averages, 1)}")

# 3. Apply a curve: any course where the average < 50 gets +10 points
# Use broadcasting + boolean logic, cap at 100
low_avg_mask = course_averages < 50
courses_to_curve = np.where(low_avg_mask)[0]
print(f"Courses getting curve: {courses_to_curve.tolist()}")

# Create a curve adjustment array of shape (8,)
curve_adjustment = np.where(low_avg_mask, 10, 0)
# Broadcast adjustment to all students
curved_grades = np.minimum(grades + curve_adjustment, 100)

# 4. Assign letter grades using np.where chains
# A(>=90), B(>=80), C(>=70), D(>=60), F(<60)
letter_grades = np.where(curved_grades >= 90, 'A',
                np.where(curved_grades >= 80, 'B',
                np.where(curved_grades >= 70, 'C',
                np.where(curved_grades >= 60, 'D', 'F'))))

# 5. Find the top 10 students by overall average using argsort
# Recalculate averages based on curved grades
curved_student_averages = np.mean(curved_grades, axis=1)
top_10_indices = np.argsort(curved_student_averages)[-10:][::-1]
print(f"Top 10 student indices: {top_10_indices.tolist()}")

# 6. Create a boolean report: which students passed ALL courses (>=60 in every course)?
passed_all = np.all(curved_grades >= 60, axis=1)
num_passed_all = np.sum(passed_all)
print(f"Students passing all courses: {num_passed_all} out of 200")

# Final verification statistics
print("\n--- Final Summary ---")
print(f"Overall Average (Curved): {np.mean(curved_grades):.2f}")
print(f"Number of 'A' grades awarded: {np.sum(letter_grades == 'A')}")
