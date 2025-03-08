# Optimization of Scheduling Problems using Graph Coloring Algorithms

## 📌 Introduction
Scheduling problems are prevalent in various domains such as examination timetabling, task scheduling in operating systems, and resource allocation. To optimize such problems efficiently, **Graph Coloring Algorithms** provide an effective solution by minimizing conflicts and ensuring optimal resource utilization.

This project aims to implement graph coloring algorithms to optimize scheduling problems, focusing on techniques like:
- **Greedy Algorithm**
- **Welsh-Powell Algorithm**
- **DSATUR Algorithm**

---

## 🧩 Problem Statement
The goal is to minimize conflicts in scheduling scenarios where resources such as time slots, classrooms, or processors must be allocated efficiently. The project addresses:
- Conflict-free scheduling
- Minimization of resource usage
- Enhanced efficiency through algorithm optimization

---

## 📈 Algorithms Implemented
### 1. **Greedy Algorithm**
- Assigns colors (resources) sequentially to nodes (tasks/events) with minimal conditions.
- Time Complexity: `O(V + E)`

### 2. **Welsh-Powell Algorithm**
- A more efficient method that sorts nodes by degrees before coloring.
- Time Complexity: `O(V^2)`

### 3. **DSATUR Algorithm**
- Dynamically selects the vertex with the highest saturation degree for coloring.
- Time Complexity: `O(V^2)`

---

## ⚙️ Technologies Used
- **Python**
- **NetworkX** (Graph visualization and manipulation)
- **Matplotlib** (For visual representation)
- **Numpy and Pandas** (For data handling)
- **Development Environment: Jupyter Notebook / VS Code** 

---

## 🚀 Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/Optimization-of-Scheduling-Problems-using-Graph-Coloring-Algorithms.git
```
2. Navigate to the project directory:
```bash
cd Optimization-of-Scheduling-Problems-using-Graph-Coloring-Algorithms
```
3. Install dependencies:
```bash
pip install networkx matplotlib
```
4. Run the application:
```bash
python main.py
```

---

## 📋 Usage
- Input your scheduling requirements in the defined format.
- Choose your desired graph coloring algorithm (Greedy, Welsh-Powell, or DSATUR).
- Visualize the optimized schedule output with minimized conflicts.

---

## 📄 Example Input
```
Nodes (Events/Tasks): 5
Edges (Conflicting Tasks): [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4)]
```

### Sample Output
```
Node 0 -> Color 1
Node 1 -> Color 2
Node 2 -> Color 3
Node 3 -> Color 1
Node 4 -> Color 2
```

---

## 📷 Visual Representation
The project provides a graphical representation of the scheduling process, making it easier to understand resource allocations and minimize conflicts.

---

## 🌟 Features
✅ Efficient scheduling with minimal conflicts  
✅ Multiple graph coloring algorithms for comparison  
✅ Visual output for enhanced understanding  
✅ Scalable for complex scheduling scenarios  

---

## 🔎 Future Enhancements
- Integration with real-world data sets (e.g., exam timetables)
- Enhancing the visualization interface
- Adding support for weighted graph scenarios

---

## 🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

---

## 📄 License
This project is licensed under the **MIT License**.

---

## 📬 Contact
For queries or collaborations, reach out at [anshikasaklani894@gmail..com](mailto:your.email@example.com).

