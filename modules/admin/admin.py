from flask import Blueprint, render_template, request
import mysql.connector

admin_bp = Blueprint('admin_bp', __name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': 'Maveric#7',
    'host': 'localhost',
    'database': 'company_db'
}

@admin_bp.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        request_id = request.form['request_id']
        new_status = request.form['status']
        
        # Convert request_id to integer
        try:
            request_id = int(request_id)
        except ValueError:
            print(f"Invalid request_id: {request_id}")
            request_id = None

        if request_id is not None:
            print(f"Updating request ID {request_id} to status {new_status}")  # Debugging statement
            
            update_query = "UPDATE company SET status = %s WHERE request_id = %s"
            cursor.execute(update_query, (new_status, request_id))
            conn.commit()
            print(f"Updated {cursor.rowcount} rows.")  # Debugging statement

    # Fetch all requests from the database
    query = "SELECT * FROM company"
    cursor.execute(query)
    requests = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('admin.html', requests=requests)

@admin_bp.route('/update_status', methods=['POST'])
def update_status():
    if request.method == 'POST':
        request_id = request.form['request_id']
        new_status = request.form['status']
        
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Update the status in the database
        query = "UPDATE company SET status = %s WHERE request_id = %s"
        cursor.execute(query, (new_status, request_id))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return 'Status updated successfully'

    return 'Invalid request'

