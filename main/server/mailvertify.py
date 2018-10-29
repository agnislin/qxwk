from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
# to_addr =  '1174793397@qq.com'#input('to_addr:')#'1653075632@qq.com'

import random
population = [chr(x) for x in range(48, 58)] + [chr(x)
                                   for x in range(97, 123)] + [chr(x) for x in range(65, 91)]

def randomcode():
    return ''.join(random.sample(population, 10))


def makemail(mail, randomcode):
    url = '47.106.197.83/verify/%s+%s' % (mail, randomcode)
    return '感谢您注册千禧微课帐户！请点击下方链接完成验证： %s 如果无法访问，请复制该链接到浏览器中打开'%url


def sendmail(to_addr, msg):
    smtp_server = 'smtp.qq.com'
    from_addr = '1653075632@qq.com'
    password = 'ezdjupjphxzndifa'
    msg = MIMEText(msg, 'plain', 'utf-8')
    msg['From'] = _format_addr('千禧微课 <%s>' % from_addr)
    msg['To'] = _format_addr('user<%s>' % to_addr)
    msg['Subject'] = Header('邮箱验证通知', 'utf-8').encode()
    try:
        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
    except Exception as e:
        print(e)
        return False
    else:
        return True

def vertify(verticode, dic):
    mail = verticode.split('+')[0]
    rcode = verticode.split('+')[1]
    try:
        rmail = dic[mail]
    except KeyError:
        return False
    else:
        randomcode = rmail['randomcode']
        return rcode == randomcode
