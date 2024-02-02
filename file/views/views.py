from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, DeleteView
from rest_framework.generics import ListAPIView, get_object_or_404

from file.form import FileUploadForm
from file.models import File
from file.serializers import FileSerializer


def home(request: HttpRequest) -> HttpResponse:
    """
    Домашняя страница
    :param request: {method},
    :return: HttpResponse
    """
    all_files = File.objects.all()
    form = FileUploadForm(request.POST or None, request.FILES or None)

    context = {
        'object_list': all_files,
        'form': form,
    }

    if request.POST:
        File.objects.create(
            name=request.FILES.get('file')._name.split('.')[0],
            file=request.FILES.get('file')
        )

        return HttpResponseRedirect(reverse('file:home'))

    return render(
        request,
        template_name='file/home.html',
        context=context,
    )


class FileListView(ListView):
    model = File
    serializer_class = FileSerializer


@method_decorator(csrf_exempt, name='dispatch')
class DownloadFileView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        file_obj = get_object_or_404(File, pk=kwargs.get('pk'))
        file_content = file_obj.file.read()
        response = HttpResponse(file_content, content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename={file_obj.name}'
        return response


class FileDetailView(DetailView):
    model = File
    serializer_class = FileSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset


class FileDeleteView(DeleteView):
    model = File
    template_name = 'file/file_delete_confirm.html'
    success_url = reverse_lazy('file:all_files')
