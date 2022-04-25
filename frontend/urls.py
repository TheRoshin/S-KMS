from django.urls import path
from  .views import  home,loginAndSignup,fqa,post,search,logout, signUp, postDe, postDelete, searchRe, ranking, profile,updateProfile, counter, asset, threat, memory, c_code, threat_by,countermeasure_by,updatePassword
urlpatterns = [
    path('', home.home, name = 'home'),
    path('signUp', signUp.signUp, name = 'signUp'),
    path('login', loginAndSignup.userLogin, name = 'login'),
    path('fqa', fqa.fqa, name= 'fqa'),
    path('post', post.PostQus, name= 'post'),
    path('search', search.search, name= 'search'),
    path('searchResults/', searchRe.searchResult, name= 'searchResults'),
    path('logout', logout.userLogout, name = 'logout'),
    path('<slug:slug>/', postDe.post_detail, name='postDetail'),
    path('<slug:slug>/delete', postDelete.post_delete, name='delete'),
    path('rankings', ranking.rank, name='rankings'),
    path('profile/<slug:slug>/', profile.profileView, name='profile'),
    path('updateProfile/<slug:slug>/', updateProfile.updateProfile, name='updateProfile'),
    path('updatePassword/<slug:slug>/', updatePassword.updatePassword, name='updatePassword'),
    path('counter', counter.Counter, name='counter'),
    path('asset', asset.Asset, name='asset'),
    path('threat', threat.Threat, name='threat'),
    path('memory', memory.Memory, name='memory'),
    path('c_code', c_code.C_Code, name='c_code'),
    path('threat_by', threat_by.Threat_by, name='threat_by'),
    path('countermeasure_by', countermeasure_by.Countermeasure_by, name='countermeasure_by')
]