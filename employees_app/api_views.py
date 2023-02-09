from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .serializers import StudentSerializer
from .models import Student


def not_found_error(status = status.HTTP_404_NOT_FOUND):
    res = {'Invalid': 'Your request is invalid'}
    return Response(res, status = status)

class StudentAPI(APIView):
    """This class will providing endpoints for get,post,patch and delete only.
       So by using this we can get the data, insert data, update and delete also.
    """
    # get request here
    def get(self, request, format=None):
        id = request.data.get('id', None)

        if id is not None:
            try:
                emp = Student.objects.get(pk = id)
            except Student.DoesNotExist:
                return not_found_error()
            else:
                serializer = StudentSerializer(emp)
                return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            all_emp  = Student.objects.all()
            serializer = StudentSerializer(all_emp, many=True)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    # post request for insert data into database
    def post(self, request, format = None):
        # fetching parsed
        permission_classes = [IsAuthenticated]
        python_data =  request.data

        # serializing here
        serializer = StudentSerializer(data = python_data)

        if serializer.is_valid(): # serializer valida or not
            serializer.save()
            res = {'Data Inserted successfuly': serializer.data}
            return Response(res, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # patch request for partial updation
    def patch(self, request, format=None):
        id  = request.data.get('id',None)

        if id is not None:
            try: 
                emp = Student.objects.get(pk = id)
            except Student.DoesNotExist :
                return not_found_error()
            else:
                serializer = StudentSerializer(emp, data = request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    res = {'Student Successfuly Updated': serializer.data}
                    return Response(res, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            error = {'Id is required': "Please Provide Student Id"}
            return Response(error, status = status.HTTP_400_BAD_REQUEST)
        
    # delete request here to delete Student
    def delete(self, request, format=None):
        id  = request.data.get('id', None)
        if id is not None:

            try:
                emp = Student.objects.get(pk = id)
            except Student.DoesNotExist :
                return not_found_error()
            else:
                emp.delete()
                res = {'Deleted': "Student Successfuly Deleted"}
                return Response(res, status = status.HTTP_200_OK)
        else:
            error = {'Id required': "Please provide Id it is required"}
            return Response(error, status = status.HTTP_400_BAD_REQUEST)
        

            