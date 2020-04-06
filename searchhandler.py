class SearchHandler(object):
    def search_books(self, query, list_books, attributes):
        '''
        returns books that contains the word
        '''
        books_with_keyword = set([])
        for attribute in attributes:
            books_with_keyword = set.union(books_with_keyword, 
                self.search_by_attribute(query, attribute, list_books))
        print(books_with_keyword)
        return books_with_keyword


    def search_by_attribute(self, query, book_attribute, list_books):
        '''
            Checks if the list of book's attibute matches 
            the input query
        '''
        books_with_keyword = []
        for book_id in list_books:
            if list_books[str(book_id)][book_attribute] == query:
                books_with_keyword.append(str(list_books[book_id]['ID']))
        return set(books_with_keyword)

    def exact_phrase_search(self, query, list_books):
        books_with_keyword = []
        for book_id in list_books:
            if query in list_books[str(book_id)]['RawText']:
                books_with_keyword.append(list_books[book_id]['ID'])
        return set(books_with_keyword)

    def checker(self, query, attribute, book):
        if(attribute == 'ContainsTheseWords'):
            if query in book['RawText']:
                return True
            else:
                return False
        if(book[attribute] == query):
            return True
        else:
            return False

    def specific_search(self, queries, list_books):
        books_with_keyword = []
        for book_id in list_books:
            is_book_passed = True
            for query in queries:
                if(is_book_passed == False):
                    break
                is_book_passed = self.checker(queries[query], query, list_books[book_id])
                #print(queries[query])
            if(is_book_passed == True):
                books_with_keyword.append(list_books[book_id]['ID'])
        return books_with_keyword

            
            