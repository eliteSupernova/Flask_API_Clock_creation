from flask import Flask
import datetime

app=Flask(__name__)

# dt=datetime()
countries=['AMERICA','LONDON','CANADA','BRAZIL','JAPAN','CHINA']
cont_hours=[datetime.timedelta(hours=10,minutes=29,seconds=42),datetime.timedelta(hours=5,minutes=29,seconds=42),datetime.timedelta(hours=10,minutes=29,seconds=42),datetime.timedelta(hours=10,minutes=29,seconds=42),datetime.timedelta(hours=10,minutes=29,seconds=42),datetime.timedelta(hours=10,minutes=29,seconds=42)]
world_clock={}

def con_time(t):
    h=t.hour
    m=t.minute
    s=t.second
    time=datetime.timedelta(hours=h,minutes=m,seconds=s)
    return time

def strf(f):
    time_format=f.strftime('%I:%M:%S %p')
    return time_format


@app.route('/',methods=['GET','POST'])
def cur_time():
    now=datetime.datetime.now().time()
    time=strf(now)
    print()
    return f'<h1>MUMBAI : {time}<h1>'


@app.route('/london',methods=['GET','POST'])
def lon_time():
    now=datetime.datetime.now().time()
    cur=con_time(now)
    cur_sec=cur.total_seconds()
    london_time=cur-datetime.timedelta(hours=5,minutes=29,seconds=43)
    lon_sec=london_time.total_seconds()
    total_sec=cur_sec-lon_sec
    hours=total_sec/60/60
    str_lon=str(london_time)
    time=datetime.datetime.strptime(str_lon,'%H:%M:%S').time()
    lon_tim=strf(time)
    timezone=''
    if now.hour>time.hour:
        timezone=timezone+'ahead'
    else:
        timezone=timezone+'behind'
    return f'<h1>LONDON : {lon_tim}</h1> {timezone} {round(hours,2)} hrs'


@app.route('/brazil',methods=['GET','POST'])
def zil_time():
    now=datetime.datetime.now()
    tim_now=now.time()
    cur=con_time(tim_now)
    cur_sec=cur.total_seconds()
    brazil_time=now-datetime.timedelta(hours=8,minutes=29,seconds=43)
    zil_sec=con_time(brazil_time).total_seconds()
    total_sec=cur_sec-zil_sec
    hours=total_sec/60/60
    str_zil=str(brazil_time)
    time=datetime.datetime.strptime(str_zil,'%Y-%m-%d %H:%M:%S.%f')
    bra_time=time.time()

    zil_tim=strf(bra_time)
    return f'<h1>BRAZIL : {zil_tim}</h1> behind {round(hours,2)} hrs'


if __name__=="__main__":
    app.run(debug=True)
