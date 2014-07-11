git pull
chown escolapravalerco /home/escolapravalerco/EscolaPraValer/* -R
chgrp escolapravalerco /home/escolapravalerco/EscolaPraValer/* -R
cd /home/escolapravalerco/EscolaPraValer
pkill -f runescolacherry
cp site.log site.log.bkp
rm site.log
python runescolacherry.py & 
