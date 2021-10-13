import os.path

import pytest

import common.screenshot_def as SCR
from models.personal_data import PersonalData as Pd

current_dir = os.path.dirname(__file__)
user_images_directory = os.path.join(current_dir, "user_images")


@pytest.mark.personal_data
class TestPersonalData:
    def test_valid_edit_basic_personal_data(self, app, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with valid data
        6. Check successfully editing
        """
        app.login.go_to_editing_personal_data()
        personal_data = Pd.random()
        app.personal_data.edit_personal_data(personal_data)
        SCR.screenshot(app)
        assert app.personal_data.is_changed(), "Personal data not changed!"

    @pytest.mark.parametrize("field", ["name", "last_name", "email"])
    def test_edit_personal_data_without_required_field(self, app, auth, field):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with invalid data
        6. Check editing is not successfully
        """
        app.login.go_to_editing_personal_data()
        personal_data = Pd.random()
        setattr(personal_data, field, "")
        app.personal_data.edit_personal_data(personal_data)
        SCR.screenshot(app)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @pytest.mark.parametrize("email", ["sweeroll.ru", "@mail.ru", "111"])
    def test_edit_personal_data_with_incorrect_email(self, app, auth, email):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with incorrect email
        6. Check editing is not successfully
        """
        app.login.go_to_editing_personal_data()
        data = Pd.random()
        setattr(data, "email", email)
        app.personal_data.edit_personal_data(data)
        SCR.screenshot(app)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @pytest.mark.parametrize(
        "name, last_name",
        [
            ["123", "123"],
            ["---", "---"],
            ["\xbdR6\x10\x7f", "\xbdR6\x10\x7f"],
            [Pd().random().url, Pd().random().url],
            [Pd().random().image_url, Pd().random().image_url],
        ],
    )
    @pytest.mark.xfail
    @pytest.mark.bug
    def test_edit_incorrect_name_lastname(self, app, auth, name, last_name):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit name or(and) lastname as digits
        6. Check editing is not successfully
        """
        app.login.go_to_editing_personal_data()
        personal_data = Pd.random()
        setattr(personal_data, "name", name)
        setattr(personal_data, "last_name", last_name)
        app.personal_data.edit_personal_data(personal_data)
        SCR.screenshot(app)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @pytest.mark.set_user_image
    @pytest.mark.parametrize(
        "image_file",
        [
            os.path.join(user_images_directory, image)
            for image in os.listdir(user_images_directory)
        ],
    )
    def test_valid_edit_more_personal_data(self, app, auth, image_file):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit additional personal data with valid data
        5. Edit user image
        6. Check successfully editing
        """
        app.login.go_to_editing_personal_data()
        personal_data = Pd.random()
        app.personal_data_more.edit_personal_data_more(personal_data)
        SCR.screenshot(app)
        assert app.personal_data_more.is_changed(), \
            "Personal data not changed!"

    def test_valid_edit_optional_personal_data(self, app, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit optional personal data with valid data
        6. Check successfully editing
        """
        app.open_main_page()
        app.login.go_to_editing_personal_data()
        personal_data = Pd.random()
        app.personal_data_optional.edit_personal_data_optional(personal_data)
        SCR.screenshot(app)
        assert app.personal_data_optional.is_changed(), \
            "Personal data not changed!"

    def test_valid_edit_tag_personal_data(self, app, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Add tag with valid data
        6. Check successfully editing
        """
        app.open_main_page()
        app.login.go_to_editing_personal_data()
        personal_data = Pd.random()
        app.personal_data_tag.edit_personal_data_tag(personal_data)
        SCR.screenshot(app)
        assert app.personal_data_tag.is_changed(), "Personal data not changed!"
