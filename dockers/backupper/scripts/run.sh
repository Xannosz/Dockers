ls -td1 /target/* | tail -n +4 | xargs rm -r
zip -r "/target/server-backup-$(date +"%Y-%m-%d").zip" /source