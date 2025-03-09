# **CT-ThreatGraph: Analyzing Global Terrorism Data using Multigraph and AI** 🌍

## **Overview**
CT-ThreatGraph is an AI-powered analytical tool designed to study global terrorism trends by leveraging multigraph analysis and machine learning. The project processes complex terrorism datasets, enabling pattern detection, predictive modeling, and decision support for counter-terrorism efforts. 

By integrating graph-based AI, advanced visualization techniques, and a hybrid query processing engine, CT-ThreatGraph offers an innovative approach to understanding terrorism networks and their underlying connections.

## **Motivation**
The Global Terrorism Database (GTD) contains detailed records of terrorist activities worldwide. Analyzing this vast dataset manually is challenging due to its scale and complexity. Our goal is to develop an AI-driven system that automates the extraction of insights, enabling security analysts and researchers to:
- Identify high-risk regions and timeframes.
- Analyze relationships between terrorist groups, attack types, and targets.
- Predict potential future threats based on historical patterns.

## **Problem Statement**
Terrorism-related datasets contain unstructured and complex relationships between entities such as terrorist organizations, locations, attack types, and weapon types. Traditional tabular analysis fails to capture these intricate connections.  
CT-ThreatGraph addresses this by using **graph-based AI** to:
- Model terrorism data as a **multigraph** (nodes: entities, edges: relationships).
- Enable **natural language querying** for intuitive data retrieval.
- Provide **interactive 3D visualizations** for pattern recognition.
- Combine **graph databases and ML models** for predictive analytics.

---

## **Tools & Technologies Used**
CT-ThreatGraph leverages a powerful tech stack combining **graph analytics, machine learning, and AI-driven natural language processing**:

### **1. Graph Processing**
- **NetworkX** – For graph-based algorithms such as shortest path, centrality analysis, and node classification with Cugraph by Nvdia for GPU  Acceleration
- **ArangoDB** – A multi-model NoSQL database used for efficient **graph storage and AQL (Arango Query Language)** execution.
- **Plotly** – Used to create interactive **3D visualizations** of the graph.

### **2. Machine Learning**
- **XGBoost** – Used for predicting relationships between entities in the dataset.
- **Scikit-learn** – For training various ML models on extracted features.
- **LLM (Large Language Models)** – Used for natural language understanding, query translation, and data enrichment.

### **3. Data Processing**
- **Pandas & NumPy** – For loading, cleaning, and manipulating the dataset.
- **GeoPandas** – For spatial analysis and mapping terrorist incidents.

### **4. Backend & Query Processing**
- **Hybrid Query Processing Engine** – A combination of **NetworkX (local computation) and AQL (database queries)** to provide optimized results.
- **Python (FastAPI / Flask)** – For handling API requests.
- **LangChain** – For orchestrating AI-powered query execution.

### **5. UI & Visualization**
- **Streamlit** – For building an interactive web-based UI.
- **D3.js / Plotly** – To create real-time network graphs and 3D node-link diagrams.

---

## **Challenges Faced**
### **1. Designing Logic for Hybrid Query Processing**
One of the biggest challenges was determining **when to use NetworkX vs. ArangoDB** for processing queries.  
- **NetworkX is efficient** for small graph computations (local shortest paths, neighborhood analysis).  
- **AQL (ArangoDB)** is more efficient for large-scale traversals and global queries.  
- The solution: **a decision-making module** that dynamically selects the appropriate processing engine based on query complexity.

### **2. Handling Large Datasets Efficiently**
- The GTD dataset contains **thousands of nodes and edges**, making direct visualization difficult.
- Implemented **edge filtering and node sampling techniques** to prevent graph cluttering.
- Used **batch processing and indexing in ArangoDB** to optimize large-scale queries.

### **3. Natural Language Query Interpretation**
- Mapping human language to structured queries required **prompt engineering with LLMs**.
- Some queries needed **multi-step reasoning**, requiring **step-by-step query breakdown and execution**.
- **Solution:** A **query planner** that converts high-level NL queries into **subtasks executed in order**.

---

## **Project Impact**
CT-ThreatGraph enables security researchers, policymakers, and intelligence agencies to:
✅ **Visualize complex terrorism networks dynamically.**  
✅ **Discover hidden patterns & relationships in attack data.**  
✅ **Predict high-risk areas using AI-powered risk assessment.**  
✅ **Execute natural language queries for intuitive analysis.**  

With **real-time analytics and AI-driven insights**, this project enhances the ability to **understand, anticipate, and mitigate** terrorist threats.

---

## **Future Enhancements**
- **Integration with Neo4j for enhanced graph querying.**  
- **Fine-tuning LLMs for better natural language query interpretation.**  
- **Deploying as a full-scale interactive web application using Streamlit / Flask.**  
- **Expanding the dataset to include real-time threat intelligence feeds.**  

---

## **Conclusion**
CT-ThreatGraph is a step forward in applying **AI and graph-based analytics** to counter-terrorism research. By fusing **graph theory, machine learning, and NLP**, the project provides a **comprehensive analytical platform** that helps experts **extract insights from complex datasets** and **predict future threats**.

---
