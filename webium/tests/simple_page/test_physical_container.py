from tests.simple_page import SimplePageTest


class TestPhysicalContainer(SimplePageTest):
    def test_physical_container(self):
        assert self.page.physical_container.second_element_with_id.get_attribute('id') == 'preformatted'
