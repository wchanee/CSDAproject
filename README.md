# Smart Car Park Surveillance: Machine Learning - Based Object Detection in Shopping Parking Space 🚗🏢

Welcome to  **Smart Car Park Surveillance: Machine Learning - Based Object Detection in Shopping Parking Spaces** project repository! This is my degree project showcasing a cutting-edge solution for urban parking management. 
Our platform is designed to assist city planners, drivers, and sustainability advocates by optimizing parking spaces through intelligent surveillance.
With features like real-time car detection, parking availability insights, and congestion reduction tools, our system is your one-stop solution for enhancing urban mobility and promoting sustainable urban development.

## 🚀 Project Overview
This project leverages **machine learning**, **image processing**, and **urban planning** to optimize urban parking lot management using intelligent surveillance systems. The system employs the **YOLOv8 algorithm** for real-time object detection, enabling efficient identification of available parking spaces.

### 🔑 Key Features:
- **Detection and Analysis**: Utilizing the **YOLOv8 algorithm**, the system performs real-time image object recognition to accurately identify available parking spaces. This speeds up the parking process, reduces congestion, and enhances the user experience.
- **Extensive Data Collection and Preparation**: The project collected over **10,000 images**, which were cleaned and pre-processed to ensure high-quality data for training and analysis.
- **Sustainable Urban Development**: By optimizing parking infrastructure, this project contributes to **Sustainable Development Goal 9** by promoting innovative and sustainable urban technologies.

### 🧰 Technologies Used:
- **Programming Language**: Python
- **Object Detection Algorithm**: YOLOv8
- **Libraries**: OpenCV, NumPy, Ultralytics YOLOv8, etc

### 👍🏼 Benefits:
- Eases urban congestion by reducing the time required to find parking.
- Minimizes environmental impacts through efficient space utilization.
- Encourages smarter, more sustainable urban mobility.
- Provides a scalable and resilient solution for future urban challenges.

### 📄 Project Poster:
![image](https://github.com/user-attachments/assets/823d1f5d-f924-49a2-b959-dbc6234b0e8d)

---

### ？How to Run the Project in VSCode:
Follow these steps to set up and run this Python project on your vccode:

1. Install Python
Make sure Python is installed on your system.
- If Python is not installed, download and install it from [Python](https://www.python.org/downloads/).

2. Install the Python Extension for VS Code
- Open VS Code.
- Go to the Extensions view by clicking on the Extensions icon in the Activity Bar or pressing **Ctrl+Shift+X** / **Cmd+Shift+X**.
- Search for “Python” and install the extension by Microsoft.

3. Clone the Repository
- Open VSCode and go to Terminal > New Terminal.
- Run the following command to clone your repository:
```bash
git clone https://github.com/your-username/urban-parking-management.git
cd urban-parking-management
```
- Replace your-username with your actual GitHub username.

4. Set Up the Python Environment
- Create a Virtual Environment
- It’s best to use a virtual environment for Python projects to manage dependencies separately.
- Open VSCode’s integrated terminal (if not already open) and run the following command to create a virtual environment:
```bash
python -m venv venv
```
- Activate the virtual environment:
```bash
source venv/bin/activate
```
- Once the virtual environment is activated, you should see (venv) at the beginning of the terminal prompt.
- Run the following command to install the required dependencies:
```bash
pip install -r requirements.txt
```

5. Download YOLOv8 weights and download the YOLOv8 pre-trained weights:
- Install the ultralytics package: 
```bash
pip install ultralytics
```

6. Verify Dataset
- Ensure that your dataset is in the proper folder (e.g., data/images/ for the image files and data/labels/ for the label files). The dataset should be configured correctly in your project (likely in a YAML file or similar).

7. Run the app.py Script
- Run it directly from the terminal by typing:
```bash
python app.py
```

8. Access the Application
- If app.py is running a web-based application (e.g., using Flask or FastAPI), you should be able to open a browser and go to the address http://localhost:5000/ (or whatever port your app is configured to run on). This should bring up the interface where you can interact with the parking management system.
- If your project uses something like a GUI or a different interface, follow the on-screen instructions to interact with the system.
