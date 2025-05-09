from rest_framework.response import Response
import hashlib,uuid
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def project_data_raw_view(request):

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                p.id, p.project_id, p.project_title, p.description, p.date_added,
                u.user_id, u.username, u.email, u.first_name, u.last_name,
                c.cid, c.title AS category_title, c.description AS category_description, c.project_type
            FROM ilance_projects p
            JOIN ilance_users u ON p.user_id = u.user_id
            LEFT JOIN ilance_categories c ON p.cid = c.cid
        """)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    return Response(results)



@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    with connection.cursor() as cursor:
        cursor.execute("SELECT user_id, password, salt FROM ilance_users WHERE username = %s", [username])
        row = cursor.fetchone()

        if row is None:
            return Response({"status": "fail", "message": "User not found"}, status=404)

        user_id, db_password, salt = row

        # Double MD5 hashing + salt
        hash1 = hashlib.md5(password.encode()).hexdigest()
        hash2 = hashlib.md5(hash1.encode()).hexdigest()
        final_hash = hashlib.md5((hash2 + salt).encode()).hexdigest()

        if final_hash == db_password:
            # Generate a token
            token = str(uuid.uuid4())
            request.session['token'] = token
            request.session['user_id'] = user_id
            print("token",request.session['token'])
            return Response({"status": "success", "token": token, "session_data": dict(request.session)}, status=200)
        else:
            return Response({"status": "fail", "message": "Invalid credentials"}, status=401)
