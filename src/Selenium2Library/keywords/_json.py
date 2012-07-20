from keywordgroup import KeywordGroup
import json

class _JSONKeywords(KeywordGroup):

	def JSON_from_file(self,json_path):
		"""Given a file path as argument, open the file then parse and return JSON.
		Return appropriate RF list type. See Collections Library docs."""
		filej=open(json_path)
		parsed = json.loads(filej.read())
		return parsed

	def JSON__from_string(self,json_string):
		"""Given a string containing JSON as argument, parse and return JSON.
		Return appropriate RF list type. See Collections Library docs."""
		parsed = json.loads(json_string)
		return parsed