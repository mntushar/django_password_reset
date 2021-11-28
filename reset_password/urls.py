from django.urls import path
import reset_password as view

app_name = "reset"

urlpatterns = [
    path('confirm/', view.MyPasswordResetView.as_view(), name='reset_confirm'),
    path('success/', view.MyPasswordResetDoneView.as_view(),name='reset_success'),
    path('reset/<uidb64>/<token>', view.MyPasswordResetConfirmView.as_view(),name='password_reset'),
    path('reset_confirm/', view.MyPasswordResetCompleteView.as_view(),name='reset_confirm'),
]
