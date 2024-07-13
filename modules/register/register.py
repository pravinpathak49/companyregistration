from flask import Blueprint, render_template, request
import mysql.connector
import random
from datetime import datetime

register_bp = Blueprint('register_bp', __name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': 'Maveric#7',
    'host': 'localhost',
    'database': 'company_db'
}

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        company_name = request.form['companyName']
        business_type = request.form['businessType']
        business_location = request.form['businessLocation']
        
        # Generate a random 6-digit request ID
        request_id = random.randint(100000, 999999)
        
        # Set status
        status = 'Initialized'
        
        # Get the current date and time
        request_time = datetime.now()
        
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Insert the data into the database
        query = """
            INSERT INTO company (company_name, business_type, business_location, request_id, status, request_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (company_name, business_type, business_location, request_id, status, request_time))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return render_template('confirmation.html', request_id=request_id)
    
    return render_template('index.html')

@register_bp.route('/check-status', methods=['GET', 'POST'])
def check_status():
    if request.method == 'POST':
        request_id = request.form['requestId']
        
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Query the status from the database
        query = "SELECT status FROM company WHERE request_id = %s"
        cursor.execute(query, (request_id,))
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if result:
            status = result[0]
            message = f"Your request is in {status} phase."
        else:
            message = "Request ID not found."
        
        return render_template('check_status.html', message=message)
    
    return render_template('check_status.html', message="")
