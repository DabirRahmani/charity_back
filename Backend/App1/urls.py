from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('signup', views.signup),
    path('logout', views.logout),
    path('ForgotPassword', views.forgotPassword),
    path('LoadUserProfile', views.loadUserProfile),
    path('SubmitUserProfile', views.submitUserProfile),
    path('UserBio', views.userBio),
    path('SendEmail', views.email),

    path('CreateEvent', views.createEvent),
    path('GetEventRequested', views.requestedEventList),
    path('EditEventByAdmin', views.editEventByAdmin),
    path('EditEventByUser', views.editEventByUser),
    path('LeaveFeedback', views.leaveFeedback),
    path('DisableEvent', views.disableEvent),
    path('Search', views.search),
    path('UserEvent', views.userEvent),
    path('DeleteEvent', views.deleteEvent),
    path('NotVerifiedUserSet', views.notVerifiedUserSet),
    path('VerifyOrRejectUser', views.verifyOrRejectUser),
    path('DonateMoney', views.donate_money),


    # StoreManagement urls:
    path('CreateCategoty', views.create_category),
    path('CreateSubCategoty', views.create_subcategory),
    path('CreateProduct', views.create_product),

    path('CategotyList', views.category_list),
    path('SubCategotyList', views.subcategory_list),
    path('ProductList', views.product_list),

    path('EditCategoty', views.edit_category),
    path('EditSubCategoty', views.edit_subcategory),
    path('EditProduct', views.edit_product),

    path('DeleteCategoty', views.delete_category),
    path('DeleteSubCategoty', views.delete_subcategory),
    path('DeleteProduct', views.delete_product),
]
