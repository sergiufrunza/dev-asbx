from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


class SendEmailAPI(APIView):

    def post(self, request):
        if request.headers.get('Token'):
            pass
        data = request.data
        email_template_name = 'SendEmail/templateEmail.html'
        subject = fr"Lead from ASBX.ORG & Flint Cooper {data['disease']} Calculator - {data['phone']}"
        msg_html = render_to_string(email_template_name, data)
        send_mail(subject=subject,message="", html_message=msg_html, from_email=settings.EMAIL_HOST_USER, recipient_list=['sergiu.frunza120@gmail.com'])
        return Response({
                "status": True,
            })


class SendEmailDocuSignAPI(APIView):

    def post(self, request):
        if request.headers.get('Token'):
            pass
        data = request.data
        email_template_name = 'SendEmail/templateEmailDocuSign.html'

        subject = fr"Request DocuSign for {data['phone']} Lead"
        msg_html = render_to_string(email_template_name, data)
        send_mail(subject=subject,message="", html_message=msg_html, from_email=settings.EMAIL_HOST_USER, recipient_list=['sergiu.frunza120@gmail.com', 'aurel@7lex.com', 'joe@7lex.com', '75fs1wg4@robot.zapier.com'])
        return Response({
                "status": True,
            })





