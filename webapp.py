from flask import Flask, render_template,request
import os, subprocess, netifaces, random, requests


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
color = os.environ.get('COLOR')
env_var1 =  os.environ.get('env_var1')
env_var2 =  os.environ.get('env_var2')
env_var3 =  os.environ.get('env_var3')
env_var4 =  os.environ.get('env_var4')

bgcolor1 = '#63c3e9'
bgcolor2 = '#a8d179'
bgcolor3 = '#51d8d8'
bgcolors = [bgcolor1,bgcolor2,bgcolor3]
bgcolor=random.choice(bgcolors)


@app.route('/')
def index():

    cmdOS = """ cat /etc/os-release | grep -Ei "^NAME" | awk 'BEGIN{FS="="} {print $2}'  """
    cmdVersion = """ cat /etc/os-release | grep -Ei "^version_id" | awk 'BEGIN{FS="="} {print $2}'  """

    gateways = netifaces.gateways()
    gateway = gateways['default'][2][0]
    intName = gateways['default'][2][1]

    ip = netifaces.ifaddresses(intName)[2][0]['addr']
    netmask = netifaces.ifaddresses(intName)[2][0]['netmask']

    hostname = subprocess.getstatusoutput("hostname")[1]
    # os.path.exists('/tmp/data'),

    if os.system('df -h | grep /data') == 0 :

        mount = True

        if  os.path.exists('/tmp/data') :
            
            try:
                with open('/tmp/data/message.txt', 'r') as file:
                    texts = file.read()

            except:
                texts = "message.txt not found in /tmp/data"

    else :
        mount = False
        texts = 'volume not mount'

    var1 = {
        'name': hostname,
        'ip': ip,
        'netmask': netmask,
        'gateway': gateway,
        'mount': mount,
        'os-base': subprocess.check_output(cmdOS,shell=True).decode("utf-8").split("\n")[0],
        'os-version': subprocess.check_output(cmdVersion,shell=True).decode("utf-8").split("\n")[0]
    }


    return render_template('webapp.html', page='Index', var=var1, text=texts, color=color,env_var1=env_var1,env_var2=env_var2,env_var3=env_var3,env_var4=env_var4,bgcolor=bgcolor)


if __name__ == '__main__':
    app.run(debug=True,port=30001,host='0.0.0.0')
