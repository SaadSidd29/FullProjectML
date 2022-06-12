Start Machine Learning project.

Software and account Requirement.

1. Github Account
2. Heroku Account
3. VS Code IDE
4. GIT cli

Creating conda version
````
conda create -p venv python==3.7 -y
````

conda activate venv/

pip install -r requirements.txt

Make app.py file

Ignore venv folder in gitignore under Environments heading

To add files to git 

1. git add .
2. git add <filename/s>

To ignore file/folder from git

1. Write file/folder name in .gitignore file

To check git status

1. git status

To check all version mainatained by git

1. git log

To create version/commit all changes by git

1. git commit -m "message"

Send/Push changes/versions to github

1. git push origin <branch_namme>

To check remote url

1. git remote -v

To check current branch 

1. git branch

Diff 

1. git diff


To setup CI/CD pipeline in heroku we need 3 info

1. HEROKU_EMAIL=saad.sidd29@gmail.com
2. HEROKU_API_KEY=2d4ccb31-c6ac-45a8-b900-4ef793a5e380
3. HEROKU_APP_NAME=ml-ful-deploy


Create a docker file and dockerignore file

Build docker image

1. docker build -t <img-name>:<tag-name> .

> Note : Image name for docer must be small case