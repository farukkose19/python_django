from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from .models import Word,Kullanici,Mean
from .serializers import wordsserializer,meanserializer,kullaniciserializer
from django.http import HttpResponse,Http404,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import wordForm,kullaniciForm,meanForm


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# @csrf_exempt
# def wordList(request):
#     """
#     Tüm kod parçacıklarını görüntülemek veya oluşturmak için oluşturulmuş fonksiyondur.
#     """
#     if request.method == 'GET':
#         snippets = Word.objects.all()
#         # many : bir çok işlem ( silme ve ekleme )
#         serializer = WordSerializer(snippets, many=True)
#         # oluşan datayı, JSON olarak response et
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = WordSerializer(data=data)
#         # gelen post'u kontrol et.
#         if serializer.is_valid():
#             # True dönerse, kaydet.
#             serializer.save()
#             # oluşan datayı, JSON olarak response et
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)



@csrf_exempt
def word_detail(request, id):
    """
    Kod parçacıklarını silme ve güncelleme işlemleri yapar.
    Ayrıca 'id' görö görüntüleme işlemide yapmaktadır.
    """
    try:
        # aranan id var mı?
        snippet = Word.objects.all().filter(id=id)
    except Word.DoesNotExist:
        # Yoksa 404 sayfası gönder
        raise Http404("Böyle bir kod numarası bulunamadı!")

    if request.method == 'GET':
        # aranan data var ise, json olarak yolla.
        serializer = wordsserializer(snippet,many=True)
        return Response(serializer.data)

    # elif request.method == 'PUT':
    #     # gelen datayı, Json'a çevir.
    #     data = JSONParser().parse(request)
    #     # Serializer gönder.
    #     serializer = WordSerializer(snippet, data=data)
    #     # gelen data uygun mu ?
    #     if serializer.is_valid():
    #         # True dönerse kaydet.
    #         serializer.save()
    #         return JSONResponse(serializer.data)
    #     return JSONResponse(serializer.errors, status=400)

    # elif request.method == 'DELETE':
    #     # silinmesi gereken id var ise siler yok ise 404 döner
    #     snippet.delete()
    #     raise Http404("Böyle bir kod numarası bulunamadı!")
#http://127.0.0.1:8000/word/2/


#
# @csrf_exempt
# def kullaniciList(request):
#     """
#     Tüm kod parçacıklarını görüntülemek veya oluşturmak için oluşturulmuş fonksiyondur.
#     """
#     if request.method == 'GET':
#         snippets = Kullanici.objects.all()
#         # many : bir çok işlem ( silme ve ekleme )
#         serializer = KullaniciSerializer(snippets,many=True)
#         # oluşan datayı, JSON olarak response et
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = KullaniciSerializer(data=data)
#         # gelen post'u kontrol et.
#         if serializer.is_valid():
#             # True dönerse, kaydet.
#             serializer.save()
#             # oluşan datayı, JSON olarak response et
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)
#



@api_view(['GET', 'POST'])
def wordlist3(request):
    form = wordForm
    if request.method == 'GET':
        # Modeldeki verileri al
        snippets = Word.objects.all()
        # Serializer tarafından tarat
        serializer = wordsserializer(snippets, many=True)
        # Json olarak dönder.
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        #return JsonResponse({'aaaa': 'deneme'})

        data=request.data
        if data:
            top=Word.objects.order_by('-id')[0]
            topid=top.id+1
            form=wordForm(data)
            #id1=form.data['id']
            id1=topid
            name1=form.data['name']
            kullaniciid=form.data['kullanici']
            kullanici1=Kullanici.objects.get(id=kullaniciid)
            p=Word.objects.create(id=id1,name=name1,kullanici=kullanici1)
            id = p.id
            return JsonResponse({'sonuc': 'basarili', 'id': id})
        else:
            return JsonResponse({'sonuc': 'basarisiz'})


@api_view(['GET', 'POST'])
def login(request):
    form = kullaniciForm

    if request.method == 'POST':
        #return JsonResponse({'aaaa': 'deneme'})
        p = Kullanici
        data=request.data
        if data:
            form=kullaniciForm(data)
            username=form.data['userName']
            password1=form.data['password']
            try:
                p=Kullanici.objects.get(password=password1,userName=username)
            except Kullanici.DoesNotExist:
                return JsonResponse({'sonuc': 'kullanıcı bulanamadı, kullanıcı adı veya şifre hatalı!!'})
            id=p.id
            return JsonResponse({'sonuc': 'basarili', 'id': id})
        else:
            return JsonResponse({'sonuc': 'basarisiz'})


@api_view(['GET', 'POST'])
def meanlist(request):
    form = meanForm
    if request.method == 'GET':
        # Modeldeki verileri al
        snippets = Mean.objects.all()
        # Serializer tarafından tarat
        serializer = meanserializer(snippets, many=True)
        # Json olarak dönder.
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        #return JsonResponse({'aaaa': 'deneme'})

        data=request.data
        if data:
            form=meanForm(data)
            top = Mean.objects.order_by('-id')[0]
            topid = top.id + 1
            #id1=form.data['id']
            id1=topid
            meanname1=form.data['meanName']
            wordid1=form.data['word']
            word1=Word.objects.get(id=wordid1)
            p=Mean.objects.create(id=id1,meanName=meanname1,word=word1)
            id=p.id
            return JsonResponse({'sonuc': 'basarili', 'id': id})
        else:
            return JsonResponse({'sonuc': 'basarisiz'})

@api_view(['GET', 'POST'])
def worddelete(request):
    form = wordForm
    if request.method == 'GET':
        # Modeldeki verileri al
        snippets = Word.objects.all()
        # Serializer tarafından tarat
        serializer = wordsserializer(snippets, many=True)
        # Json olarak dönder.
        return Response(serializer.data)
    elif request.method == 'POST':
        data=request.data
        if data:
            form=wordForm(data)
            id1=form.data['id']
            word = Word.objects.get(id=id1)
            word.delete()
            return JsonResponse({'sonuc': 'silindi'})
        else:
            return JsonResponse({'sonuc': 'basarisiz'})

@api_view(['GET', 'POST'])
def wordEdit(request):
    form = wordForm
    if request.method == 'GET':
        snippets = Word.objects.all()
        serializer = wordsserializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        if data:
            form = wordForm(data)
            id1 = form.data['id']
            word = Word.objects.get(id=id1)
            wordname = form.data['name']
            word.name = wordname
            word.save()
            return JsonResponse({'sonuc': 'kelime düzenlendi'})
        else:
            return JsonResponse({'sonuc': 'basarisiz'})



@api_view(['GET', 'POST'])
def kullanici(request):
    form = kullaniciForm
    if request.method == 'GET':
        snippets = Kullanici.objects.all()
        serializer = kullaniciserializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        if data:
            form = kullaniciForm(data)
            top = Kullanici.objects.order_by('-id')[0]
            topid = top.id + 1
            id1=topid
            kullaniciname = form.data['userName']
            password=form.data['password']
            k=Kullanici.objects.create(id=id1,userName=kullaniciname,password=password)
            id=k.id
            return JsonResponse({'sonuc': 'basarili', 'id': id})
        else:
            return JsonResponse({'sonuc': 'basarisiz'})


@api_view(['GET', 'POST'])
def wordsearch(request):
    form = wordForm
    if request.method == 'GET':
        snippets = Word.objects.all()
        serializer = wordsserializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        if data:
            form = wordForm(data)
            name = form.data['name']
            kulid = form.data['kullanici']

            try:
                word = Word.objects.get(name=name, kullanici=kulid)
            except Word.DoesNotExist:
                return JsonResponse({'sonuc': 'kelime bulunamadi'})
            id = word.id
            serializerss = wordsserializer(word)
            return Response(serializerss.data)
        else:
            return JsonResponse({'sonuc': 'basarisiz'})



@api_view(['GET', 'POST'])
def wordgetid(request):
    form = wordForm
    if request.method == 'GET':
        # Modeldeki verileri al
        snippets = Word.objects.all()
        # Serializer tarafından tarat
        serializer = wordsserializer(snippets, many=True)
        # Json olarak dönder.
        return Response(serializer.data)
    elif request.method == 'POST':
        #return JsonResponse({'aaaa': 'deneme'})

        data=request.data
        if data:
            form=wordForm(data)
            id1=form.data['id']
            p=Word.objects.all().filter(id=id1)
            serializer=wordsserializer(p,many=True)
            return Response(serializer.data)
        else:
            return JsonResponse({'sonuc': 'basarisiz'})



@api_view(['GET', 'POST'])
def meangetid(request):
    form = meanForm
    if request.method == 'GET':
        # Modeldeki verileri al
        snippets = Mean.objects.all()
        # Serializer tarafından tarat
        serializer = meanserializer(snippets, many=True)
        # Json olarak dönder.
        return Response(serializer.data)
    elif request.method == 'POST':
        #return JsonResponse({'aaaa': 'deneme'})

        data=request.data
        if data:
            form=meanForm(data)
            id1=form.data['id']
            p=Mean.objects.all().filter(id=id1)
            serializer=meanserializer(p,many=True)
            return Response(serializer.data)
        else:
            return JsonResponse({'sonuc': 'basarisiz'})



@api_view(['GET', 'POST'])
def meansil(request):
    form = meanForm
    if request.method == 'GET':
        # Modeldeki verileri al
        snippets = Mean.objects.all()
        # Serializer tarafından tarat
        serializer = meanserializer(snippets, many=True)
        # Json olarak dönder.
        return Response(serializer.data)
    elif request.method == 'POST':
        #return JsonResponse({'aaaa': 'deneme'})

        data=request.data
        if data:
            form=meanForm(data)
            id1=form.data['id']
            p=Mean.objects.all().filter(id=id1)
            p.delete()
            return JsonResponse({'sonuc': 'basarili'})
        else:
            return JsonResponse({'sonuc': 'basarisiz'})


@api_view(['GET', 'POST'])
def meanedit(request):
    form = meanForm
    if request.method == 'GET':
        # Modeldeki verileri al
        snippets = Mean.objects.all()
        # Serializer tarafından tarat
        serializer = meanserializer(snippets, many=True)
        # Json olarak dönder.
        return Response(serializer.data)
    elif request.method == 'POST':
        #return JsonResponse({'aaaa': 'deneme'})

        data=request.data
        if data:
            form=meanForm(data)
            id1=form.data['id']
            meanname=form.data['meanName']
            p=Mean.objects.get(id=id1)
            p.meanName=meanname
            p.save()
            return JsonResponse({'sonuc': 'basarili'})
        else:
            return JsonResponse({'sonuc': 'basarisiz'})


@api_view(['GET', 'POST'])
def wordgetuserid(request):
    form = wordForm
    if request.method == 'GET':
        # Modeldeki verileri al
        snippets = Word.objects.all()
        # Serializer tarafından tarat
        serializer = wordsserializer(snippets, many=True)
        # Json olarak dönder.
        return Response(serializer.data)
    elif request.method == 'POST':
        #return JsonResponse({'aaaa': 'deneme'})

        data=request.data
        if data:
            form=wordForm(data)
            kulid=form.data['kullanici']
            p=Word.objects.all().filter(kullanici=kulid)
            serializer=wordsserializer(p,many=True)
            return Response(serializer.data)
        else:
            return JsonResponse({'sonuc': 'basarisiz'})