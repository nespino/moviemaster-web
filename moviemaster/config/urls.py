"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

from web.models import Person, Alias, Movie

# Serializers define the API representation.
class AliasSerializer(serializers.ModelSerializer):
    person = serializers.StringRelatedField()
    class Meta:
        model = Alias
        fields = ['alias', 'person']

class PersonSerializer(serializers.ModelSerializer):
    aliases = serializers.StringRelatedField(many=True)
    movies_as_cast = serializers.StringRelatedField(many=True)
    movies_as_director = serializers.StringRelatedField(many=True)
    movies_as_producer = serializers.StringRelatedField(many=True)
    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'aliases', 'movies_as_cast', 'movies_as_director', 'movies_as_producer']


class MoviePersonSerializer(serializers.ModelSerializer):
    aliases = serializers.StringRelatedField(many=True)
    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'aliases']


class MovieSerializer(serializers.ModelSerializer):
    casting = MoviePersonSerializer(read_only=True, many=True)
    directors = MoviePersonSerializer(read_only=True, many=True)
    producers = MoviePersonSerializer(read_only=True, many=True)
    roman_release_year = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['title', 'roman_release_year', 'casting', 'directors', 'producers']

    def int_to_roman(self, input):
        """ Convert an integer to a Roman numeral. """

        if not isinstance(input, type(1)):
            raise (TypeError, "expected integer, got %s" % type(input))
        if not 0 < input < 4000:
            raise (ValueError, "Argument must be between 1 and 3999")
        ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        result = []
        for i in range(len(ints)):
            count = int(input / ints[i])
            result.append(nums[i] * count)
            input -= ints[i] * count
        return ''.join(result)

    def get_roman_release_year(self, movie):
        return self.int_to_roman(movie.release_year)

# ViewSets define the view behavior.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class AliasViewSet(viewsets.ModelViewSet):
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'aliases', AliasViewSet)
router.register(r'movies', MovieViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
