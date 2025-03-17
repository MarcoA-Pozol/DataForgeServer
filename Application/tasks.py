import time
import json
from django.contrib.auth import get_user_model
# Caching, table generation, response
from django.http import JsonResponse
from prettytable import PrettyTable
from django.core.cache import cache
# PDF generation, Email sending
from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas

CACHE_KEY = 'cached_users' # Unique key for caching the users
CACHE_TIMEOUT = 10 # 15 minutes

def second_plane_task():
    statement = 100
    for i in range (0, statement+1):
        print(f"Second plane process statement: {i}%")
        time.sleep(0.1)
    print("Load completed")

def store_db_users_on_cache():
    """
    This method checks if the requested users are saved on cache, 
    if not, then it requests user's non-sensitive info from the database 
    and stores them in Redis's cache.
    """

    # Check if users are in cache.
    cached_users = cache.get(CACHE_KEY)
    if cached_users:
        print('Users obtained from cache.')
        users_list = json.loads(cached_users)
    else:
        # Retrieve data from User model.
        print('Obtaining users from database.')
        User = get_user_model()
        users = list(User.objects.values('id', 'username', 'email', 'country', 'language'))

        # Convert the list of dictionaries into JSON string
        users_json = json.dumps({'users': users})

        # Load JSON back into Python dictionary
        users_dict = json.loads(users_json)  # This is a dictionary: {'users': [...]}
        users_list = users_dict["users"]  # Extract only the list of users

        # Create a PrettyTable instance
        table = PrettyTable(field_names=["id", "username", "email", "country", "language"])

        # Add rows to PrettyTable
        for user in users_list:
            table.add_row([user["id"], user["username"], user["email"], user["country"], user["language"]]) 

        # Print table multiple times to simulate real-time updates (Showing data with table every 10 seconds during 2 hours).
        # for i in range(720):
        #   print(table)
        #   time.sleep(10)

        for i in range(10):
            cache.set(CACHE_KEY, json.dumps(users), timeout=CACHE_TIMEOUT)
            print('Saving users on Cache.')
            time.sleep(20)

    return JsonResponse({'users': users_list})  # Return the JSON response properly

def generate_users_pdf_report(file_path:str='reports/pdf/users_report.pdf') -> None:
    """
        This method generates a report of users and save it in PDF format to be sent to an specific email adress.
    """ 

    # Obtaining list of users from database
    User = get_user_model()
    users = list(User.objects.values('id', 'username', 'email', 'country', 'language'))

    # Format the data as a readable string
    users_text = "\n".join(
        [f"{user['id']}: {user['username']} ({user['email']}) - {user['country']} [{user['language']}]" for user in users]
    )

    for i in range(5):
        time.sleep(5)
        # Generating pdf file
        c = canvas.Canvas(file_path) # The pdf file name.
        c.drawString(100, 750, 'Users Report') # Title inside the document

        # Inserting one user per line from the users text (list)
        y_position = 730
        for line in users_text.split('\n'):
            c.drawString(100, y_position, line)
            y_position -= 20

        c.save()

        # Sending pdf file to email adress
        email = EmailMessage('Users Report', 'Users Report Fixed File', to=['marcoantoniopozolnarciso@gmail.com'])
        email.attach_file(file_path)
        email.send()
        time.sleep(15)

def retrieve_current_user_data(user:object):
    """
        Retrieves current authenticated user's data.
    """ 
    print("Fetching user from Database")
    User = get_user_model()
    try:
        user_data = User.objects.filter(username=user.username).values().first()
    except Exception as e:
        error =  {'error': e, 'details': 'It was not possible to fetch the provided user from the database.'}
        print("ERROR:", error)
        return error
    
    for i in range(5):
        print("User JOTASON:", user_data)
        time.sleep(10)
    print('Background task completed!')