from django.http import HttpResponse

# Create your views here.

def index(request):
    line1 = '<h1 style="text-align: center">黎明之战</h1>'
    line3 = '<a href="/play/">进入游戏界面</a>'
    line2 = '<img src="https://store-images.s-microsoft.com/image/apps.65264.13518670361548729.1f63fff2-f06f-4a63-9044-ca11e254c5ce.cd169869-fd0b-49e4-91ef-7485a390452c?mode=scale&q=90&h=1080&w=1920" width=1200>'
    return HttpResponse(line1 + line3 + line2)


def play(request):
    line1 = '<h1 style="text-align: center">游戏即将开始</h1>'
    line2 = '<a href="/">返回主界面</a>'

    return HttpResponse(line1 + line2)
