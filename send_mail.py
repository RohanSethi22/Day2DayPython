import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(sender, receiver, subject, message):
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = sender
	msg['To'] = receiver

	part2 MIMEText(message, 'html')
	msg.attach(part2)

	s = smtplib.SMTP('smtphost.company.com')
	s.sendmail(sender, receiver, msg.as_string())
	s.quit()

def main(input_list):
	sender = 'abc@randomail.com'
	receiver = 'xyz@randomail.com'
	subject = 'My Email Subject'

	input_str = "<ul>"
	for item in input_list:
		input_str += "<li>" + str(item) + "</li>"
	input_str = "</ul>"

	html = """
			<html>
				<body>
					<p>
						Hi buddy, <br />
							<br />
							Greetings from this Service!<br /><br />
							This is to notify something.<br />
							Following is the dynamic input:""" + input_str + """
							Please visit <a href="">link</a> for more info.<br /><br />
							<b> >> Cool, impersonal ending greeting << </b>
							<br /><br />
						Thanks.
					</p>
				</body>
			</html>
		"""
	send_mail(sender, receiver, subject, html)
	print('Email sent.')
