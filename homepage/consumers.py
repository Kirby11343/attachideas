import asyncio
import json
from django.contrib.auth.models import User
from homepage.models import Comment, Post
from channels.db import database_sync_to_async
from channels.consumer import AsyncConsumer

class CommentConsumer(AsyncConsumer):
	
		async def websocket_connect(self, event):
			print('connection successfull', event)
			await self.send({
					'type': 'websocket.accept'
				})
			self.post = 'post'
			await self.channel_layer.group_add(
				self.post,
				self.channel_name
				)

		async def websocket_receive(self, event):
			print('received: ', event)
			new_comment_data = event.get('text')
			new_comment = json.loads(new_comment_data)
			post_id = new_comment['post_id']
			author = new_comment['author']
			comment_text = new_comment['comment_text']
			await self.create_comment(post_id, author, comment_text)
			comment = {
				'comment_text': comment_text,
				'author': author,
			}
			await self.channel_layer.group_send(
				self.post,
				{
					'type': 'show_comment',
					'text': json.dumps(comment)
				}
				)

		async def websocket_disconnect(self, event):
			print('connection closed', event)

		@database_sync_to_async
		def create_comment(self, post_id, author, comment_text):
			author = User.objects.get(username=author)
			post = Post.objects.get(id=post_id)
			Comment.objects.create(post=post, author=author, comment_text=comment_text)
		
		async def show_comment(self, event):
			await self.send({
					'type': 'websocket.send',
					'text': event['text']
				})
