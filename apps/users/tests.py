from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UsersManagersTests(TestCase):
    def test_create_user(self):
        """Tes pembuatan user biasa dengan role Cashier"""
        user = User.objects.create_user(username="kasir1", password="foo", role="CASHIER")
        self.assertEqual(user.username, "kasir1")
        self.assertEqual(user.role, "CASHIER")
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        """Tes pembuatan superuser (Admin)"""
        admin_user = User.objects.create_superuser(username="admin", password="foo", role="ADMIN")
        self.assertEqual(admin_user.username, "admin")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)