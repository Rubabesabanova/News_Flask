class News:
    def __init__(self, _id, _title, _content):
        self.id=_id
        self.title=_title
        self.content=_content

news_list = [
    News('1', 'Expecto patronum', "to summon up a Patronus"),
    News('2', 'Accio', "to call an object to you "),
    News('3', 'Wingardium Leviosa', "to levitate objects "),
    News('4', 'Expelliarmus', "to disarm your opponent "),
    News('5', 'Lumos', "to ignite one’s wand-tip to provide light "),
]
