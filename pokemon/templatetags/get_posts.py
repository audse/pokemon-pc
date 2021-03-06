from django.template import Library

from forum.models import Post, Category

register = Library()

@register.assignment_tag
def get_posts():
	post_category = Category.objects.get(name="Announcements")
	get_posts = Post.objects.filter(category=post_category).order_by("-post_time")[:6]
	for post in get_posts:
		post.body_length = 64 - len(post.title)
	return get_posts

@register.assignment_tag
def get_3_posts():
	post_category = Category.objects.get(name="Announcements")
	get_3_posts = Post.objects.filter(category=post_category).order_by("-post_time")[:3]
	for post in get_3_posts:
		post.body_length = 72 - len(post.title)
	return get_3_posts
