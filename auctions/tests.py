from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Category, Bid, Listing, Comment

User = get_user_model()

class ModelTests(TestCase):

    def setUp(self):
        # Cria um usuário para os testes
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(categoryName="Cars")
        self.bid = Bid.objects.create(bid=100, user=self.user)
        self.listing = Listing.objects.create(
            title="Test Listing",
            description="Test Description",
            imageUrl="http://example.com/image.jpg",
            price=self.bid,
            owner=self.user,
            category=self.category
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpass'))

    def test_category_creation(self):
        self.assertEqual(str(self.category), "Cars")

    def test_bid_creation(self):
        self.assertEqual(self.bid.bid, 100)
        self.assertEqual(self.bid.user, self.user)

    def test_listing_creation(self):
        self.assertEqual(self.listing.title, "Test Listing")
        self.assertEqual(self.listing.description, "Test Description")
        self.assertEqual(self.listing.price, self.bid)
        self.assertEqual(self.listing.owner, self.user)
        self.assertEqual(self.listing.category, self.category)
        self.assertTrue(self.listing.isActive)

    def test_comment_creation(self):
        comment = Comment.objects.create(author=self.user, listing=self.listing, message="Great listing!")
        self.assertEqual(comment.message, "Great listing!")
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.listing, self.listing)

    def test_listing_str(self):
        self.assertEqual(str(self.listing), "Test Listing")

    def test_comment_str(self):
        comment = Comment.objects.create(author=self.user, listing=self.listing, message="Nice!")
        self.assertEqual(str(comment), f"{self.user} comment on {self.listing}")