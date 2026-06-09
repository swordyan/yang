cd E:\my_daily_push
git pull origin master --no-edit
git add .
git commit -m "office update at $(Get-Date -Format 'HH:mm') on $(Get-Date -Format 'yyyy-MM-dd')"
git push origin master
