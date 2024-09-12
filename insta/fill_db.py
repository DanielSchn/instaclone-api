from insta.models import User, Post, Comment, Like

user1 = User.objects.create(username="Teresina",email_address="teresa@teresa.de",profile_image="profile_images/teresina.png")
user2 = User.objects.create(username="Daniel",email_address="daniel@daniel.de",profile_image="profile_images/daniel.png")
user3 = User.objects.create(username="Cat_Man",email_address="cat@man.de",profile_image="profile_images/katze.png")

post1 = Post.objects.create(user=user1,image="posts/greece.jpg",location="Greece",description="Lovely Friends, ich habe den besten Platz zum Seele baumeln lassen gefunden!")
post2 = Post.objects.create(user=user2,image="posts/scary_cat.jpg",location="Cat Castle",description="Was machen diese niedlichen Tiere eigentlich Nachts? Und warum trägt er eine Fliege?")
post3 = Post.objects.create(user=user3,image="posts/lasagna-3344997_1280.jpg",location="at_Home",description="MjamMjam")

comment1 = Comment.objects.create(post=post1, user=user2, content="Wow ist das schön dort!")
comment2 = Comment.objects.create(post=post2, user=user3, content="Was ist mit denen los?")
comment3 = Comment.objects.create(post=post3, user=user1, content="Bekomme ich was davon?")

Like.objects.create(post=post2, user=user1)
Like.objects.create(post=post2, user=user3)

Like.objects.create(post=post1, user=user3)
Like.objects.create(post=post1, user=user2)

Like.objects.create(post=post3, user=user1)
Like.objects.create(post=post3, user=user2)


#Delete all
Comment.objects.all().delete()
User.objects.all().delete()
Post.objects.all().delete()
Like.objects.all().delete()