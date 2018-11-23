from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sms/', views.SendSMS.as_view(), name='send_sms'),
    path('account/recharge', views.RechargeAccountView.as_view(), name='recharge_account'),
    path('recharge/verify', views.ConfirmTransacionView.as_view(), name='confirm_transaction'),
    path('airtime/recharge', views.AirtimeRechargeView.as_view(), name='airtime_recharge'),
    path('history/', views.HistoryView.as_view(), name='history'),
]
