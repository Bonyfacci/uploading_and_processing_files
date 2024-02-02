import os

from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from file.models import File
from file.views.views import DownloadFileView, home

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(TEST_DIR, 'data')


class FileTestCase(APITestCase):
    """
    Для тестирования файлов (File)
    """

    def setUp(self):
        self.file = File.objects.create(
            name='test',
            file="test_file.txt"
        )

    def get_file(self):

        response = self.client.get(
            reverse('file:all_files')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            File.objects.all().count(),
            1
        )

    def get_files(self):

        response = self.client.get(
            reverse('file:all-files')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            File.objects.all().count(),
            1
        )


# class FileViewsTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(username='test_user', password='test_password')
#         self.file = File.objects.create(name='Test_File', file='path/to/testfile.txt')
#
#     def test_home_view(self):
#         url = reverse('file:home')
#         request = self.factory.get(url)
#         response = home(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Home Page')
#
#     def test_download_file_view(self):
#         url = reverse('file:file_download', args=[self.file.pk])
#         request = self.factory.get(url)
#         response = DownloadFileView.as_view()(request, pk=self.file.pk)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response['Content-Disposition'], 'attachment; filename=Test File')

