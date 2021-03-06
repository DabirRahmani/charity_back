from django.urls import path
from . import views

doing_urls = [
    path('UploadImage', views.ImageView.as_view(), name='upload_image'),
    path('Invite', views.invite),
]

auth_urls = [
    path('login', views.login),
    path('signup', views.signup),
    path('logout', views.logout),
    path('ForgotPassword', views.forgotPassword),
    path('LoadUserProfile', views.loadUserProfile),
    path('SubmitUserProfile', views.submitUserProfile),
    path('EditProfileImage', views.editProfileImage),
    path('UserBio', views.userBio),
    path('SendEmail', views.email),
    path('NotVerifiedUserSet', views.notVerifiedUserSet),
    path('VerifiedDonatorSet', views.verifiedDonatorSet),
    path('AdminSet', views.adminSet),
    path('VerifyOrRejectUser', views.verifyOrRejectUser),
]

event_urls = [
    path('CreateEvent', views.createEvent),
    path('GetEventRequested', views.requestedEventList),
    path('EditEventByAdmin', views.editEventByAdmin),
    path('EditEventByUser', views.editEventByUser),
    path('LeaveFeedback', views.leaveFeedback),
    path('DisableEvent', views.disableEvent),
    path('Search', views.searchEvent),
    path('UserEvent', views.userEvent),
    path('DeleteEvent', views.deleteEvent),
    path('DonateMoney', views.donateMoneyEvent),
    path('EditEventImage', views.editEventImage),
]

donate_urls = [
    path('GeneralDonate', views.generalDonate),
    path('PendingDonate', views.pendingDonates),
    path('Delivery', views.delivery),
]

transaction_urls = [
    path('TransactionList', views.transactionList),
    path('RecentTransactionList', views.recentTransactionList),
    path('BiggestTransactionList', views.biggestTransactionList),
]

store_management_urls = [
    path('CreateCategory', views.create_category),
    path('CreateSubCategory', views.create_subcategory),
    path('CreateProduct', views.create_product),
    path('CategoryList', views.category_list),
    path('SubCategoryList', views.subcategory_list),
    path('ProductList', views.product_list),
    path('EditCategory', views.edit_category),
    path('EditSubCategory', views.edit_subcategory),
    path('EditProduct', views.edit_product),
    path('DeleteCategory', views.delete_category),
    path('DeleteSubCategory', views.delete_subcategory),
    path('DeleteProduct', views.delete_product),
    path('TheCategory', views.the_category),
    path('TheSubCategory', views.the_subcategory),
    path('TheProduct', views.the_product),

    path('DataAnalyze', views.dataAnalyze)
]

needRequest_urls = [
    path('CreateNeedRequest', views.createNeedRequest),
    path('RequestedNeedRequestList', views.requestedNeedRequestList),
    path('MyNeedRequestList', views.myNeedRequestList),
    path('AcceeptOrRejectNeedRequest', views.acceptOrRejectNeedRequest),
    path('AcceptedNeedRequestList', views.acceptedNeedRequestList),
    path('AllNeedRequestList', views.allNeedRequestList),
]

admin_management_urls = [
    path('PromoteToSuperAdmin', views.promoteToSuperAdmin),
    path('PromoteToAdmin', views.promoteToAdmin),
    path('DemoteAdmin', views.demoteAdmin),
]

pack_list = [
    doing_urls,
    auth_urls,
    event_urls,
    donate_urls,
    transaction_urls,
    store_management_urls,
    needRequest_urls,
    admin_management_urls
]

urlpatterns = []
for pack in pack_list:
    for url in pack:
        urlpatterns.append(url)
