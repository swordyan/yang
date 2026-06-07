cd E:\my_daily_push
git pull origin master --no-edit
git add .
git commit -m "auto update all files at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
git push origin master
