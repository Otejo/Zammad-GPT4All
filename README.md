# Zammad-GPT4ALL
Suggest ticket response in Zammad using GPT4ALL

To get things started:

On the server with GPT4all:
go to gpt_server/

setup environment:  
python3 -m venv venv (install venv if need, "sudo apt install python3-venv)
source venv/bin/activate
pip install "uvicorn[standard]"
pip install -r requirements.txt

run: uvicorn main:app --reload --host 0.0.0.0

On the server running Zammad:

go to zammad_server/
setup environment
python3 -m venv venv
source venv/bin/activate
pip install "uvicorn[standard]"
pip install -r requirements.txt

update main.py file to include the appropriate ip/hosts and email address for the admin/service account. 
set os environment variable to the appropriate Zammad password 

gpt4all_address = "x.x.x.x:8000"
zammad_address = "x.x.x.x"
zammad_secret = os.environ.get("zammad_password")
zammad_email = 'admin_email@forZammad.com'

e.g. 
export zammad_password=mycomplexpassword123
gpt4all_address = "192.168.1.100:8000"
zammad_address = "192.168.1.200"
zammad_secret = os.environ.get("zammad_password")
zammad_email = 'myemail@address.com'
