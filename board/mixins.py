from django.contrib.auth.mixins import UserPassesTestMixin

class OnlyUserMixin(UserPassesTestMixin):
    # 条件を満たさない場合に403ページに移動
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk']