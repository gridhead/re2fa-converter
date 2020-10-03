# re2fa-converter

We love contributions from everyone.
By participating in this project,
you agree to abide by the [code of conduct](https://github.com/t0xic0der/re2fa-converter/blob/master/CODE_OF_CONDUCT.md)

We expect everyone to follow the code of conduct
anywhere in this project codebases,
issue trackers, chatrooms, and mailing lists.

## Contributing Code

Below are the steps to be followed to contribute to the repository. Lets together make this a wonderful repository. 💪

### 1. Find an issue or Create your issue

![image](https://user-images.githubusercontent.com/35392585/94846898-81ad4880-043f-11eb-8e75-3f93f753153e.png)

- Take a look at the Existing issues or create your own issues! [Link](https://github.com/t0xic0der/re2fa-converter/issues) 
- Comment on the issue.
- Wait for the admin to assign the issue to you after which you can start working on it.


Note: Your PR will only be approved if you are assigned to that issue. Also, every small project must have an associated issue for it.

### 2. Fork the Project

![image](https://user-images.githubusercontent.com/35392585/94847432-347da680-0440-11eb-972c-a8881972957b.png)


- Fork this Repository. This will create a local copy of this Repository on your GitHub Profile. 
```
$ git clone https://github.com/<your-username>/re2fa-converter
```

Now, let's add a reference to the original [Repository](https://github.com/t0xic0der/re2fa-converter) repository using

```sh
$ git remote add upstream https://github.com/t0xic0der/re2fa-converter.git
```

> This adds a new remote named ***upstream***.

- If you have already forked the project, update pull from the upstream before working.
```
$ git remote update
$ git checkout <branch-name>
$ git rebase upstream/<branch-name>
```

### 3. Branch

Create a new branch. Follow the branch creation rule. 
#### BRANCH CREATION RULE
* Go to [this](https://github.com/t0xic0der/re2fa-converter/issues) link and see the issues created by you or assigned to you.
* Create a new branch for each issue in your forked repository.
* The name of your branch should follow the following rule: **[ISSUE NO #]-[SUITABLE NAME ACCORDING TO THE TITLE OF THE ISSUE(all lowercase letters and words separated by a hyphen(-))]**.
* That is, if the *TITLE* of the issue **#8** is **Dashboard - Development for Hospital**, then the branch name should be **8-hospital-dashboard**

```
$ git checkout -b branch_name
```

### 4. Work on the issue assigned
- Work on the issue(s) assigned to you. 
- Create a new folder with a suitable name. 
- Add all the files/folders needed.
- After you've made changes or made your contribution to the project add changes to the branch you've just created by:
```
# To add all new files to branch Branch_Name
$ git add .
```
### 5. Commit
- To commit, give a descriptive message for the convenience of the reviewer by:
```
# This message get associated with all files you have changed
$ git commit -m 'message
```

### 6. Push your work to GitHub

- Finally, push your work in your branch in GitHub.

```
$ git push -u origin Branch_Name
```

### 7. Pull Request (PR)

![image](https://user-images.githubusercontent.com/35392585/94847670-84f50400-0440-11eb-825e-b2d27afd483f.png)

- Go to your repository in the browser and click on compare and pull requests. Then add a title and description to your pull request that explains your contribution. You can use the PR template to describe your work.
- Treat `master` branch as your master branch, i.e. all your PRs should use `master` as the target branch.
- Congrats! Your PR has been submitted and will be promptly reviewed, and suggestions would be added by the admin to improve it.
- Add Screenshots to help us know what this issue is all about.
- Finally, the admin will merge it.


> **_all the contributions from anyone to improve/add new code to this project are welcomed. Every small contribution matter and we are thankful to all the contributors. 😇_**
