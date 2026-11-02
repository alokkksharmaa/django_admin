from django.http import HttpResponse

# Create your views here.


def set_session(request):
  request.session['username'] = 'Alok Kumar'
  return HttpResponse("Session data Set")


def get_session(request):
  username = request.session.get('username')
  if username is None:
    return HttpResponse("No session data found. Set a session first.", status=404)
  return HttpResponse(f"Session data: {username}")
