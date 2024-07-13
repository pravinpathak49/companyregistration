# from flask import Flask, render_template, request
# import mysql.connector
# import random
# from datetime import datetime

# app = Flask(__name__)

# # Database configuration
# db_config = {
#     'user': 'root',
#     'password': 'Maveric#7',
#     'host': 'localhost',
#     'database': 'company_db'
# }

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         company_name = request.form['companyName']
#         business_type = request.form['businessType']
#         business_location = request.form['businessLocation']
        
#         # Generate a random 6-digit request ID
#         request_id = random.randint(100000, 999999)
        
#         # Set status
#         status = 'Initialized'
        
#         # Get the current date and time
#         request_time = datetime.now()
        
#         # Connect to the database
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()
        
#         # Insert the data into the database
#         query = """
#             INSERT INTO company (company_name, business_type, business_location, request_id, status, request_)
#             VALUES (%s, %s, %s, %s, %s, %s)
#         """
#         cursor.execute(query, (company_name, business_type, business_location, request_id, status, request_time))
#         conn.commit()
        
#         cursor.close()
#         conn.close()
        
#         return render_template('confirmation.html', request_id=request_id)
    
#     return render_template('index.html')

# @app.route('/check-status', methods=['GET', 'POST'])
# def check_status():
#     if request.method == 'POST':
#         request_id = request.form['requestId']
        
#         # Connect to the database
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()
        
#         # Query the status from the database
#         query = "SELECT status FROM company WHERE request_id = %s"
#         cursor.execute(query, (request_id,))
#         result = cursor.fetchone()
        
#         cursor.close()
#         conn.close()
        
#         if result:
#             status = result[0]
#             message = f"Your request is in {status} phase."
#         else:
#             message = "Request ID not found."
        
#         return render_template('check_status.html', message=message)
    
#     return render_template('check_status.html', message="")

# @app.route('/admin', methods=['GET', 'POST'])
# def admin():
#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor(dictionary=True)

#     if request.method == 'POST':
#         request_id = request.form['request_id']
#         new_status = request.form['status']
        
#         # Convert request_id to integer
#         try:
#             request_id = int(request_id)
#         except ValueError:
#             print(f"Invalid request_id: {request_id}")
#             request_id = None

#         if request_id is not None:
#             print(f"Updating request ID {request_id} to status {new_status}")  # Debugging statement
            
#             update_query = "UPDATE company SET status = %s WHERE request_id = %s"
#             cursor.execute(update_query, (new_status, request_id))
#             conn.commit()
#             print(f"Updated {cursor.rowcount} rows.")  # Debugging statement

#     query = "SELECT request_id, company_name, business_type, business_location, status FROM company"
#     cursor.execute(query)
#     requests = cursor.fetchall()
    
#     cursor.close()
#     conn.close()
    
#     return render_template('admin.html', requests=requests)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
from modules.admin.admin import admin_bp
from modules.register.register import register_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(register_bp)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/check-status')
def check_status():
    return render_template('check_status.html')

if __name__ == '__main__':
    app.run(debug=True)
