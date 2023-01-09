import smtplib
import ssl


class EmailNotifications:
    def __init__(self):
        self.__port = 587
        self.__server = "smtp.gmail.com"
        self.__sender_email = "testmyapp6969@gmail.com"
        """Receiver email constant can be set to any email. """
        self.__receiver_email = "radic.nikola993@gmail.com"
        """Test email, obscuring the password was not needed. """
        self.__password = "zqlfenazrooqqblf"

    def get_port(self):
        return self.__port

    def get_server(self):
        return self.__server

    def get_sender_email(self):
        return self.__sender_email

    def get_receiver_email(self):
        return self.__receiver_email

    def get_password(self):
        return self.__password

    def send_attention_notification(self):
        message = """\
            Automated notification:

            Your immediate attention is required."""

        context = ssl.create_default_context()
        with smtplib.SMTP(self.get_server(), self.get_port()) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(self.get_sender_email(), self.get_password())
            server.sendmail(self.get_sender_email(), self.get_receiver_email(), message)

    def send_production_completed_notification(self):
        message = """\
            Automated notification:

            Production has been completed."""

        context = ssl.create_default_context()
        with smtplib.SMTP(self.get_server(), self.get_port()) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(self.get_sender_email(), self.get_password())
            server.sendmail(self.get_sender_email(), self.get_receiver_email(), message)

    def send_lacking_resources(self):
        message = """\
            Automated notification:

            Production is lacking resources."""

        context = ssl.create_default_context()
        with smtplib.SMTP(self.get_server(), self.get_port()) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(self.get_sender_email(), self.get_password())
            server.sendmail(self.get_sender_email(), self.get_receiver_email(), message)
