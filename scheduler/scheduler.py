from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from services.amazon_traker import a_tracker
from services.myntr_traker import m_tracker
from mail_manager.mail import send_mail
from urllib.parse import urlparse


from scheduler.models import GlobalDb

def product_price_check():
    print("Traking!")
    users = GlobalDb.get_users()

    for user in users:
        email = user['email']
        products = user['products']
        u_id = user['_id']
        for p in products:
            if not p['done']:
                p_id = p['_id']
                url = p['url']
                base_price = p['base_price']

                if urlparse(url).netloc == 'www.myntra.com':
                    tr = m_tracker.Tracker(url)
                else:   
                    tr = a_tracker.Tracker(url)
                t_res = tr.check_price(base_price)
                if t_res['status']:
                    m_status = send_mail(url = url,to = email)
                    if m_status['status']:
                        GlobalDb.update(u_id,p_id)    
    return

# product_price_check()

scheduler = BackgroundScheduler()
scheduler.add_job(func=product_price_check, trigger="interval",seconds=10)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())