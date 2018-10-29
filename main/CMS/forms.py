# #coding:utf8
# from flask_wtf import FlaskForm
# from wtforms import StringField,PasswordField,SubmitField
# from wtforms.validators import DataRequired

# class LoginForm(FlaskForm):
#     '''管理员登录表单'''
#     account = StringField(
#         label = "帐号",
#         validators = [DataRequired("请输入账号！")]，
#         description="账号"
#         render_kw={
#             "class":"form-comtrol",
#             "placeholder":"请输入账号!",
#             "required":"required"


#         }
#     pwd = PasswordField(
#         label="密码",
#         validators = [DataRequired("请输入密码！")]，
#         description="密码"
#         render_kw={
#             "class":"form-comtrol",
#             "placeholder":"请输入密码!",
#             "required":"required"
#             }
#           )
        



#     submit = SubmitField(

#         '登录',
#         render_kw = {

#             "class":"btn btn-primary btn-block btn-flat",
#         }
#     )

#         