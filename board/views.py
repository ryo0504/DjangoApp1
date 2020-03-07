from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.views import generic
from .models import *
from django.contrib.auth.views import LoginView
from .forms import *
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from .forms import SignUpForm, ThreadForm, PostForm
from .models import User
from .models import Thread
from .models import Post
from .mixins import OnlyUserMixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Lp(generic.TemplateView):
    template_name = 'board/lp.html'


class PostList(generic.TemplateView):
    template_name = 'board/post_list.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'board/login.html'


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'board/sign_up.html'

    def get_success_url(self):
        form = self.get_form()
        # usernameから登録したユーザー情報を参照
        user = User.objects.get(name=form.data.get('name'))

        # ログイン処理を行う
        login(self.request, user)
        return reverse('board:post_list')


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'board/user_detail.html'


class UserUpdateView(OnlyUserMixin, generic.UpdateView):
    model = User
    template_name = "board/user_update.html"
    form_class = UserForm

    def get_success_url(self):
        return reverse_lazy('board:user_detail', kwargs={"pk": self.kwargs["pk"]})


class ThreadCreateView(LoginRequiredMixin, generic.CreateView):
    model = Thread
    template_name = "board/thread/create.html"
    form_class = ThreadForm
    success_url = reverse_lazy("board:thread_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ThreadListView(LoginRequiredMixin, generic.ListView):
    model = Thread
    template_name = "board/thread/thread_list.html"


class ThreadDetailView(LoginRequiredMixin, generic.DetailView):
    model = Thread
    template_name = "board/thread/thread_detail.html"


class ThreadUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Thread
    template_name = "board/thread/thread_update.html"
    form_class = ThreadForm

    def get_success_url(self):
        return resolve_url('board:thread_list')


class ThreadDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Thread
    template_name = "board/thread/delete.html"
    success_url = reverse_lazy("board:thread_list")


def post_list(request, pk):
    # 特定のスレッドにひもづいた投稿を作成する
    # 引数の `pk` はスレッドの `pk` を指すので要注意

    thread = get_object_or_404(Thread, pk=pk)
    post_list = Post.objects.filter(thread=thread)
    form = PostForm(request.POST or None)

    # フォームが送信されて、なおかつその値が正しい場合は投稿データを登録してリダイレクト
    if form.is_valid():
        post = form.save(commit=False)
        post.thread = thread
        post.user = request.user
        post.save()
        return redirect('board:post_list', pk=thread.pk)

    context = {'form': form, 'post_list': post_list, 'thread':thread}
    return render(request, 'board/post/post_list.html', context)


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "board/post/post_detail.html"


# def post_detail(request, thread_pk, pk):
#     thread = get_object_or_404(Thread, pk=thread_pk)
#     post = get_object_or_404(Post, pk=pk, thread=thread)
#     return render(request, 'board/post/post_detail.html', {'post': post})