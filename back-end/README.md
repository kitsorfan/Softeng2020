# **📃 Back-end**

## **📚 Backend Structure**
- Database scheme
- Data generators & dump files
- API.py

<br>

## **📌 Prerequisites**
```bash
sudo apt-get install python-dev default-libmysqlclient-dev libssl-dev

pip3 install -r requirements.txt

pip3 install -r secondary_requirements.txt
```

<br>

## 💡 Execution Steps

### **1. Exporting API**
```bash
export FLASK_APP=api.py		
```
or for Windows 
```bash
set FLASK_APP=api.py
```
or for debug mode
```bash
export FLASK_ENV=development
set FLASK_DEBUG=1
```
### **2. Running the flask server**
```bash
flask run -h localhost -p 8765 --cert=adhoc
```

<br>

## **✅ Testing**
Manual testing through **Postman**.


