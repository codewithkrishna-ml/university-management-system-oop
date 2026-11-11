# University & Student Management System 🎓🏛️

An enterprise-inspired academic administration and ERP console engine built in Python using core **Object-Oriented Programming (OOP)** architectures. This system seamlessly coordinates interactions between Students, Faculty Professors, and dynamic Course catalogs—managing seat limits, subject assignments, and automated credit-weighted CGPA computations.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML) -> **Aspiring ML Engineer at Google / Microsoft** 🤖⚡
*   **Milestone:** Successfully completed the **100 Days of Code** challenge and built a **25+ Project Python OOP Portfolio**!
*   **Current Focus:** Mastering Data Structures & Algorithms (DSA) and building data science workflows with **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Role-Based Academic Registry:** Distinctly manages registration profiles for `Student` entities and `Professor` faculty members along with their specific departments.
*   **Dynamic Course & Seat Management:** Allows administrators to launch courses with defined credit weights and maximum enrollment caps (`max_seats`), automatically blocking over-enrollments once seats fill up.
*   **Faculty Assignment Pipeline:** Links registered professors directly to specific courses, updating both course metadata and faculty schedules simultaneously.
*   **Credit-Weighted CGPA Engine:** Automatically evaluates student performance across multiple enrolled subjects (`calculate_gpa`), multiplying earned grade points by individual course credits to output an accurate cumulative GPA.
*   **Comprehensive Academic Transcripts:** Generates clean student report cards displaying basic profile info, individual subject grades (`Pending` vs graded), and live CGPA standing.

---

## 🛠️ OOP Concepts & Engineering Architecture

This project serves as a strong demonstration of modular software design and multi-class relationships:
*   **Hierarchical Inheritance:** Structures `Student` and `Professor` subclasses cleanly underneath a shared `Person` super-class, reusing core identity attributes (`person_id`, `name`, `email`) via `super().__init__()`.
*   **Deep Composition & Cross-Referencing:** The master `UniversityManager` controller orchestrates runtime lookups across three interconnected dictionaries (`students`, `professors`, `courses`), ensuring data stays synchronized across objects.
*   **Encapsulated Validation Methods:** Uses dedicated helper methods like `has_available_seats()` to keep business logic clean, modular, and easy to read.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd university-management-system-oop
    ```
3.  **Run the interactive university portal:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   **Python 3.x** installed on your machine.
*   Runs completely on pure Python core architectures without needing external third-party library installations.
