from github2pandas.utility import Utility
from github2pandas.version import Version
from pathlib import Path
import os
import pandas as pd

github_token = os.environ['TOKEN']
git_repo_name = os.environ['CI_REPOSITORY_NAME']
git_repo_owner = os.environ['CI_REPOSITORY_OWNER']
    
default_data_folder = Path("repo")

readmefilename = "./data/README.md"

def replaceTextBetween(originalText, delimeterA, delimterB, replacementText):
    leadingText = originalText.split(delimeterA)[0]
    trailingText = originalText.split(delimterB)[1]
    return leadingText + delimeterA + replacementText + delimterB + trailingText

if __name__ == "__main__":
    print(git_repo_owner, git_repo_name)
    repo = Utility.get_repo(git_repo_owner, git_repo_name, github_token, default_data_folder)
    Version.no_of_proceses = 8
    Version.generate_version_pandas_tables(repo = repo, data_root_dir=default_data_folder)
    
    users = Utility.get_users(default_data_folder)
    print(users)
    pdCommits = Version.get_version(data_root_dir=default_data_folder)
    pdEdits = Version.get_version(data_root_dir=default_data_folder, filename=Version.VERSION_EDITS)

    print(pdCommits.author.unique())
    pdEdits = pdEdits.merge(pdCommits[['commit_sha', 'author', 'commited_at']], left_on='commit_sha', right_on='commit_sha')
    pdEdits = pdEdits.merge(users[['anonym_uuid', 'login']], left_on='author', right_on='anonym_uuid')
    
    # Generate Table 
    pdFileEdits = pdEdits.groupby(['commit_sha']).first()
    counts = pdFileEdits.groupby(['login']).agg({'total_added_lines': 'sum', 'total_removed_lines': 'sum'})
    print(counts.to_markdown())
    with open(readmefilename, 'r') as filehandle:
        filecontent = filehandle.read()
    newfilecontent = replaceTextBetween(filecontent, "## Beiträge", "## Idee der Übung",
                                        '\n\n' + counts.to_markdown() + '\n\n')
    with open(readmefilename, 'w') as filehandle:
        filehandle.write(newfilecontent)


    



