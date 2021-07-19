from contacts.models.contact_model import Contacts
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework import status
from utils.contact_utils import Util


class ContactApiView(APIView):
    def post(self, request, format=None):
        data = self.request.data

        try:
            send_mail(
                 data['subject'],
                 'Name: '
                + data['name']
                + '\Email: '
                + data['email']
                + '\n\nMessage:\n'
                + data['message'],
                 'bizname1990@gmail.com',
                ['bizname1990@gmail.com'],
                fail_silently=False
            )

            contacts = Contacts(
                name = data['name'],
                email = data['email'],
                subject = data['subject'],
                message = data['message']
            )

            contacts.save()
            return Response({'success': 'Message sent successfully'}, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Failed to send your email, contact the administrator'}, status=status.HTTP_400_BAD_REQUEST)