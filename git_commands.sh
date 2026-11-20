# 1. Move into the project folder
cd my-web-project

# 2. Initialise a local Git repository
git init

# 3. Add project files to the staging area
git add .

# 4. Save the first version
git commit -m "Initial web technology project"

# 5. Create and switch to a feature branch
git switch -c feature-update

# 6. After editing and saving files, commit the changes
git add .
git commit -m "Add feature update"

# 7. Return to the main branch and merge the feature branch
git switch mains 
git merge feature-update

# 8. Connect the local repository to the GitHub repository
git remote add origin https://github.com/USERNAME/REPOSITORY.git

# 9. Push the main branch to GitHub
git push -u origin main

# For later updates
git add .
git commit -m "Update project"
git push
