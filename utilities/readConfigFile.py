import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\Admin\PycharmProjects\nopCommerse\configurations\config.ini")

class Read_values():

    @staticmethod
    def getFirstName():
        first_name = config.get('registration info', 'first_name')
        return first_name

    @staticmethod
    def getLastName():
        last_name = config.get('registration info', 'last_name')
        return last_name

    @staticmethod
    def getEmail():
        email = config.get('registration info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('registration info', 'password')
        return password

    @staticmethod
    def getConfirmPassword():
        confirm_password = config.get('registration info', 'confirm_password')
        return confirm_password


# @pytest.fixture(params=[ ("akshay16sakhare@gmail.com", "Babayaga@123", "PASS"),
#                                 ("akshay16sakhare@gmail.com", "@123", "FAIL"),
#                                 ("akshay@gmail.com", "@123", "FAIL"),
#                                 ("akshay16sakhare@gmail.com", "@12345", "FAIL"),
#                                 ("akshay@gmail.com", "@12345", "FAIL")
#                              ]
#                              )
# def get_data_for_login(request):
#     return request.param