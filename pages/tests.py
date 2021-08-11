from django.test import SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "index.html")


    def test_about_page_uses_correct_template(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "about.html")

    def test_about_page_loads_correct_content(self):
        response = self.client.get("/about/")
        self.assertContains(response, "Odasys")