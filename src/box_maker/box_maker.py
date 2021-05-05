import pascal_voc_writer


class BoxMaker:
	def __init__(self, count: int = 10):
		self._count = count

	def test(self):
		writer = pascal_voc_writer.Writer(
			path='hello.jpg',
			width=600,
			height=400,
		)

		writer.addObject(
			name='category1',
			xmin=10,
			ymin=20,
			xmax=30,
			ymax=40,
		)

		writer.save('this.xml')

	def hello(self):
		print('Hello world!')

