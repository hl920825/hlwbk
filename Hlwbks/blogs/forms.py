
from django import forms

from blogs.helper import set_password
from blogs.models import User


class UserForm(forms.ModelForm):
    """用户注册验证"""
    # 单独添加字段
    password = forms.CharField(max_length=16,
                               min_length=6,
                               error_messages={
                                   'required': '密码不能为空',
                                   'max_length': '密码长度最大长度为16位',
                                   'min_length': '密码长度最小长度为6位'
                               })

    repassword = forms.CharField(error_messages={'required': '确认密码不能为空'})

    class Meta:
        model = User
        fields = ['phone', ]
        error_messages = {
            'phone': {
                'required': '手机号不能为空!'
            }
        }

    def clean_phone(self):
        # 验证手机号是否唯一
        phone = self.cleaned_data.get('phone')
        rs = User.objects.filter(phone=phone).exists()
        if rs:
            raise forms.ValidationError('手机号已被被注册!')
        else:
            return phone

    def clean(self):
        # 验证两次密码是否一致
        password = self.cleaned_data.get('password')
        repassword = self.cleaned_data.get('repassword')
        if password and repassword and password != repassword:
            raise forms.ValidationError({'repassword': '两次输入的密码不一致!'})


class LoginForm(forms.ModelForm):
    """用户登录验证"""

    class Meta:
        model = User
        fields = ['phone', 'password']
        error_messages = {
            'phone': {
                'required': '手机号不能为空!'
            },
            'password': {
                'required': '密码不能为空!'
            }
        }

    def clean(self):
        # 验证账号密码是否正确
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        # 根据手机号获取
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            raise forms.ValidationError({'phone': '手机号未被注册!'})
        # 验证密码
        if user.password != set_password(password):
            raise forms.ValidationError({'password': '密码错误!'})
        # 将用户信息保存到cleaned_data中
        self.cleaned_data['user'] = user
        return self.cleaned_data
