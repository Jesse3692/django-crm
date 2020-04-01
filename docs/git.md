# git使用

## 初始化配置

### 配置用户信息

```shell
git config --global user.name "username"
git config --global user.email email_address
```

### 查看配置信息

```shell
git config --list
```

## 远程仓库配置

### 关联远程仓库

```shell
git remote add origin branch_name url
```

### 查看远程仓库

```shell
git remote -v
```

### 将本地仓库内容提交到远程仓库

```shell
git push -u origin master
```

## 查看某一版本信息

```shell
git checkout commit-id
```

## 恢复操作

不想修改原先的已提交的内容

```shell
git checkout .
```
