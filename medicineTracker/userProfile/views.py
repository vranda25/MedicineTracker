from django.shortcuts import render
from .models import *
from .serializer import *
from accounts.models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


# Create your views here.

class ProfileView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        queryset = Profile.objects.filter(user=user)
        serialize = ProfileSerializer(queryset, many=True)
        return Response({
            'data': serialize.data
        })

    def post(self, request):
        try:
            user = {'user': request.user.id}
            data = request.data
            data = {**data, **user}
            serializer = ProfileSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Your Profile has been updated successfully!',
                    'data': serializer.data,
                })
            return Response({
                'status': '400',
                'message': 'Something went wrong:(',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': '400',
                'message': 'Something went wrong:(',
                'data': {}
            })

    def put(self, request):
        try:
            user = request.user.id
            profile = Profile.objects.get(user__id=user)
            print(profile)

            if profile:
                data = request.data
                data = {**data, **{'user': user}}
                serializer = ProfileSerializer(profile, data)
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'status': 200,
                        'message': 'Your Profile has been updated successfully!',
                        'data': serializer.data,
                    })
                return Response({
                    'status': 400,
                    'message': 'Something went wrong :(',
                    'data': serializer.errors,
                })
        except Exception as e:
            print(e)
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': {},
            })


    # def delete(self, request):
    #     try:
    #         user = request.user.id
    #         profile = Profile.objects.get(user__id=user)
    #         profile.delete()
    #         return Response({
    #             'status': 200,
    #             'message': 'Your Profile has been deleted successfully!',
    #             'data': {},
    #         })
    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             'status': 400,
    #             'message': 'Something went wrong',
    #             'data': {},
    #         })


class AllergiesView(APIView):
    def post(self, request):
        try:
            user = {'user': request.user.id}
            data = request.data
            data = {**data, **user}
            serializer = AllergiesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Your Allergies has been updated successfully!',
                    'data': serializer.data,
                })
            return Response({
                'status': '400',
                'message': 'Something went wrong:(',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status' : 400,
                'message': 'Something went wrong',
                'data': {},
            })

    # def delete(self,request):



class HistoryView(APIView):
    def post(self, request):
        try:
            user = {'user': request.user.id}
            data = request.data
            data = {**data, **user}
            serializer = HistorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Your History has been updated successfully!',
                    'data': serializer.data,
                })
            return Response({
                'status': '400',
                'message': 'Something went wrong:(',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status' : 400,
                'message': 'Something went wrong',
                'data': {},
            })







