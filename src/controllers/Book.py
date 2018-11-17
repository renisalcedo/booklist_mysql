class Book:
    def __init__(self, db):
        self.db = db
        self.table = 'Books'
        self.cursor = db.cursor()

    def new(self, title, author, desc):
        """ Adds a new book to the database
        :type title: str
        :type author: str
        :type desc: str
        :rtype book: dict{str,str,str}
        """
        req_body = (title, author, desc)
        db_props = (self.table, 'title', 'author', 'description')

        sql = "INSERT INTO {0[0]} ({0[1]}, {0[2]}, {0[3]}) \
               VALUES (\"{1[0]}\", \"{1[1]}\", \"{1[2]}\")"

        self.cursor.execute(sql.format(db_props, req_body))

    def get_by_id(self, id):
        """ Finds a Book by the id in the database
        :type id: int
        :rtype book: dict{str,str,str}
        """
        sql = "SELECT * FROM {} WHERE id = {}"

        self.cursor.execute(sql.format(self.table, id))
        data = self.cursor.fetchall()

        if data:
            _,title,author,desc = data[0]
            return {'Title':title,'Author':author,'Description':desc}

        return {'Error': 'id not found'}

    def update(self, id, data):
        """ Updats the data in the books database.
        :type id: int
        :type data: tuple(str,str,str)
        :rtype book: dict{str,str,str}
        """
        data = self.get_by_id(id)

        if data:
            db_props = (self.table, 'title', 'author', 'description')
            sql = 'UPDATE {0[0]} SET {0[1]} = {2[0]}, \
                  {0[2]} = {2[1]}, {0[3]} = {2[2]} WHERE ID = {1[1]}'

            self.cursor.execute(sql.format(db_props, id, data))
            return {'res': 'The record of the book was updated.'}

        return {'Error': 'There was no book with the given id.'}

    def delete(self, id):
        """ Deletes a book from the database
        :type id: int
        :rtype book: dict{str}
        """
        data = self.get_by_id(id)

        if data:
            sql = "DELETE FROM {0} WHERE id = {1}"
            self.cursor.execute(sql.format(self.table, id))
            return {'res': 'The record of the book was deleted.'}

        return {'Error': 'There was no book with the given id.'}

    def save(self):
        """ Saves the data last Added """
        self.db.commit()