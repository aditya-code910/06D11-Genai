# Multimodal Manufacturing Creator

## Overview

This project demonstrates how **Generative AI** can be used to bridge the gap between concept and visualization in manufacturing systems.

The user provides a simple prompt such as **"Design a robotic arm"**, and the system generates:

- A structured explanation of the manufacturing system  
- A visual representation of the concept  

The application integrates both **text and image generation** to deliver a multimodal output.

---

## Key Features

- **Multimodal output** (text and image)  
- **AI-based text generation** using Large Language Models  
- **AI-based image generation** using diffusion models  
- **Flask-based REST API backend**  
- Integration with external AI services  
- Containerized deployment using **Docker**  
- Scalable deployment using **Kubernetes**  

---

## System Workflow

1. The user enters a **manufacturing-related prompt** through the frontend interface  
2. The request is sent to the **Flask backend** via an HTTP POST request  
3. The backend processes the input and sends it to:  
   - A **Large Language Model API** for text generation  
   - An **image generation model** for visual output  
4. The backend receives both responses  
5. The outputs are combined into a **structured JSON response**  
6. The frontend displays both the generated **text and image**  

---

## Architecture

The system follows a **layered architecture**:

- **Frontend Layer**  
  Handles user input and displays output  

- **Backend Layer (Flask)**  
  Processes requests and integrates APIs  

- **AI Services Layer**  
  - LLM for text generation  
  - Diffusion model for image generation  

- **Deployment Layer**  
  - Docker for containerization  
  - Kubernetes for orchestration and scalability  

---

## Technologies Used

- **Python**  
- **Flask**  
- **HTML, CSS, JavaScript**  
- **OpenRouter (LLM API)**  
- **HuggingFace (Stable Diffusion)**  
- **Docker**  
- **Kubernetes**  

---

## Results

The project successfully demonstrates:

- Integration of **Generative AI** into a real-world application  
- Simultaneous **text and image generation**  
- Backend API handling and response formatting  
- Deployment using **containerization and orchestration tools**  

---

## Limitations

- No database integration  
- Basic user interface  
- Dependency on external APIs for AI generation  
- Local deployment environment  

---

## Future Scope

- Integration with **vector databases** (RAG systems)  
- Improved image generation models  
- Cloud deployment (**AWS, Azure, GCP**)  
- Advanced frontend frameworks (**React**)  
- User authentication and data storage  
