from django.shortcuts import render, redirect
from .forms import AddFeatureForm,AddLabelForm
from django.views.generic import FormView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FeatureSerializer, LabelSerializer
from .models import Label, Feature
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.db import IntegrityError


@csrf_exempt
def add_feature(request):
    if request.method == 'POST':
        feature = request.POST.get('feature')
        label = request.POST.get('label')
        try:
            label_obj = Label.objects.get(name=label)
            Feature.objects.create(name=feature, label=label_obj)
            return render(request, 'add_feature.html', {'message': 'Feature added successfully'})
        except Label.DoesNotExist:
            return render(request, 'add_feature.html', {'message': 'The label does not exist.'})
    else:
        return render(request, 'add_feature.html')

@csrf_exempt
def add_label(request):
    if request.method == 'POST':
        label = request.POST.get('label')
        try:
            Label.objects.create(name=label)
            return render(request, 'add_label.html', {'message': 'Label added successfully'})
        except IntegrityError as e:
            return render(request, 'add_label.html', {'message': 'This label already exists'})
    else:
        return render(request, 'add_label.html')

@api_view(['GET'])
def get_features(request):
    features = Feature.objects.all()
    serializer = FeatureSerializer(features, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_labels(request):
    labels = Label.objects.all()
    serializer = LabelSerializer(labels, many=True)
    return Response(serializer.data)




class AddFeatureView(FormView):
    form_class = AddFeatureForm
    template_name = 'add_feature.html'

    def form_valid(self, form):
        feature = form.cleaned_data['feature']
        label = form.cleaned_data['label']
        Feature.objects.create(name=feature, label=label)
        return redirect('features')


class AddLabelView(FormView):
    form_class = AddLabelForm
    template_name = 'add_label.html'

    def form_valid(self, form):
        label = form.cleaned_data['label']
        Label.objects.create(name=label)
        return redirect('labels')
    

class LabelCreateAPIView(GenericAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()




class FeatureCreateAPIView(GenericAPIView):
    serializer_class = FeatureSerializer
    queryset = Feature.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
