from rest_framework.response import Response
from rest_framework.views import APIView
from Verification import verify
import phonenumbers


class SendVerificationCode(APIView):

    def post(self, request):

        phone = request.data['phone']

        if phonenumbers.is_possible_number(phonenumbers.parse(phone)):

            if verify.send(phone):
                return Response({'status': True})
            else:
                return Response({'status': False})

        else:
            return Response({'status': False})


class CheckVerificationCode(APIView):

    def post(self, request):

        phone = request.data['phone']
        code = request.data['code']

        if verify.check(phone, code):
            return Response({'status': True})
        else:
            return Response({'status': False})

