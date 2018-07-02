Website update instructions:

Note: at some point, read:
* https://www.digitalocean.com/community/tutorials/how-to-set-up-uwsgi-and-nginx-to-serve-python-apps-on-ubuntu-14-04
* https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04
* https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-applications-using-uwsgi-web-server-with-nginx

# Update HTML/CSS files on website:

1. Update files in `development/personal_website` locally
2. Use `update_website` commmand
3. Full command: `scp -r -i ~/.ssh/Lucia_2.pem.txt ~/personal_website/* ec2-user@ec2-54-90-232-170.compute-1.amazonaws.com:/home/ec2-user/weidman`

# Update Flask app:

## Test locally:

1. `cd development/personal_website/wsgi-scripts`
2. python3 routes.py  
3. Fix errors

## When ready to run on website:

1. Upload files to website following steps above

### Restart server:

1. `ps aux | grep uwsgi`
2. `kill -9 <pid>`
3. `cd ~/weidman/wsgi-scripts/`
4. `source ~/weidman/venv/bin/activate` - here you can `pip install` packages
if you need to
5. `uwsgi --socket 127.0.0.1:8080 --wsgi-file routes.py --callable app`
