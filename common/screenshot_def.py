import allure
from allure_commons.types import AttachmentType


def screenshot(app=None):
    allure.attach(
        app.personal_data.make_screenshot(),
        name="screenshot",
        attachment_type=AttachmentType.PNG,
    )
