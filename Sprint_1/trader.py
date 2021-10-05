from initial_setup import *
from td.client import TDClient

#Setup for td ameritrade connection
TDSession = TDClient(
    client_id='12CEWACOWXBGEOPIKQDGPAD1V5QNJU6U',
    redirect_uri='http://127.0.0.1:5500/Sprint_2/index.html',
    credentials_path='C:\Users\Daniel\Desktop\School\Applied Programming\personal_work\Sprint_1\Credentials'
)

#login using session credentials
TDSession.login()