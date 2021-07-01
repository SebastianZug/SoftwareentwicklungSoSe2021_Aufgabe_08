import os

github_token = os.environ['TOKEN']
git_repo_name = os.environ['CI_REPOSITORY_NAME']
git_repo_owner = os.environ['CI_REPOSITORY_OWNER']

readmefilename = "README.md"
shieldfilename = ".github/workflows/ShieldsTemplate.md"

with open(shieldfilename, 'r') as filehandle:
    shields = filehandle.read()

shields = shields.replace("<CI_REPOSITORY_OWNER>", git_repo_owner)
shields = shields.replace("<CI_REPOSITORY_NAME>", git_repo_name)

with open(readmefilename, 'r') as filehandle:
    readmecontent = filehandle.read()

with open(readmefilename, 'w') as filehandle:
    filehandle.write(shields + "\n" + readmecontent)