from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404, JsonResponse


#url
import requests
from bs4 import BeautifulSoup


from rest_framework import generics
from rest_framework import mixins

#basic auth
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets


# Create your views here.
class PostViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # def list(self, reques):
    #     posts = Post.objects.all()
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)
    
    # def create(self,request):
    #     serializer = PostSerializer(data=request.data)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status =status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
    


class genericAPIView(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field ='id'
    # authentication_classes =[TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request,id):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request,id)
    
    def delete(self, request, id=None):
        return self.destroy(request,id)



class PostsAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
def PostsView(request):
    if request.method == 'GET':
   # url = request.GET.get('https://joatoon26.com/webtoon?page=100')
        response = requests.get('https://fxfx242.com/pt')
        
        arr_movie = []

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            element_class = 'webtoon-list'
            elements = soup.find_all(class_=element_class)[0].find_all('li')
            
            linksD = []
            arrImg = []
            arrGenre = []
            arrDay = []
            arrPlat = []
            
            for element in elements:
                link = element.find('a')['href']
                # img_url = element.find('img')['src']
                # genre = element.find_all('span')[2].text
                # platform = img_url.split('/')[-1].split('.')[0]
                # day = element.find_all('span')[1].text
                
                linksD.append(link)
                # arrImg.append(img_url)
                # arrGenre.append(genre)
                # arrDay.append(day)
                # arrPlat.append(platform)
            
            # for i, link in enumerate(linksD):
            #     response_detail = requests.get(link)
            #     if response_detail.status_code == 200:
            #         soup_detail = BeautifulSoup(response_detail.content, 'html.parser')
                    
            #         title_class = "view-content"
            #         dec_class = "view-content1"
            #         episode_class = "na-subject"
                    
            #         title = soup_detail.find(class_=title_class).find('h1').text
            #         des = soup_detail.find_all(class_=dec_class)[1].text
            #         episode_links = soup_detail.find_all(class_=episode_class)
            #         imgT = arrImg[i]
            #         genre = arrGenre[i]
            #         durate = arrDay[i]
            #         plate = arrPlat[i]
                    
            #         linkspermovie = []
            #         for episode_link in episode_links:
            #             linkspermovie.append(episode_link['href'])
                    
            #         if linkspermovie:
            #             linkspermovie.reverse()
            #             arrayoneMovie = [title, imgT, des, len(linkspermovie), linkspermovie, genre, durate, plate]
            #             arr_movie.append(arrayoneMovie)
        
        return JsonResponse(linksD, safe=False)
# def PostsView(request):
    
#     if request.method == 'GET':
#         url = request.GET.get('https://joatoon26.com/webtoon?page=100')
#         response = request.get(url)
        
#         arr_movie = []

#         if response.status_code == 200:
#             soup = BeautifulSoup(response.content, 'html.parser')
            
#             element_class = 'mx-n2'
#             elements = soup.find_all(class_=element_class)
            
#             linksD = []
#             arrImg = []
#             arrGenre = []
#             arrDay = []
#             arrPlat = []
            
#             for element in elements:
#                 link = element.find('a')['href']
#                 img_url = element.find('img')['src']
#                 genre = element.find_all('span')[2].text
#                 platform = img_url.split('/')[-1].split('.')[0]
#                 day = element.find_all('span')[1].text
                
#                 linksD.append(link)
#                 arrImg.append(img_url)
#                 arrGenre.append(genre)
#                 arrDay.append(day)
#                 arrPlat.append(platform)
            
#             for i, link in enumerate(linksD):
#                 response_detail = request.get(link)
#                 if response_detail.status_code == 200:
#                     soup_detail = BeautifulSoup(response_detail.content, 'html.parser')
                    
#                     title_class = "view-content"
#                     dec_class = "view-content1"
#                     episode_class = "na-subject"
                    
#                     title = soup_detail.find(class_=title_class).find('h1').text
#                     des = soup_detail.find_all(class_=dec_class)[1].text
#                     episode_links = soup_detail.find_all(class_=episode_class)
#                     imgT = arrImg[i]
#                     genre = arrGenre[i]
#                     durate = arrDay[i]
#                     plate = arrPlat[i]
                    
#                     linkspermovie = []
#                     for episode_link in episode_links:
#                         linkspermovie.append(episode_link['href'])
                    
#                     if linkspermovie:
#                         linkspermovie.reverse()
#                         arrayoneMovie = [title, imgT, des, len(linkspermovie), linkspermovie, genre, durate, plate]
#                         arr_movie.append(arrayoneMovie)
        
#         return arr_movie

#         # posts = Post.objects.all()
#         # serializer = PostSerializer(posts, many=True)
#         # return Response(serializer.data)
#     elif request.method =='POST':
    
#         serializer = PostSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status =status.HTTP_201_CREATED)
#         return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)


class postDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serailizer = PostSerializer(post)
        return Response(serailizer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    
@api_view(['GET','PUT','DELETE'])
def detail(request, pk):
    try:
        post =  Post.objects.get(pk=pk)
    except post.DoesNotExitst:
        return Response(status =status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':       
        serializer = PostSerializer(post,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)
     