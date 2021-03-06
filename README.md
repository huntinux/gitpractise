# Getting Started


## 新建project
到`http://github.com/` 点击`New project`
输入Project name，Description。点击`Create project`
然后页面会有一些提示：

```sh
# Git global setup:

git config --global user.name "曹洪瑾"
git config --global user.email "huntinux@gmail.com"

# Create Repository

mkdir newproject
cd newproject
git init
touch README
git add README
git commit -m 'first commit'
git remote add origin https://github.com/huntinux/gitpractise.git
git push -u origin master

# Existing Git Repo?

cd existing_git_repo
git remote add origin git地址
git push -u origin master

```
根据以上提示，可以新建一个project, 它只包含一个README文件。

## 添加文件

```sh
touch newfile
git add newfile 
git commit -m 'add a newfile'
git push origin master

```

## 删除文件

```sh
git rm newfile 
git commit -m 'del the newfile'
git push origin master
```

## branching

```sh
git checkout -b branch1 # create branch1 and jump to it 
vim README		# modify something
git commit -a -m 'add some text to README.md [branch1]' # commit
git push origin branch1 # push
```

## merging

```sh
git checkout master	# to master branch1
git merge branch1	# merge branch1 to master
git branch -d branch1	# delete branch1
git push origin master	# push 
```
## 删除本地分支
```sh
git branch -d branch-name	
```

## 删除远程分支
```sh
git push origin :branch-name # 冒号前面的空格不能少，原理是把一个空分支push到server上，相当于删除该分支。
```

## 新建目录 

```sh
mkdir newdir	
touch newdir/newfile
git add newdir
git commit -m 'add new dir'
git push origin master
```

## 删除目录
```sh
git rm -r newdir
git commit -m 'del new dir'
git push origin master
```
## 使用virtualenv tools 
将python-sample中的tools加入了project，方便使用virtualenv。

## clone 指定分支
```sh
git clone -b <branch> <remote_repo> 
example: clone nginx-0.1 branch
git clone -b nginx-0.1 https://github.com/nginx/nginx.git 
```
