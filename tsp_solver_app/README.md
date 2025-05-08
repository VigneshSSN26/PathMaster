# TSP Solver Application

A user-friendly Travelling Salesman Problem (TSP) solver that enables users to input data, choose solving methods, and visualize optimized routes. This project showcases algorithmic thinking, optimization strategies, and intuitive UI design.

## ✨ Features

- 🔢 **Dynamic Programming (DP):** Optimal solution for small-sized datasets.
- 🧭 **Nearest Neighbour Heuristic:** Fast approximation for larger datasets.
- 🖼️ **Route Visualization:** Displays the calculated path on a 2D plot or map.
- 🧠 **Smart Method Selection:** Automatically selects the best solving method based on dataset size.
- 📋 **Custom Input Interface:** Easy-to-use UI for adding cities and distances manually.

## 🧰 Tech Stack

- **Frontend:** HTML/CSS/JavaScript
- **Backend:** Python with Flask
- **Visualization:** Matplotlib
- **Algorithms:** Dynamic Programming, Nearest Neighbour

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed:

```bash
python --version
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

### Run the App

```bash
python app.py
```

Open your browser and go to `http://localhost:5000`.

## 📁 Project Structure

```
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── tsp/
│   ├── dynamic_programming.py
│   └── nearest_neighbour.py
└── README.md
```

## 📄 License

This project is licensed under the MIT License.
