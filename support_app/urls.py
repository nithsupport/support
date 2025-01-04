
from django.urls import path, re_path
from . import views
from .image_access_download import download_image, download_all_images

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_us, name='contact_us'),
    
    path('NAFJKO8sHTQ5AXPcVBNmEWyUZSA/', views.hn_campus_call_back, name='hn_campus_call_back'),
    path('PQW2ASDfGHCVn6LQAZbMOEF9rUT/', views.ec_campus_call_back, name='ec_campus_call_back'),
    path('ODA1LTMyZDQtNDk4Yy05MTI1LTV/', views.rr_campus_call_back, name='rr_campus_call_back'),
      
    path('searching/', views.category, name='category-search'),
    
    path('request/', views.request_a_call_back, name='request-a-call-back'),
    
    path('upload-jee-main-1-details/', views.jee_main1_form, name='jee-main1-form'),
    path('jee-main1-list/', views.view_jee_main1, name='jee-main1-list'),
    path('delete/jee-main1/<int:pk>/', views.delete_jee_main1, name='delete-jee-main1'),
    path('download/jee-main1/', views.download_jee_main1, name='download-jee-main1'),
    path('download/upload-jee-main-1/<int:pk>/image/<str:model_name>/', download_image, name='download-upload-jee-main-1-image'),
    
    path('upload-2-jee-main-details/', views.jee_main2_form, name='jee-main2-form'),
    path('jee-main2-list/', views.view_jee_main2, name='jee-main2-list'),
    path('delete/jee-main2/<int:pk>/', views.delete_jee_main2, name='delete-jee-main2'),
    path('download/jee-main2/', views.download_jee_main2, name='download-jee-main2'),
    path('download/upload-2-jee-main/<int:pk>/image/<str:model_name>/', download_image, name='download-upload-2-jee-main-image'),
    
    path('upload-comed-k-details/', views.comedk_form, name='comedk-ranking-form'),
    path('comed-k-ranking-list/', views.view_comedk, name='comedk-ranking-list'),
    path('delete/comed-k-ranking/<int:pk>/', views.delete_comedk, name='delete-comedk-ranking'),
    path('download/comed-k-ranking/', views.download_comedk, name='download-comedk-ranking'),
    path('download/upload-comed-k/<int:pk>/image/<str:model_name>/', download_image, name='download-upload-comed-k-image'),
    
    path('upload-cet-ranking/', views.cet_ranking_form, name='cet-ranking-form'),
    path('cet-ranking-list/', views.view_cet_ranking, name='cet-ranking-list'),
    path('delete/cet-ranking/<int:pk>/', views.delete_cet_ranking, name='delete-cet-ranking'),
    path('download/cet-ranking/', views.download_cet_ranking, name='download-cet-ranking'),
    # path('cet-ranking/all-download/', views.download_all_cet_ranking, name='download-all-cet-ranking'),
    
    path('class12marks/', views.puc_marks_upload_form, name='puc-marks-upload-form'),
    path('class12marks-list/', views.view_puc_marks_upload, name='puc-marks-upload-list'),
    path('delete/class12marks/<int:pk>/', views.delete_puc_marks_upload, name='delete-puc-marks-upload'),
    path('download/class12marks/xls', views.download_puc_marks_upload, name='download-puc-marks-upload'),
    path('download/class12marks/<int:pk>/image/<str:model_name>/', download_image, name='download-class12marks-image'),
    
    path('download/all-images/<str:model_name>/', download_all_images, name='download-all-images'),
    
    path('add/faq/', views.faq_form, name='add-faq'),
    path('faq-list/', views.view_faq, name='faq-list'),
    path('edit/faq/<int:pk>/', views.edit_faq, name='edit-faq'),
    path('delete/faq/<int:pk>/', views.delete_faq, name='delete-faq'),
    
    path('add/<str:model_name>/faq/', views.all_faq_form, name='add-all-faq'),
    path('<str:model_name>/faq-list/', views.view_all_faq, name='selected-faq-list'),
    path('edit/<str:model_name>/faq/<int:pk>/', views.edit_all_faq, name='edit-selected-faq'),
    path('delete/<str:model_name>/faq/<int:pk>/', views.delete_selected_faq, name='delete-selected-faq'),
    
    path('daily-report/', views.add_daily_report, name='add-daily-report'),
    path('daily-report-list/<str:username>/', views.view_daily_report, name='daily-report-list'),
    path('all-daily-report-list/', views.view_all_daily_report, name='all-daily-report-list'),
    path('edit/daily-report/<int:pk>/', views.edit_daily_report, name='edit-daily-report'),
    path('delete/daily-report/<int:pk>/', views.delete_daily_report, name='delete-daily-report'),
    path('daily-report/download/', views.download_daily_report, name='download-daily-report'),
    
    path('grievance/', views.grievance_form, name='grievance-form'),
    path('grievance-list/', views.view_grievance, name='grievance-list'),
    path('delete/grievance/<int:pk>/', views.delete_grievance, name='delete-grievance'),
    path('grievance/download/', views.download_grievance, name='download-grievance'),
    
    path('amaatra/', views.amaatra_form, name='amaatra-form'),
    path('amaatra-list/', views.view_amaatra, name='amaatra-list'),
    path('delete/amaatra/<int:pk>/', views.delete_amaatra, name='delete-amaatra'),
    path('amaatra/download/', views.download_amaatra, name='download-amaatra'),
    
    path('ssm/', views.ssm_form, name='ssm-form'),
    path('ssm-list/', views.view_ssm, name='ssm-list'),
    path('delete/ssm/<int:pk>/', views.delete_ssm, name='delete-ssm'),
    path('ssm/download/', views.download_ssm, name='download-ssm'),
    
    path('ectransportation/', views.ec_transportation_form, name='ec-transportation-form'),
    path('ec-transportation-list/', views.view_ec_transportation, name='ec-transportation-list'),
    path('delete/ec-transportation/<int:pk>/', views.delete_ec_transportation, name='delete-ec-transportation'),
    path('ec-transportation/download/', views.download_ec_transportation, name='download-ec-transportation'),
    path('download/ectransportation/<int:pk>/image/<str:model_name>/', download_image, name='download-ectransportation-image'),
    
    path('rrtransportation/', views.rr_transportation_form, name='rr-transportation-form'),
    path('rr-transportation-list/', views.view_rr_transportation, name='rr-transportation-list'),
    path('delete/rr-transportation/<int:pk>/', views.delete_rr_transportation, name='delete-rr-transportation'),
    path('rr-transportation/download/', views.download_rr_transportation, name='download-rr-transportation'),
    path('download/rrtransportation/<int:pk>/image/<str:model_name>/', download_image, name='download-rrtransportation-image'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    
    
    #login and logout page
    path('login/', views.loginpage, name='login-page'),
    path('logout/', views.logoutpage, name='logout-page'),
    
    path('group/create/', views.add_group_permissions, name='create-group-permissions'),
    path('group/edit/<int:group_id>/', views.edit_group_permissions, name='edit-group-permissions'),
    
    path('user/create/', views.create_admin_user, name='create-admin-user'),
    path('user/edit/<str:username>/', views.edit_admin_user, name='edit-admin-user'),
    
    path('profile/<str:username>/', views.profile, name='user-profile'),

    path('user/change-password/', views.PasswordsChangeView.as_view(template_name='login_users/change_password.html'), name='change-password-form'),
    path('user/changing/password/', views.change_password, name='change-password-form'),
    path('user/<int:user_id>/change-password/', views.admin_changing_users_passwords, name='admin-change-password-form'),
    
    # path('category/<str:category_name>/', views.category, name='category'),
    path('pesu/<str:category_name>/', views.category, name='category'),
    # path('amaatra/<str:category_name>/', views.amaatra_category, name='amaatra_category'),
    path('<str:model_name>/category/<str:category_name>/', views.selected_category, name='selected_category'),
    path('error/404/', views.error_404_view, name='404-error'),
    path('user/access-denied-page/', views.access_denied_page, name='access-denied-page')
    
]