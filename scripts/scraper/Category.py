class Category:
    def __init__(self, url, name, parent_category):
        self.url = url
        self.name = name
        self.parent_category = parent_category
    
    def __str__(self):
        return f'Category "{self.name}" at {self.url}, under {self.parent_category}'