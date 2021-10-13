class LoginConstants:
    AUTH_ERROR = "Неверный логин или пароль, попробуйте заново."


class SignUpConstants:
    SIGN_UP_PAGE_URL = "https://qacoursemoodle.innopolis.university/login/signup.php?"


class PersonalDataConstants:
    EMAIL_DISPLAY_MODES = {
        "hidden": "0",
        "all_can_see": "1",
        "show_to_course_participants": "2",
    }
    TIMEZONE_VALUES = (
        "99",  # server's timezone
        "Asia/Dubai",
        "America/Santiago",
        "Africa/Tunis",
        "Europe/Moscow",
        "Europe/Moscow",
        "UTC",
    )
