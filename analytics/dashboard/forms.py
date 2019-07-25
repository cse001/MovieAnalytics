from django import forms


class queryForm(forms.Form):
    queryChoices = [('m','MovieName'),('pr','PublicRating'),('cr','CriticRating'),('g','Genre'),('runtime','Runtime'),('year','Year'),('gross','Gross')]
    var1 = forms.ChoiceField(choices=queryChoices)
    var2 = forms.ChoiceField(choices=queryChoices)

#The Plots in the Post
# sns.jointplot(data=dataMoviesFull, x='criticRating', y='audienceRating')
# sns.jointplot(data=dataMoviesFull, x='criticRating', y='audienceRating', kind='hex')
# sns.jointplot(data=dataMoviesFull, y='audienceRating', x='timeMin')
# sns.jointplot(data=dataMoviesFull, y='criticRating', x='timeMin')
# sns.jointplot(data=dataMoviesFull, y='grossMillions', x='audienceRating')
# sns.jointplot(data=dataMoviesFull, x='criticRating', y='grossMillions')
# sns.jointplot(data=dataMoviesFull, x='audienceRating', y='Vote')
# sns.jointplot(data=dataMoviesFull, x='timeMin', y='grossMillions')

# The DistPlots
# fig, axes = plt.subplots(2, 3)
# fig.set_size_inches(12, 8)
#
# m1 = sns.distplot(dataMoviesFull.audienceRating, bins=15, ax=axes[0, 0])
# m2 = sns.distplot(dataMoviesFull.criticRating, bins=15, ax=axes[0, 1])
# m3 = sns.distplot(dataMoviesFull.timeMin, bins=15, ax=axes[0, 2])
# m4 = sns.distplot(dataMoviesFull.grossMillions, bins=15, ax=axes[1, 0])
# m5 = sns.distplot(dataMoviesFull.Vote, bins=15, ax=axes[1, 1])
# m6 = sns.distplot(dataMoviesFull.Year, bins=15, ax=axes[1, 2])

# The Histograms
