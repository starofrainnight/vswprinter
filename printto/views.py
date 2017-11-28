import os
from django.views.generic import TemplateView, FormView
from . import APP_NAME, get_template_name
from .forms import UploadedFileForm


class IndexView(FormView):
    form_class = UploadedFileForm
    # Replace with your template.
    template_name = get_template_name('index.html')
    # Replace with your URL or reverse().
    success_url = '/%s/successed' % APP_NAME

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.save()

            model = form.instance

            print("Printing : %s" % model.file.path)

            os.system(".\\SumatraPDF.exe -print-to-default \"%s\"" %
                      model.file.path)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class UploadSuccessedView(TemplateView):
    template_name = get_template_name("upload_successed.html")
