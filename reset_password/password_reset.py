from django.views import View
from django.urls import reverse
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView,  PasswordResetConfirmView, PasswordResetCompleteView

from reset_password.password_reset_form import PasswordResetForm, AccountSetPasswordForm


class MyContaxt(View):
    def common_data(self):
        context = {}
        return context


class MyPasswordResetView(MyContaxt, PasswordResetView):
    template_name = 'password_reset.html'
    form_class = PasswordResetForm

    def get_context_data(self, **kwargs):
        context = self.common_data()
        context['title'] = 'Password Reset'
        super_context = super().get_context_data(**kwargs)
        context.update(super_context)

        return context

    def get_success_url(self):
        success_url = reverse('reset:reset_success')
        return success_url


class MyPasswordResetDoneView(MyContaxt, PasswordResetDoneView):
    template_name = 'password_reset.html'

    def get_context_data(self, **kwargs):
        context = self.common_data()
        context['sent_title'] = 'Password reset mail sent'
        context['sent'] = 'True'
        super_context = super().get_context_data(**kwargs)
        context.update(super_context)

        return context


class MyPasswordResetConfirmView(MyContaxt, PasswordResetConfirmView):
    template_name = 'password_reset.html'
    form_class = AccountSetPasswordForm

    def get_context_data(self, **kwargs):
        context = self.common_contexts()
        context['title'] = 'Enter your new password'
        context['Reset_new_password'] = True

        super_context = super().get_context_data(**kwargs)
        context.update(super_context)

        return context

    def get_success_url(self):
        success_url = reverse('reset:reset_confirm')
        return success_url


class MyPasswordResetCompleteView(MyContaxt, PasswordResetCompleteView):
    template_name = 'password_reset.html'

    def get_context_data(self, **kwargs):
        context = self.common_contexts()
        context['title'] = 'Password reset successful'
        context['reset_confirm'] = True

        super_context = super().get_context_data(**kwargs)
        context.update(super_context)

        return context
