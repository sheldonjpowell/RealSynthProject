Copying this repository (and following a few steps) should give you a starter flask application with a working user_login
To remove the user section, delete the auth blueprint, and any references to the login / sign up pages


Step 0: Tutorial
---- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
---- https://elemental-flat-e5b.notion.site/The-Ultimate-Flask-Tutorial-111c0b0b64d9449a8e4aefea44d60a66

Step 0.5: Pulling from git
---- Open a terminal in the folder/directory you want this starter in 
---- enter the following lines:
	---- git init 
		 git remote add starter https://github.com/NathanPerrine/My_Flask_Starter
		 git remote -v 
			---- Checks to see if the new remote is correctly added
		 git pull starter main
		 git remote rm starter 
			---- Removes the remote you just created (no longer needed)

Step 1: Create a python virtual environment
---- python -m venv {venv_name}

Step 2: Activate Venv 
---- <name-of-environment>\Scripts\activate
---- If you're getting an error "flask not found" you're using the wrong python interpreter
---- set python interpreter to the new venv
    ---- ctrl + shift + P 
        ---- Python: Select interpreter
        ---- Select the newly created venv

Step 3: Requirements
---- upgrade pip
    ---- python -m pip install --upgrade pip
---- pip install -r requirements.txt
    ---- set version requirements if needed
    ---- 

Step 4: .gitignore
----Update your gitignore file to not track:
    ---- {venv_name}/ <---- Change name to your venv name
    ---- __pycache__/
    ---- .env
    ---- app.db
---- If you have 1k+ untracked changes in your source control you didn't set your own venv_name

Step 5: .env 
---- Create a file called '.env' in the top level folder
---- FLASK_APP=run.py
     FLASK_ENV=development
     SECRET_KEY=
     ---- In the terminal enter 'python'
          import os 
          base64.b64encode(os.urandom(24)).decode('utf-8)
          copy new secret_key
     DATABASE_URL={link to database}
    ---- https://www.elephantsql.com/
    ---- Make sure url starts with "postgresql"
		---- add 'ql' to the end of the 'postgres' at the beginning of the url

Step 6: Database Migration
---- in the terminal:
        flask db init
        flask db migrate
        flask db upgrade

Step 7: templates / base.html
---- Edit Title 
	---- Change base.html title tag to your name	
---- Edit Nav Bar 
    ---- Currently is set to bootstrap navbar - light, bottom border, collapses on small screens 
    ---- Separates the sign up / login / logout to the right of the page
    ---- Has several jinja is authenticated checks to change the navbar options
	---- Update brand name, and name of links when you have them, if not needed remove the a-tag
	


Step x: Blueprints
---- app/__init__.py
    ---- For each blueprint add the following below 'app = flask' before from app import routes
    ---- from app.blueprints.XXXXX import XXXXX
         app.register_blueprint(XXXXX)



Step x: Cloudinary 
---- If you want to store pictures online, upload the images to cloudinary then link the URL generated
---- Sign up for Cloudinary to get your env variables
---- Set .env variables 
---- CLOUDINARY_NAME=
     CLOUDINARY_API_KEY=
     CLOUDINARY_API_SECRET=
---- On the models.py of where you want to upload:
    import cloudinary 
    import cloudinary.uploader 
    import cloudinary.api 

    cloudinary.config(
        cloud_name=os.environ.get('CLOUDINARY_NAME'),
        api_key=os.environ.get('CLOUDINARY_API_KEY'),
        api_secret=os.environ.get('CLOUDINARY_API_SECRET')
    )