from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import pandas as pd
import os
import seaborn as sns
sns.set(rc={'figure.figsize':(10,10)})
import io
import matplotlib.pyplot as plt
from analytics import settings
from dashboard.forms import queryForm
from dashboard.analysis import getData
def processReq(request):
    var1 = ""
    var2 = ""
    warning=""
    if request.method == "POST":
        myform = queryForm(request.POST)
        if myform.is_valid():
            data = myform.cleaned_data
            var1 = data['var1']
            var2 = data['var2']
            return MovieAnalytics.getReqType(request,var1,var2)
        else:
            warning = "Irrelevant Data was received"
            return  render (request,'dashboard/index2.html', {"var1":var1,"var2":var2,'warning':warning})
    else:
        myform = queryForm()
    return render (request,'dashboard/index2.html', {"var1":var1,"var2":var2,'warning':warning})
# Create your views here.
def hi(request):
    return MovieAnalytics.getRuntimevsGross(request)

def hello(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    requ = True
    preset_form = queryForm()
    return render(request, "dashboard/index.html", {'preset_form':preset_form,'req':requ})
class MovieAnalytics(TemplateView):
    def getReqType(request,var1,var2):
        if (var1 == 'cr' and var2 == 'pr') or (var1=='pr' and var2=='cr'):
            #CriticRating vs PublicRating Done
            return MovieAnalytics.getPublicRatingVsCriticRating(request)
        elif (var1=='m' and var2=='pr') or (var1=='pr' and var2=='m'):
            #MoviesWithTopPublicRatings Done
            return MovieAnalytics.getTopMoviesPublicRating(request)
        elif (var1=='m' and var2=='cr') or (var1=='cr' and var2 =='m'):
            #MoviesWithTopCriticRatings Done
            return MovieAnalytics.getTopMoviesCriticRating(request)
        elif (var1=='m' and var2=='gross') or (var1=='gross' and var2=='m'):
            #MovieWithHighestGross
            return MovieAnalytics.getTopMoviesGross(request)
        elif (var1=='m' and var2=='runtime') or (var1 =='runtime' and var2=='m'):
            #MovieWithHighRuntime
            return MovieAnalytics.getTopMoviesRuntime(request)
        elif (var1=='runtime' and var2=='gross')or (var2=='runtime' and var1=='gross') :
            #MovieWithHighestGross
            return MovieAnalytics.getRuntimevsGross(request)
        elif (var1=='m' and var2=='year')or (var1=='year' and var2=='m') :
            #MovieWithHighestGross
            return MovieAnalytics.getCountMoviesYear(request)
        elif (var1=='m' and var2=='g')or (var1=='g' and var2=='m') :
            #MovieWithHighestGross
            return MovieAnalytics.getCountGenre(request)
        elif (var1=='pr' and var2=='g')or (var1=='g' and var2=='pr') :
            #MovieWithHighestGross
            return MovieAnalytics.getPublicRatingGenre(request)
        elif var1 == var2:
            warning = "Exception : Can't compare same fields"
            return render (request,'dashboard/index2.html',{"warning":warning})

        else:
            print ("Lets See")
        return render (request,'dashboard/index2.html', {"var1":var1,"var2":var2})
    def getTopMoviesCriticRating(request):
        df = getData()
        topMovies = df.nlargest(15,['CriticRating'])
        gr = sns.barplot(y='MovieName',x='CriticRating', data=topMovies)
        gr.set_yticklabels(gr.get_yticklabels(), fontsize=7)
        mediapath = settings.MEDIA_ROOT
        figure = gr.get_figure()
        figure.savefig(mediapath + "/chart1.png")
        plt.clf()
        return render(request, "dashboard/index.html", {"PATH":settings.MEDIA_URL})
    def getTopMoviesPublicRating(request):
        df = getData()
        topMovies = df.nlargest(15,['PublicRating'])
        br = sns.barplot(y='MovieName',x='PublicRating', data=topMovies)
        br.set_yticklabels(br.get_yticklabels(), fontsize=7)
        mediapath = settings.MEDIA_ROOT
        figure = br.get_figure()
        figure.savefig(mediapath + "/chart1.png")
        return render(request, "dashboard/index.html", {"PATH":settings.MEDIA_URL})
    def getRuntimevsGross(request):
        df = getData()
        data = df.loc[df.GrossMillions>0]
        data = data.loc[data.PublicRating > 0]
        gr= sns.jointplot(data=data, x='PublicRating', y='Runtime')
        buf = io.BytesIO()
        mediapath = settings.MEDIA_ROOT
        gr.savefig(mediapath + "/chart1.png")
        plt.clf()
        factlist = [1,2,3,4,5]
        return render(request, "dashboard/index.html", {"PATH":settings.MEDIA_URL,"factlist":factlist})
    def getPublicRatingVsCriticRating(request):
        df = getData()
        data = df.loc[df['CriticRating']>-1]
        data = data.loc[df['PublicRating']>0]
        gr= sns.jointplot(data=data, x='PublicRating', y='CriticRating')
        mediapath = settings.MEDIA_ROOT
        gr.savefig(mediapath + "/chart1.png")
        factlist = [1,2,3,4,5]
        plt.clf()
        return render(request, "dashboard/index.html", {"PATH":settings.MEDIA_URL,"factlist":factlist})
    def getTopMoviesGross(request):
        df = getData()
        topMovies = df.nlargest(15,['GrossMillions'])
        gr = sns.barplot(y='MovieName',x='GrossMillions', data=topMovies)
        gr.set_yticklabels(gr.get_yticklabels(), fontsize=7)
        mediapath = settings.MEDIA_ROOT
        figure = gr.get_figure()
        figure.savefig(mediapath + "/chart1.png")
        plt.clf()
        return render(request, "dashboard/index.html", {"PATH":settings.MEDIA_URL})
    def getTopMoviesRuntime(request):
        df = getData()
        df = df.loc[df['Runtime']>0]
        topMovies = df.nlargest(15,['Runtime'])
        gr = sns.barplot(y='MovieName',x='Runtime', data=topMovies)
        gr.set_yticklabels(gr.get_yticklabels(), fontsize=7)
        mediapath = settings.MEDIA_ROOT
        figure = gr.get_figure()
        figure.savefig(mediapath + "/chart1.png")
        plt.clf()
        return render(request, "dashboard/index.html", {"PATH":settings.MEDIA_URL})
    def getCountMoviesYear(request):
        df = getData()
        df = df.loc[df['PublicRating']>0]
        df = df.loc[df['CriticRating']>0]
        gr = sns.countplot(y='Year',data=df)
        gr.set_yticklabels(gr.get_yticklabels(), fontsize=7)
        gr.set_title("Number of Movies that were rated by critics and public")
        mediapath = settings.MEDIA_ROOT
        figure = gr.get_figure()
        figure.savefig(mediapath + "/chart1.png")
        plt.clf()
        return render(request, "dashboard/index.html", {"PATH":settings.MEDIA_URL})
    def getCountGenre(request):
        df = getData()
        df = df.loc[df['PublicRating']>0]
        df = df.loc[df['CriticRating']>0]
        gr = sns.countplot(y='Genre',data=df)
        gr.set_yticklabels(gr.get_yticklabels(), fontsize=7)
        gr.set_title("Number of Movies of a Genre that were rated by critics and public")
        mediapath = settings.MEDIA_ROOT
        figure = gr.get_figure()
        figure.savefig(mediapath + "/chart1.png")
        plt.clf()
        return render(request, "dashboard/index.html", {"PATH":settings.MEDIA_URL})
    def getPublicRatingGenre(request):
        df = getData()
        df = df.groupby('Genre').mean()
        df = df.nlargest(10,'PublicRating')
        return render(request, "dashboard/index.html", {"PATH":settings.MEDIA_URL})
