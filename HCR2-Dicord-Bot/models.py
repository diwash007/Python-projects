from tortoise import fields
from tortoise.models import Model

class Scores(Model):
	id = fields.IntField(pk=True)
	name = fields.CharField(50)
	score = fields.IntField(50)
	server = fields.IntField()

	class Meta:
		table = "scores"
		table_description = " scores of the players "

class Servers(Model):
	server_id = fields.IntField(pk=True)
	map = fields.CharField(50)
	vehicle = fields.CharField(50)

	class Meta:
		table = "servers"
		table_description = "servers"

