PASSWORD_RESET_URL = '{base_url}/profile/reset-password/{username}'

PROFILE_PAGE_URL = '{base_url}/profile/user/{username}'


class UsernameValidations:

    MAXIMUM_LENGTH = 50
    BLACKLIST_CHARACTERS = ['>', '<', '%', '^', '#', '@', '*', '~', ' ']
