from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



from .models import Book, Review, Genre
from .serializers import BookSerializer, ReviewSerializer,GenreSerializer



# Create your views here.


# Create a new book review (with a rating and text) - done
# ● Listing all books based on review ranking - done
# ● Creating a new book. - done
# ● Updating an existing book. - done
# ● Deleting a book.- done

class ListReview(APIView):
    '''
        This view is used for listing the books based on the rating and creating a new review for a book
    '''

    def get(self, request,rating, format=None):
        '''
            url : /rating/<rating>
            response : Response list with book objects greater than <rating> input
        '''
        review =Review.objects.select_related('book').filter(rating__gte = rating)       
        serializer = ReviewSerializer(review,many=True)
        book_ids = []
        for i in serializer.data:
            book_ids.append(i['book'])
        
        book = Book.objects.filter(id__in = book_ids)
        book_data = BookSerializer(book, many=True)
        return Response(book_data.data)
    
    def post(self, request, format=None):
            '''
            function to create a new Review
            '''
            serializer = ReviewSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBooks(APIView):

    '''
        this api view is used to create a new book / list all existing books
    '''
    def get(self, request, format=None):
        '''
            List all books
        '''

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        '''
            Create a New Book
        '''
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    """
    This API view is used to alter/get/delete a specific book
    """

    def get(self, request, pk, format=None):
        '''
            Get a book by Id
        '''
        book  = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    

    def put(self, request, pk, format=None):
        '''
        Update an existing book by id
        '''
        book  = Book.objects.get(id=pk)
        serializer = BookSerializer(book,data = request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):

        '''
        Delete an existing Book
        '''
        book  = Book.objects.get(id=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
    


class ListGenre(APIView):

    '''
        this api view is used to create a new book / list all existing books
    '''
    def get(self, request, format=None):
        '''
            List all genre
        '''

        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        '''
            Create a New Genre
        '''
        serializer = GenreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)