from django.urls import path
from . import views

urlpatterns = [
    path("",views.Homepage, name = "Home") ,
    path("deposits/<int:id>/",views.Depositpage, name = "Deposit") ,
    path("transfer/<int:id>/",views.Transfer, name = "Transfer") ,
    path("transactionhistory/",views.Historypage, name = "History") ,
    path("withdraw/<int:id>/",views.Withdraw, name = "Withdraw"),
    path("Users/",views.Userpage, name = "users" )

]

